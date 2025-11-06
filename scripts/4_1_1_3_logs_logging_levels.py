import logging


# Root logger is created with level WARNING.
logger = logging.getLogger()


# Non-root logger is created with level NOTSET.
# logger = logging.getLogger(__name__)


# If the logger has a level of NOTSET, its chain of ancestor loggers
# is traversed until either an ancestor with a level other than NOTSET is found, or the root is reached.
# If the root is reached, and it has a level of NOTSET, then all messages will be processed.
# Otherwise, the root’s level will be used as the effective level.


# logger.setLevel(logging.NOTSET)
logger.setLevel(
    logging.DEBUG
)  # Check this setting for logger without any configuration. Even if the logger's level is set to DEBUG, LogRecord is forwarded to ‘handler of last resort’ with level of WARNING.

# If no logging configuration is provided, it is possible to have a situation
# where a logging event needs to be output, but no handlers can be found to output the event.

# The event is output using a ‘handler of last resort’, stored in lastResort.
# This internal handler is not associated with any logger, and acts like a StreamHandler
# which writes the event description message to the current value of sys.stderr
# (therefore respecting any redirections which may be in effect).
# No formatting is done on the message - just the bare event description message is printed.
# The handler’s level is set to WARNING, so all events at this and greater severities will be output.


print(f"{logger.level = }")
print(f"{logger.getEffectiveLevel() = }")

# All possible levels of logging.
logger.critical("Your CRITICAL message")
logger.error("Your ERROR message")
logger.warning("Your WARNING message")
logger.info("Your INFO message")
logger.debug("Your DEBUG message")
