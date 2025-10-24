from pathlib import Path
from ..utils/shell import run
from ..logging_setup import logger
def lint(rust_crate_dir: Path) -> None:
    run(["cargo","fmt"], cwd=rust_crate_dir)
    run(["cargo","clippy","--","-D","warnings"], cwd=rust_crate_dir)
    logger.info("Linter: fmt+clippy clean")
