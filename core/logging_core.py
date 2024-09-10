import logging
from config import ConfigSettings


def Initialize():
    log = logging.getLogger("werkzeug")
    log.disabled = True
    logHandler = logging.StreamHandler()

    level = logging.INFO
    if ConfigSettings.LOG_LEVEL == "debug":
        level = logging.DEBUG
    logging.basicConfig(
        level=level,
        format="[%(asctime)s]: %(process)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
