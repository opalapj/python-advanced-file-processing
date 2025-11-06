import logging
import time


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

handler = logging.FileHandler(
    filename="data/handler_and_formatter_log.log",
    mode="w",
    encoding="utf-8",
)
# handler.setLevel('DEBUG')  # For specify additional level of 'filtering'.

formatter = logging.Formatter(
    fmt="{levelname:10} | {asctime} | {name:8} | {message}",
    datefmt="%A, %d. %B %Y %I:%M%p %z",
    style="{",
)

# formatter.converter = time.gmtime

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
