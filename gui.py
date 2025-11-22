"""GUI de TokenMasters con estilo inspirado en la referencia Vercel.

Incluye:
- Numeración de líneas sincronizada con el editor.
- Indicador visual del progreso (léxico, sintáctico, semántico).
- Tarjetas coloreadas para errores por tipo.
- Botones para abrir cada log generado.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Iterable, List


def _ensure_tcl_env() -> None:
    """Configura rutas de TCL/TK si la instalación no las expone."""

    python_dir = Path(sys.executable).parent
    tcl_dir = python_dir / "tcl"
    tcl_library = tcl_dir / "tcl8.6"
    tk_library = tcl_dir / "tk8.6"

    if tcl_library.exists() and tk_library.exists():
        os.environ["TCL_LIBRARY"] = str(tcl_library)
        os.environ["TK_LIBRARY"] = str(tk_library)


_ensure_tcl_env()

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from analyzer_service import (
    AnalysisResult,
    run_lexical_analysis,
    run_semantic_analysis,
    run_syntax_analysis,
)


class AnalyzerGUI:
    COLORS = {
        "bg": "#eef1f7",
        "header_bg": "#1f2937",
        "header_fg": "#f8fafc",
        "card_bg": "#ffffff",
        "editor_bg": "#0b1220",
        "editor_fg": "#f1f5f9",
        "line_bg": "#0f172a",
        "line_fg": "#a5b4fc",
        "comment_fg": "#60a5fa",
        "button_primary": "#1d4ed8",
        "button_primary_hover": "#1a3fb5",
        "button_secondary": "#dbeafe",
        "status_bg": "#111827",
        "status_fg": "#e2e8f0",
        "card_shadow": "#d0d7e6",
    }

    ERROR_COLORS = {
        "Léxico": ("#fee2e2", "#b91c1c"),
        "Sintáctico": ("#fef3c7", "#92400e"),
        "Semántico": ("#ede9fe", "#5b21b6"),
    }

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("TokenMasters – Analizador Dart")
        self.root.geometry("1240x760")
        self.root.configure(bg=self.COLORS["bg"])

        self.git_user_var = tk.StringVar(value="Sam-24-dev")
        self.status_var = tk.StringVar(value="Estado: Listo")
        self.progress_var = tk.StringVar(value="· Léxico | · Sintáctico | · Semántico")
        self.file_var = tk.StringVar(value="Sin archivo cargado")
        self.phases = ("lexico", "sintactico", "semantico")
        self.log_path_vars = {
            "lexico": tk.StringVar(value="--"),
            "sintactico": tk.StringVar(value="--"),
            "semantico": tk.StringVar(value="--"),
        }
        self.log_paths = {phase: None for phase in self.phases}

        self._create_styles()
        self._build_layout()
        self._update_line_numbers()
        self._apply_basic_highlighting()

    # ------------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------------
    def _create_styles(self) -> None:
        style = ttk.Style(self.root)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Card.TFrame", background=self.COLORS["card_bg"], relief="flat")
        style.configure("Header.TLabel", font=("Segoe UI", 13, "bold"), foreground=self.COLORS["header_fg"], background=self.COLORS["header_bg"])
        style.configure("Section.TLabel", font=("Segoe UI", 12, "bold"), background=self.COLORS["card_bg"], foreground="#111827")
        style.configure("Body.TLabel", background=self.COLORS["card_bg"], foreground="#333")
        style.configure("Info.TLabel", background=self.COLORS["header_bg"], foreground=self.COLORS["header_fg"])

        style.configure(
            "Primary.TButton",
            padding=10,
            foreground="#ffffff",
            background=self.COLORS["button_primary"],
            font=("Segoe UI", 10, "bold"),
        )
        style.map(
            "Primary.TButton",
            background=[("active", self.COLORS["button_primary_hover"]), ("disabled", "#94a3b8")],
            foreground=[("disabled", "#e2e8f0")],
        )

        style.configure(
            "Secondary.TButton",
            padding=8,
            background=self.COLORS["button_secondary"],
            foreground="#1f2937",
            font=("Segoe UI", 10),
        )
        style.map("Secondary.TButton", background=[("active", "#e2e8f0")])

        style.configure("Treeview", font=("Segoe UI", 10), rowheight=24)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    def _build_layout(self) -> None:
        self._build_header()
        self._build_main_content()
        self._build_logs_panel()
        self._build_status_bar()

    def _build_header(self) -> None:
        header = tk.Frame(self.root, bg=self.COLORS["header_bg"], pady=12, padx=24)
        header.pack(fill="x")

        title = ttk.Label(header, text="TokenMasters – Analizador Dart", style="Header.TLabel")
        title.pack(side="left")

        user_frame = tk.Frame(header, bg=self.COLORS["header_bg"])
        user_frame.pack(side="right")
        ttk.Label(user_frame, text="Usuario Git", style="Info.TLabel").pack(anchor="e")
        self.git_entry = ttk.Entry(user_frame, textvariable=self.git_user_var, width=24)
        self.git_entry.pack(pady=2)
        user_hint = ttk.Label(user_frame, text="(Usado para nombrar los logs)", style="Info.TLabel")
        user_hint.configure(font=("Segoe UI", 8))
        user_hint.pack(anchor="e")

    def _build_main_content(self) -> None:
        main_frame = tk.Frame(self.root, bg=self.COLORS["bg"], padx=24, pady=16)
        main_frame.pack(fill="both", expand=True)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        self._build_editor_card(main_frame)
        self._build_results_card(main_frame)

    def _build_editor_card(self, parent: tk.Frame) -> None:
        card = tk.Frame(parent, bg=self.COLORS["card_bg"], bd=0, highlightthickness=1, highlightbackground=self.COLORS["card_shadow"], padx=18, pady=16)
        card.grid(row=0, column=0, sticky="nsew", padx=(0, 16))

        header = ttk.Label(card, text="Editor de Código", style="Section.TLabel")
        header.grid(row=0, column=0, sticky="w")

        self.file_label = ttk.Label(card, textvariable=self.file_var, style="Body.TLabel")
        self.file_label.grid(row=1, column=0, sticky="w", pady=(2, 10))

        buttons = tk.Frame(card, bg=self.COLORS["card_bg"])
        buttons.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 10))
        self.load_button = self._create_button(buttons, "Cargar .dart", self.load_file)
        self.load_button.pack(side="left", padx=4)
        self.clear_button = self._create_button(buttons, "Limpiar", self.clear_all)
        self.clear_button.pack(side="left", padx=4)
        self.analyze_button = self._create_button(
            buttons,
            "▶ Analizar Completo",
            self.analyze_code,
            primary=True,
        )
        self.analyze_button.pack(side="left", padx=(8, 0))

        editor_container = tk.Frame(card, bg=self.COLORS["card_bg"])
        editor_container.grid(row=3, column=0, columnspan=2, sticky="nsew")
        card.rowconfigure(3, weight=1)
        card.columnconfigure(0, weight=1)
        editor_container.rowconfigure(0, weight=1)
        editor_container.rowconfigure(1, weight=0)
        editor_container.columnconfigure(0, weight=0)
        editor_container.columnconfigure(1, weight=1)
        editor_container.columnconfigure(2, weight=0)

        self.line_numbers = tk.Text(
            editor_container,
            width=5,
            padx=6,
            takefocus=0,
            border=0,
            state="disabled",
            background=self.COLORS["line_bg"],
            foreground=self.COLORS["line_fg"],
            font=("Cascadia Code", 11),
        )
        self.line_numbers.grid(row=0, column=0, sticky="ns")

        self.text_editor = tk.Text(
            editor_container,
            wrap="none",
            font=("Cascadia Code", 11),
            background=self.COLORS["editor_bg"],
            foreground=self.COLORS["editor_fg"],
            insertbackground="#93c5fd",
            relief="flat",
            undo=True,
        )
        self.text_editor.grid(row=0, column=1, sticky="nsew")

        self.text_editor.tag_configure("comment", foreground=self.COLORS["comment_fg"])

        self.text_editor.bind("<KeyRelease>", self._on_text_modified)
        self.text_editor.bind("<MouseWheel>", self._on_text_modified)
        self.text_editor.bind("<ButtonRelease-1>", self._on_text_modified)
        self.text_editor.bind("<Configure>", self._on_text_modified)
        self.text_editor.edit_modified(False)

        self.y_scroll = ttk.Scrollbar(editor_container, orient="vertical", command=self._on_scrollbar)
        self.y_scroll.grid(row=0, column=2, sticky="ns")
        self.text_editor.configure(yscrollcommand=self._on_textscroll)
        self.line_numbers.configure(yscrollcommand=self._on_textscroll)

        self.x_scroll = ttk.Scrollbar(editor_container, orient="horizontal", command=self.text_editor.xview)
        self.x_scroll.grid(row=1, column=1, sticky="ew")
        self.text_editor.configure(xscrollcommand=self.x_scroll.set)

    def _build_results_card(self, parent: tk.Frame) -> None:
        card = tk.Frame(parent, bg=self.COLORS["card_bg"], bd=0, highlightthickness=1, highlightbackground=self.COLORS["card_shadow"], padx=18, pady=16)
        card.grid(row=0, column=1, sticky="nsew")
        parent.rowconfigure(0, weight=1)

        header_frame = tk.Frame(card, bg=self.COLORS["card_bg"])
        header_frame.pack(fill="x")
        
        ttk.Label(header_frame, text="Panel de Resultados", style="Section.TLabel").pack(side="left")
        
        self.fullscreen_button = self._create_button(header_frame, "⛶ Ver completo", self._show_fullscreen_results, primary=False)
        self.fullscreen_button.pack(side="right")

        self.notebook = ttk.Notebook(card)
        self.notebook.pack(fill="both", expand=True, pady=(10, 0))

        self._build_tokens_tab()
        self._build_errors_tab()

    def _build_tokens_tab(self) -> None:
        self.tokens_tab = ttk.Frame(self.notebook, style="Card.TFrame")
        self.notebook.add(self.tokens_tab, text="Tokens (0)")

        self.tokens_tree = ttk.Treeview(
            self.tokens_tab,
            columns=("num", "token", "value", "line"),
            show="headings",
        )
        self.tokens_tree.heading("num", text="#")
        self.tokens_tree.heading("token", text="Token")
        self.tokens_tree.heading("value", text="Valor")
        self.tokens_tree.heading("line", text="Línea")
        self.tokens_tree.column("num", width=60, anchor="center")
        self.tokens_tree.column("token", width=160, anchor="w")
        self.tokens_tree.column("value", width=260, anchor="w")
        self.tokens_tree.column("line", width=80, anchor="center")
        self.tokens_tree.pack(fill="both", expand=True, side="left")

        y_scroll = ttk.Scrollbar(self.tokens_tab, orient="vertical", command=self.tokens_tree.yview)
        y_scroll.pack(side="right", fill="y")
        x_scroll = ttk.Scrollbar(self.tokens_tab, orient="horizontal", command=self.tokens_tree.xview)
        x_scroll.pack(fill="x", side="bottom")
        self.tokens_tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    def _build_errors_tab(self) -> None:
        self.errors_tab = ttk.Frame(self.notebook, style="Card.TFrame")
        self.notebook.add(self.errors_tab, text="Errores (0)")

        self.error_cards_frame = tk.Frame(self.errors_tab, bg=self.COLORS["card_bg"])
        self.error_cards_frame.pack(fill="x", pady=(0, 10))

        tree_frame = tk.Frame(self.errors_tab, bg=self.COLORS["card_bg"])
        tree_frame.pack(fill="both", expand=True)

        self.errors_tree = ttk.Treeview(
            tree_frame,
            columns=("type", "line", "description"),
            show="headings",
        )
        self.errors_tree.heading("type", text="Tipo")
        self.errors_tree.heading("line", text="Línea")
        self.errors_tree.heading("description", text="Descripción")
        self.errors_tree.column("type", width=140, anchor="w")
        self.errors_tree.column("line", width=90, anchor="center")
        self.errors_tree.column("description", width=360, anchor="w")
        self.errors_tree.tag_configure("error", foreground="#b91c1c")
        self.errors_tree.pack(fill="both", expand=True, side="left")

        y_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.errors_tree.yview)
        y_scroll.pack(side="right", fill="y")
        x_scroll = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.errors_tree.xview)
        x_scroll.pack(fill="x", side="bottom")
        self.errors_tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    def _build_logs_panel(self) -> None:
        logs_frame = tk.Frame(self.root, bg=self.COLORS["bg"], padx=24)
        logs_frame.pack(fill="x", pady=(0, 8))

        card = tk.Frame(logs_frame, bg=self.COLORS["card_bg"], bd=0, highlightthickness=1, highlightbackground=self.COLORS["card_shadow"], padx=18, pady=12)
        card.pack(fill="x")

        ttk.Label(card, text="Logs generados", style="Section.TLabel").grid(row=0, column=0, sticky="w")
        card.columnconfigure(1, weight=1)

        for idx, (key, title) in enumerate((
            ("lexico", "Léxico"),
            ("sintactico", "Sintáctico"),
            ("semantico", "Semántico"),
        )):
            ttk.Label(card, text=f"{title}:", style="Body.TLabel").grid(row=idx + 1, column=0, sticky="w", pady=2)
            label = ttk.Label(card, textvariable=self.log_path_vars[key], style="Body.TLabel")
            label.grid(row=idx + 1, column=1, sticky="w")
            button = ttk.Button(card, text="Abrir", style="Secondary.TButton", command=lambda k=key: self._open_log(k))
            button.grid(row=idx + 1, column=2, padx=6)

    def _build_status_bar(self) -> None:
        status = tk.Frame(self.root, bg=self.COLORS["status_bg"], padx=24, pady=10)
        status.pack(fill="x")

        ttk.Label(status, textvariable=self.status_var, style="Info.TLabel").pack(side="left")
        ttk.Label(status, textvariable=self.progress_var, style="Info.TLabel").pack(side="right")

    def _create_button(self, parent: tk.Widget, text: str, command, primary: bool = False) -> tk.Button:
        bg = self.COLORS["button_primary"] if primary else self.COLORS["button_secondary"]
        fg = "#f8fafc" if primary else "#0f172a"
        active_bg = self.COLORS["button_primary_hover"] if primary else "#cbd5f5"
        font = ("Segoe UI", 10, "bold" if primary else "normal")

        return tk.Button(
            parent,
            text=text,
            command=command,
            font=font,
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=fg,
            borderwidth=0,
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
            highlightthickness=0,
        )

    # ------------------------------------------------------------------
    # Editor helpers
    # ------------------------------------------------------------------
    def _on_text_modified(self, event=None) -> None:
        if self.text_editor.edit_modified():
            self.text_editor.edit_modified(False)
        self._update_line_numbers()
        self._apply_basic_highlighting()

    def _update_line_numbers(self) -> None:
        content = self.text_editor.get("1.0", "end-1c")
        line_count = content.count("\n") + 1
        numbers = "\n".join(f"{i:>3}" for i in range(1, line_count + 1))
        self.line_numbers.configure(state="normal")
        self.line_numbers.delete("1.0", "end")
        self.line_numbers.insert("1.0", numbers)
        self.line_numbers.configure(state="disabled")

    def _apply_basic_highlighting(self) -> None:
        if not hasattr(self, "text_editor"):
            return

        self.text_editor.tag_remove("comment", "1.0", "end")
        start = "1.0"
        while True:
            idx = self.text_editor.search("//", start, stopindex="end")
            if not idx:
                break
            line = idx.split(".")[0]
            line_end = f"{line}.end"
            self.text_editor.tag_add("comment", idx, line_end)
            start = line_end

    def _on_textscroll(self, *args) -> None:
        self.y_scroll.set(*args)
        self.line_numbers.yview_moveto(args[0])

    def _on_scrollbar(self, *args) -> None:
        self.text_editor.yview(*args)
        self.line_numbers.yview(*args)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def load_file(self) -> None:
        path = filedialog.askopenfilename(
            title="Selecciona un archivo Dart",
            filetypes=[("Archivos Dart", "*.dart"), ("Todos los archivos", "*.*")],
        )
        if not path:
            return

        try:
            content = Path(path).read_text(encoding="utf-8")
        except OSError as exc:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{exc}")
            return

        self.text_editor.delete("1.0", "end")
        self.text_editor.insert("1.0", content)
        self.file_var.set(f"Archivo: {Path(path).name}")
        self._update_line_numbers()
        self._apply_basic_highlighting()
        self.set_status(f"Archivo {Path(path).name} cargado")

    def clear_all(self) -> None:
        self.text_editor.delete("1.0", "end")
        self._clear_tree(self.tokens_tree)
        self._clear_tree(self.errors_tree)
        self.notebook.tab(self.tokens_tab, text="Tokens (0)")
        self.notebook.tab(self.errors_tab, text="Errores (0)")
        self.file_var.set("Sin archivo cargado")
        for var in self.log_path_vars.values():
            var.set("--")
        self.log_paths = {phase: None for phase in self.phases}
        self._render_error_cards([])
        self.set_status("Editor limpio")
        self.progress_var.set("· Léxico | · Sintáctico | · Semántico")
        self._update_line_numbers()
        self._apply_basic_highlighting()

    def analyze_code(self) -> None:
        code = self.text_editor.get("1.0", "end").strip()
        if not code:
            messagebox.showwarning("Advertencia", "El editor está vacío. Carga o escribe código antes de analizar.")
            return

        git_user = self.git_user_var.get().strip() or "TokenMasters"
        self._set_buttons_state("disabled")
        self.set_status("Analizando código…")

        try:
            result = self._run_pipeline(code, git_user)
        except Exception as exc:
            messagebox.showerror("Error", f"Ocurrió un error durante el análisis:\n{exc}")
            self.set_status("Error durante el análisis")
            self._set_buttons_state("normal")
            self.progress_var.set("· Léxico | · Sintáctico | · Semántico")
            return

        self._populate_tokens(result.tokens)
        self._populate_errors(result.errors)
        self._render_error_cards(result.errors)

        self.notebook.tab(self.tokens_tab, text=f"Tokens ({len(result.tokens)})")
        self.notebook.tab(self.errors_tab, text=f"Errores ({len(result.errors)})")

        for key, path in result.log_paths.items():
            self.log_path_vars[key].set(path or "--")
            self.log_paths[key] = path

        self.set_status(
            f"Análisis completado. {len(result.tokens)} tokens reconocidos, {len(result.errors)} errores."
        )
        self.progress_var.set("✔ Léxico | ✔ Sintáctico | ✔ Semántico")
        self._set_buttons_state("normal")

    def _run_pipeline(self, code: str, git_user: str) -> AnalysisResult:
        self.progress_var.set("… Léxico | · Sintáctico | · Semántico")
        lexical = run_lexical_analysis(code, git_user)
        self.progress_var.set("✔ Léxico | … Sintáctico | · Semántico")
        syntax = run_syntax_analysis(code, git_user)
        self.progress_var.set("✔ Léxico | ✔ Sintáctico | … Semántico")
        semantic = run_semantic_analysis(code, git_user)

        combined_errors: List[dict] = []
        combined_errors.extend(lexical["errors"])
        combined_errors.extend(syntax["errors"])
        combined_errors.extend(semantic["errors"])

        return AnalysisResult(
            tokens=lexical["tokens"],
            errors=combined_errors,
            log_paths={
                "lexico": lexical["log_path"],
                "sintactico": syntax["log_path"],
                "semantico": semantic["log_path"],
            },
            raw_outputs={"lexico": "", "sintactico": syntax["raw_output"], "semantico": semantic["raw_output"]},
        )

    # ------------------------------------------------------------------
    # Population helpers
    # ------------------------------------------------------------------
    def _set_buttons_state(self, state: str) -> None:
        for button in (self.load_button, self.analyze_button, self.clear_button):
            button.configure(state=state)

    def _populate_tokens(self, tokens: Iterable[dict]) -> None:
        self._clear_tree(self.tokens_tree)
        for idx, token in enumerate(tokens):
            tag = "odd" if idx % 2 else "even"
            self.tokens_tree.insert(
                "",
                "end",
                values=(
                    token.get("num"),
                    token.get("token"),
                    token.get("value"),
                    token.get("line"),
                ),
                tags=(tag,),
            )
        self.tokens_tree.tag_configure("odd", background="#f8fafc")

    def _populate_errors(self, errors: Iterable[dict]) -> None:
        self._clear_tree(self.errors_tree)
        for error in errors:
            self.errors_tree.insert(
                "",
                "end",
                values=(error.get("type"), error.get("line"), error.get("description")),
                tags=("error",),
            )

    def _render_error_cards(self, errors: Iterable[dict]) -> None:
        for child in self.error_cards_frame.winfo_children():
            child.destroy()

        errors = list(errors)
        if not errors:
            tk.Label(
                self.error_cards_frame,
                text="Sin errores. Ejecuta un análisis para ver resultados.",
                bg=self.COLORS["card_bg"],
                fg="#4b5563",
                font=("Segoe UI", 10),
            ).pack(anchor="w")
            return

        # Ordenar por número de línea para mostrar los primeros errores cronológicamente
        sorted_errors = sorted(errors, key=lambda e: e.get('line') if e.get('line') not in (None, 'None') else 9999)

        for error in sorted_errors[:4]:
            bg, fg = self.ERROR_COLORS.get(error.get("type"), ("#e5e7eb", "#111827"))
            card = tk.Frame(self.error_cards_frame, bg=bg, padx=12, pady=8, bd=0, relief="flat")
            card.pack(fill="x", pady=3)
            tk.Label(card, text=f"{error.get('type')} (Línea {error.get('line') or '-'}).", bg=bg, fg=fg, font=("Segoe UI", 10, "bold")).pack(anchor="w")
            tk.Label(card, text=error.get("description"), bg=bg, fg=fg, font=("Segoe UI", 10)).pack(anchor="w")

    def _clear_tree(self, tree: ttk.Treeview) -> None:
        for item in tree.get_children():
            tree.delete(item)

    def _open_log(self, key: str) -> None:
        path = self.log_paths.get(key)
        if not path:
            messagebox.showinfo("Logs", "Aún no se ha generado este log.")
            return
        if not os.path.exists(path):
            messagebox.showwarning("Logs", f"El archivo ya no existe:\n{path}")
            return
        try:
            os.startfile(path)  # type: ignore[attr-defined]
        except AttributeError:
            messagebox.showinfo("Logs", path)

    def _show_fullscreen_results(self) -> None:
        """Muestra los resultados en una ventana de pantalla completa."""
        fullscreen_win = tk.Toplevel(self.root)
        fullscreen_win.title("TokenMasters - Resultados Completos")
        fullscreen_win.geometry("1200x800")
        fullscreen_win.configure(bg=self.COLORS["bg"])

        # Header
        header = tk.Frame(fullscreen_win, bg=self.COLORS["header_bg"], pady=12, padx=24)
        header.pack(fill="x")
        ttk.Label(header, text="Resultados del Análisis", style="Header.TLabel").pack(side="left")
        close_btn = self._create_button(header, "X Cerrar", fullscreen_win.destroy)
        close_btn.pack(side="right")

        # Tarjetas de errores (primeras 4)
        cards_container = tk.Frame(fullscreen_win, bg=self.COLORS["bg"])
        cards_container.pack(fill="x", padx=24, pady=(16, 8))
        
        all_errors = [self.errors_tree.item(item, "values") for item in self.errors_tree.get_children()]
        # Ordenar por línea
        sorted_errors = sorted(all_errors, key=lambda e: int(e[1]) if str(e[1]).isdigit() else 9999)
        for error_values in sorted_errors[:4]:
            error_type, error_line, error_desc = error_values
            bg, fg = self.ERROR_COLORS.get(error_type, ("#e5e7eb", "#111827"))
            card = tk.Frame(cards_container, bg=bg, padx=12, pady=8, bd=0, relief="flat")
            card.pack(fill="x", pady=3)
            tk.Label(card, text=f"{error_type} (Línea {error_line}).", bg=bg, fg=fg, font=("Segoe UI", 10, "bold")).pack(anchor="w")
            tk.Label(card, text=error_desc, bg=bg, fg=fg, font=("Segoe UI", 10)).pack(anchor="w")

        # Notebook con resultados
        notebook = ttk.Notebook(fullscreen_win)
        notebook.pack(fill="both", expand=True, padx=24, pady=(0, 16))

        # Tab de tokens
        tokens_frame = ttk.Frame(notebook, style="Card.TFrame")
        notebook.add(tokens_frame, text=f"Tokens ({self.tokens_tree.get_children().__len__()})")
        
        tokens_tree = ttk.Treeview(tokens_frame, columns=("num", "token", "value", "line"), show="headings")
        tokens_tree.heading("num", text="#")
        tokens_tree.heading("token", text="Token")
        tokens_tree.heading("value", text="Valor")
        tokens_tree.heading("line", text="Línea")
        tokens_tree.column("num", width=80, anchor="center")
        tokens_tree.column("token", width=200, anchor="w")
        tokens_tree.column("value", width=400, anchor="w")
        tokens_tree.column("line", width=100, anchor="center")
        
        for item in self.tokens_tree.get_children():
            values = self.tokens_tree.item(item, "values")
            tokens_tree.insert("", "end", values=values)
        
        tokens_tree.pack(fill="both", expand=True, side="left")
        tokens_y_scroll = ttk.Scrollbar(tokens_frame, orient="vertical", command=tokens_tree.yview)
        tokens_y_scroll.pack(side="right", fill="y")
        tokens_x_scroll = ttk.Scrollbar(tokens_frame, orient="horizontal", command=tokens_tree.xview)
        tokens_x_scroll.pack(fill="x", side="bottom")
        tokens_tree.configure(yscrollcommand=tokens_y_scroll.set, xscrollcommand=tokens_x_scroll.set)

        # Tab de errores
        errors_frame = ttk.Frame(notebook, style="Card.TFrame")
        notebook.add(errors_frame, text=f"Errores ({self.errors_tree.get_children().__len__()})")
        
        errors_tree = ttk.Treeview(errors_frame, columns=("type", "line", "description"), show="headings")
        errors_tree.heading("type", text="Tipo")
        errors_tree.heading("line", text="Línea")
        errors_tree.heading("description", text="Descripción")
        errors_tree.column("type", width=150, anchor="w")
        errors_tree.column("line", width=100, anchor="center")
        errors_tree.column("description", width=700, anchor="w")
        errors_tree.tag_configure("error", foreground="#b91c1c")
        
        for item in self.errors_tree.get_children():
            values = self.errors_tree.item(item, "values")
            errors_tree.insert("", "end", values=values, tags=("error",))
        
        errors_tree.pack(fill="both", expand=True, side="left")
        errors_y_scroll = ttk.Scrollbar(errors_frame, orient="vertical", command=errors_tree.yview)
        errors_y_scroll.pack(side="right", fill="y")
        errors_x_scroll = ttk.Scrollbar(errors_frame, orient="horizontal", command=errors_tree.xview)
        errors_x_scroll.pack(fill="x", side="bottom")
        errors_tree.configure(yscrollcommand=errors_y_scroll.set, xscrollcommand=errors_x_scroll.set)

    def set_status(self, message: str) -> None:
        self.status_var.set(message)


def main() -> None:
    root = tk.Tk()
    AnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
