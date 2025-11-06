import logging


logger = logging.getLogger(__name__)

# Each logger can have several handlers added.
# One handler can save logs to a file, while another can send them to an external service.
file_handler = logging.FileHandler("data/handler_log.log", mode="w")
file_handler.setLevel("CRITICAL")
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel("DEBUG")
logger.addHandler(stream_handler)

# The level set in the logger determines which severity of messages
# it will pass to its handlers.
# logger.setLevel('DEBUG')
# logger.root.setLevel('DEBUG')


print(f"{logger.level = }")
print(f"{logger.getEffectiveLevel() = }")

logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
