import configparser


config = configparser.ConfigParser(
    inline_comment_prefixes="#",
)

print("Parsed files:", config.read("data/config.ini"))
print("Defaults:", config.defaults())
print("Sections:", config.sections())
print()

# Printing whole data with distinction between defaults and section.
print(config.default_section)
for option, value in config.defaults().items():
    print("|---{}: {}".format(option, value))
for section in config.sections():
    print(section)
    for option in filter(lambda x: x not in config.defaults(), config.options(section)):
        print("|---{}: {}".format(option, config.get(section, option)))
print()

# Printing whole data where sections' options contain default options.
for section in config.sections():
    print(section)
    for option in config.options(section):
        print("|---{}: {}".format(option, config.get(section, option)))
print()

# Two ways of getting options' values.
print("Host:", config["mariadb"]["host"])
print("Host:", config.get("mariadb", "host"))

print("Port:", int(config["redis"]["port"]))
print("Port:", config.getint("redis", "port"))  # Getting int type option.
