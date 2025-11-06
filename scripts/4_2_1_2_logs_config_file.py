import logging
import logging.config


logging.config.fileConfig(
    # fname='data/config_file_required_content_template.ini',
    # fname='data/config_file_minimum_file_handler.ini',
    # fname='data/config_file_null_handler.ini',
    fname="data/config_file_practical_example.ini",
)

logger = logging.getLogger(__name__)

logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
