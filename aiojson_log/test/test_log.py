import os
from pathlib import Path

import pytest

from aiojson_log.log import get_logger


@pytest.mark.asyncio
async def test_async_json_file_log():
    log_file_path = Path("logs/test.json")
    if log_file_path.exists():
        os.remove(str(log_file_path))
    logger = await get_logger('test')
    await logger.debug("debug message")
    await logger.info("info message")
    await logger.warning("warning message")
    await logger.error("error message")
    await logger.critical("critical message")

    with open(str(log_file_path), "r") as f:
        logs = f.read().strip().split("\n")

    assert len(logs) == 5

    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    for record, level in zip(logs, levels):
        assert level in record
        assert '"message":' in record
        assert '"asctime":' in record
        assert '"process_id":' in record
        assert '"thread_id":' in record
