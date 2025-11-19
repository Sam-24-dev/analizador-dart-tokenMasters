"""Servicios de análisis para la GUI de TokenMasters.

Este módulo actúa como una capa de fachada (tipo API interna) que
reutiliza los analizadores existentes (lexer.py y parser.py) sin
modificarlos. Proporciona funciones que aceptan código Dart en texto,
ejecutan los análisis correspondientes y regresan resultados
estructurados (tokens, errores, rutas de logs) listos para ser
consumidos por la interfaz gráfica u otros clientes.
"""

from __future__ import annotations

import io
import os
import re
import tempfile
from contextlib import redirect_stdout
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import lexer as lexer_module
import parser as parser_module


# Directorios principales
PROJECT_ROOT = Path(__file__).resolve().parent
LOG_DIR = PROJECT_ROOT / "logs"
TEMP_DIR = LOG_DIR / "tmp"


@dataclass
class AnalysisResult:
    tokens: List[Dict]
    errors: List[Dict]
    log_paths: Dict[str, Optional[str]]
    raw_outputs: Dict[str, str]


def _ensure_directories() -> None:
    """Garantiza que exista la carpeta de logs y la temporal."""
    LOG_DIR.mkdir(exist_ok=True)
    TEMP_DIR.mkdir(exist_ok=True)


def _write_temp_code(code: str) -> Path:
    """Guarda el código Dart en un archivo temporal y retorna su ruta."""
    _ensure_directories()
    fd, path = tempfile.mkstemp(suffix=".dart", dir=str(TEMP_DIR))
    with os.fdopen(fd, "w", encoding="utf-8") as tmp:
        tmp.write(code)
    return Path(path)


def _cleanup_temp_code(path: Path) -> None:
    """Elimina el archivo temporal creado para los analizadores."""
    try:
        path.unlink(missing_ok=True)
    except OSError:
        pass


def _stringify_token_value(value) -> str:
    """Normaliza el valor del token para visualización."""
    if isinstance(value, tuple) and len(value) == 2 and value[0] == "str":
        return value[1]
    return str(value)


def _extract_log_path(output: str) -> Optional[str]:
    """Busca en la salida del analizador una línea con el path del log."""
    for line in output.splitlines():
        line = line.strip()
        if line.lower().startswith("log:"):
            return line.split("Log:", 1)[1].strip()
    return None


def _extract_line_number(message: str) -> Optional[int]:
    """Obtiene el número de línea desde un mensaje estándar."""
    match = re.search(r"[Ll][íi]nea\s+(\d+)", message)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            return None
    return None


def _format_error_entry(message: str, kind: str) -> Dict:
    """Crea una entrada uniforme de error para la GUI."""
    return {
        "type": kind,
        "line": _extract_line_number(message),
        "description": message,
    }


def run_lexical_analysis(code: str, git_user: str) -> Dict:
    """Ejecuta el análisis léxico directamente sobre el texto recibido."""
    _ensure_directories()

    tokens: List[Dict] = []
    errors: List[Dict] = []
    token_count = 0

    original_t_error = lexer_module.t_error

    def custom_t_error(t):
        message = (
            f"Carácter ilegal '{t.value[0]}' en línea {t.lexer.lineno}, "
            f"columna {lexer_module.find_column(t)}"
        )
        errors.append(
            {
                "type": "Léxico",
                "line": t.lexer.lineno,
                "description": message,
            }
        )
        t.lexer.skip(1)

    lexer_module.t_error = custom_t_error

    try:
        ply_lexer = lexer_module.build_lexer()
        ply_lexer.input(code)

        while True:
            tok = ply_lexer.token()
            if not tok:
                break

            token_count += 1
            tokens.append(
                {
                    "num": token_count,
                    "token": tok.type,
                    "value": _stringify_token_value(tok.value),
                    "line": tok.lineno,
                }
            )
    finally:
        lexer_module.t_error = original_t_error

    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y-%Hh%M")
    log_filename = LOG_DIR / f"lexico-{git_user}-{timestamp}.txt"

    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write("=" * 80 + "\n")
        log_file.write("  ANÁLISIS LÉXICO - DART\n")
        log_file.write("  Proyecto: TokenMasters\n")
        log_file.write("=" * 80 + "\n\n")
        log_file.write(f" Usuario: {git_user}\n")
        log_file.write(f" Fecha y hora: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
        log_file.write("\n" + "=" * 80 + "\n")
        log_file.write("  TOKENS RECONOCIDOS\n")
        log_file.write("=" * 80 + "\n\n")
        log_file.write(f"{'#':<6} | {'TIPO':<20} | {'LÍNEA':<6} | {'VALOR'}\n")
        log_file.write("-" * 80 + "\n")

        for token in tokens:
            log_file.write(
                f"{token['num']:<6} | {token['token']:<20} | "
                f"{token['line']:<6} | {token['value']}\n"
            )

        log_file.write("\n" + "=" * 80 + "\n")
        log_file.write("  ESTADÍSTICAS\n")
        log_file.write("=" * 80 + "\n\n")
        log_file.write(f" Total de tokens reconocidos: {token_count}\n")
        log_file.write(f" Total de errores léxicos: {len(errors)}\n")

        if errors:
            log_file.write("\n" + "=" * 80 + "\n")
            log_file.write("  ERRORES ENCONTRADOS\n")
            log_file.write("=" * 80 + "\n\n")
            for error in errors:
                log_file.write(
                    f" Línea {error['line']}: {error['description']}\n"
                )

        log_file.write("\n" + "=" * 80 + "\n")
        log_file.write(f"  Análisis realizado por: {git_user}\n")
        log_file.write("  Analizador Léxico para Dart - TokenMasters\n")
        log_file.write("=" * 80 + "\n")

    return {
        "tokens": tokens,
        "errors": errors,
        "log_path": str(log_filename),
        "stats": {
            "token_count": token_count,
            "error_count": len(errors),
        },
    }


def _run_parser_phase(
    phase: str,
    code: str,
    git_user: str,
) -> Dict:
    """Ejecuta cualquiera de las fases del parser (sintáctica o semántica)."""

    temp_path = _write_temp_code(code)
    buffer = io.StringIO()

    try:
        if phase == "syntax":
            analysis_fn = parser_module.analyze_syntax
        elif phase == "semantic":
            analysis_fn = parser_module.analyze_semantic
        else:
            raise ValueError(f"Fase desconocida: {phase}")

        with redirect_stdout(buffer):
            analysis_fn(str(temp_path), git_user)

        raw_output = buffer.getvalue()
        log_path = _extract_log_path(raw_output)
        if log_path and not os.path.isabs(log_path):
            log_path = str((PROJECT_ROOT / log_path).resolve())

        if phase == "syntax":
            raw_errors = list(parser_module.syntax_errors)
            kind = "Sintáctico"
        else:
            raw_errors = list(parser_module.semantic_errors)
            kind = "Semántico"

        errors = [_format_error_entry(message, kind) for message in raw_errors]

        return {
            "errors": errors,
            "log_path": log_path,
            "raw_output": raw_output,
        }
    finally:
        _cleanup_temp_code(temp_path)


def run_syntax_analysis(code: str, git_user: str) -> Dict:
    """Analiza la sintaxis del código recibido."""
    return _run_parser_phase("syntax", code, git_user)


def run_semantic_analysis(code: str, git_user: str) -> Dict:
    """Analiza la semántica del código recibido."""
    return _run_parser_phase("semantic", code, git_user)


def run_full_analysis(code: str, git_user: str) -> AnalysisResult:
    """Ejecuta léxico, sintáctico y semántico secuencialmente."""
    lexical = run_lexical_analysis(code, git_user)
    syntax = run_syntax_analysis(code, git_user)
    semantic = run_semantic_analysis(code, git_user)

    combined_errors: List[Dict] = []
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
        raw_outputs={
            "lexico": "",
            "sintactico": syntax["raw_output"],
            "semantico": semantic["raw_output"],
        },
    )
