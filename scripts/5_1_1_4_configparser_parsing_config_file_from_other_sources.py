import configparser


config = configparser.ConfigParser(
    inline_comment_prefixes="#",
)

dict_ = {
    "DEFAULT": {"host": "localhost"},
    "mariadb": {"name": "hello", "user": "root", "password": "password"},
    "redis": {"port": 6379, "db": 0},
}

# 1st method.
# Load configuration from any object that provides a dict-like items() method.
# config.read_dict(dict_)

# 2nd method.
# Read and parse configuration data from f which must be an iterable yielding
# Unicode strings (for example files opened in text mode).
# with open('data/config.ini') as stream:
#     config.read_file(stream)

# 3rd method.
# Parse configuration data from a string.
with open("data/config.ini") as stream:
    content = stream.read()
    config.read_string(content)


# Printing whole data with distinction between defaults and section.
print(config.default_section)
for option, value in config.defaults().items():
    print("|---{}: {}".format(option, value))
for section in config.sections():
    print(section)
    for option in filter(lambda x: x not in config.defaults(), config.options(section)):
        print("|---{}: {}".format(option, config.get(section, option)))
