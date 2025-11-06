import logging
import logging.config

import data.config_dict as config_dict


logging.config.dictConfig(
    # config=config_dict.required_content_template,
    # config=config_dict.minimum_file_handler,
    # config=config_dict.null_handler,
    config=config_dict.practical_example,
)

logger = logging.getLogger(__name__)

logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
