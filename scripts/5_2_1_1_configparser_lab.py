import configparser


class Mess:
    def __init__(self):
        self.prod = {}
        self.dev = {}

    def divide(self, file, tag):
        config = configparser.ConfigParser()
        config.read(file)
        for section in config.sections():
            if config.get(section, tag) == "prod":
                self.prod[section] = dict(
                    filter(lambda x: x[0] != tag, config[section].items())
                )
            elif config.get(section, tag) == "dev":
                self.dev[section] = dict(
                    filter(lambda x: x[0] != tag, config[section].items())
                )

    def write(self):
        for key, value in self.__dict__.items():
            config = configparser.ConfigParser()
            config.read_dict(value)
            filename = "data/" + key + "_config.ini"
            with open(filename, "w") as configfile:
                config.write(configfile)


mess = Mess()
mess.divide("data/mess.ini", "env")
mess.write()
