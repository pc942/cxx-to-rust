import click
from pathlib import Path
from ..logging_setup import logger
from ..agents import repo_crawler, planner, translator, linter, builder, verifier, pr_bot

@click.group(name="migrate")
def app(): pass

@app.command()
@click.option("--repo", type=click.Path(path_type=Path), required=True)
@click.option("--slice", "slice_name", type=str, default="pilot")
def run(repo: Path, slice_name: str):
    ws = Path(".migrate"); ws.mkdir(exist_ok=True)
    manifest = ws / "manifest.json"
    repo_crawler.crawl(repo, manifest)
    sl = planner.plan(manifest, slice_name, ws / f"slice_{slice_name}.json")
    out = translator.translate(sl.sources, ws, slice_name)
    linter.lint(out)
    builder.build_and_test(Path("rust"))
    metrics = verifier.verify()
    if metrics["coverage_parity"] >= 0.95:
        pr_bot.open_pr(f"migrate/{slice_name}", f"Migrate: {slice_name}", f"metrics={metrics}")
    else:
        logger.warning("Below threshold; needs review.")
