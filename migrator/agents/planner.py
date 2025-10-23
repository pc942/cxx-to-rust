import json
from pathlib import Path
from pydantic import BaseModel
from ..logging_setup import logger
class Slice(BaseModel):
    name: str
    sources: list[Path]
def plan(manifest: Path, slice_name: str, out_path: Path) -> Slice:
    tus = json.loads(manifest.read_text())
    sl = Slice(name=slice_name, sources=[Path(t["source"]) for t in tus])
    out_path.write_text(sl.model_dump_json(indent=2))
    logger.info(f"Planner: {slice_name} with {len(sl.sources)} sources")
    return sl
