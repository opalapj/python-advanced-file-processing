import logging


# logging.basicConfig()
# Responsible for the basic logging configuration.
# Does basic configuration for the logging system by creating a StreamHandler
# with a default Formatter and adding it to the root logger.
# The default format set by basicConfig() for messages is:
# '%(levelname)s:%(name)s:%(message)s'

logging.basicConfig(
    filename="data/basic_config_log.log",
    filemode="w",
    format="{levelname:10} | {asctime} | {name:8} | {message}",
    datefmt="%A, %d. %B %Y %I:%M%p %z",
    style="{",
    level=logging.DEBUG,
    encoding="utf-8",
)

logger = logging.getLogger(__name__)

logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
