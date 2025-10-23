from pathlib import Path
from ..logging_setup import logger
from ...tools.c2rust_wrapper import c2rust_translate
def translate(sources: list[Path], workspace: Path, name: str) -> Path:
    out = workspace / "rust" / name
    c2rust_translate(sources, out)
    logger.info(f"Translator: baseline -> {out}")
    return out
