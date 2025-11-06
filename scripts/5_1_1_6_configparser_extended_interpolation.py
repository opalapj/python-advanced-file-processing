import configparser


config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read("data/config_extended_interpolation.ini")

# Printing whole data with distinction between defaults and section.
print(config.default_section)
for option, value in config.defaults().items():
    print("|---{}: {}".format(option, value))
for section in config.sections():
    print(section)
    for option in filter(lambda x: x not in config.defaults(), config.options(section)):
        print("|---{}: {}".format(option, config.get(section, option)))
