from pathlib import Path
from .util import run
def c2rust_translate(srcs: list[Path], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for s in srcs:
        run(["c2rust","transpile",str(s),"--output-dir",str(out_dir)])
