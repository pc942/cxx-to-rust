from ..logging_setup import logger
def open_pr(branch: str, title: str, body: str) -> None:
    logger.info(f"PR: {branch} — {title}\n{body}")
