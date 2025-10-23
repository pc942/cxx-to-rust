import subprocess
from pathlib import Path
def run(cmd: list[str], cwd: Path | None = None) -> str:
    p = subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
    return p.stdout
