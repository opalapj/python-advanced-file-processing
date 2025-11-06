import logging
import logging.config
import tomllib


with open(r"data/config.toml", mode="rb") as config_file:
    config = tomllib.load(config_file)

logging.config.dictConfig(config=config)

logger = logging.getLogger(__name__)

logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
