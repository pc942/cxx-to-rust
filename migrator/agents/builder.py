from pathlib import Path
from ..utils/shell import run
from ..logging_setup import logger
def build_and_test(rust_workspace: Path) -> None:
    run(["cargo","build"], cwd=rust_workspace)
    run(["cargo","test"], cwd=rust_workspace)
    logger.info("Builder: build+test ok")
