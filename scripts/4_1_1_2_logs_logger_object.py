import logging


# logging.getLogger(name=None)
# Return a logger with the specified name or, if name is None, return a logger
# which is the root logger of the hierarchy. If specified, the name is typically
# a dot-separated hierarchical name like ‘a’, ‘a.b’ or ‘a.b.c.d’.
# Choice of these names is entirely up to the developer who is using logging.
root_logger = logging.getLogger()
hello_logger = logging.getLogger("hello")
hello_world_logger = logging.getLogger("hello.world")
recommended_logger = logging.getLogger(__name__)

print("Parent logger: {0.parent} of logger: {0}".format(root_logger))
print("Parent logger: {0.parent} of logger: {0}".format(hello_logger))
print("Parent logger: {0.parent} of logger: {0}".format(hello_world_logger))
print("Parent logger: {0.parent} of logger: {0}".format(recommended_logger))
