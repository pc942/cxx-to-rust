from pathlib import Path
import json
from ..logging_setup import logger
def crawl(repo: Path, out_manifest: Path) -> None:
    tus = []
    cc = list(repo.rglob("compile_commands.json"))
    if cc:
        data = json.loads(cc[0].read_text())
        for e in data:
            if str(e.get("file","")).endswith((".cpp",".cc",".cxx")):
                tus.append({"source": e["file"], "headers": [], "defines": [], "flags": e.get("command","").split()})
    else:
        for p in repo.rglob("*.cpp"):
            tus.append({"source": str(p), "headers": [], "defines": [], "flags": []})
    out_manifest.parent.mkdir(parents=True, exist_ok=True)
    out_manifest.write_text(json.dumps(tus, indent=2))
    logger.info(f"RepoCrawler: {len(tus)} TUs -> {out_manifest}")
