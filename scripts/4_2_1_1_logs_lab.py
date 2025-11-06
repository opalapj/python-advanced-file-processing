import logging
import random
import time


class Phone:

    def __init__(self, producer, number, owner):
        self.producer = producer
        self.number = number
        self.owner = owner
        self.mode = None
        self.file_name = None
        self.logger = None
        print("Phone configured!")

    def logs_configuration(self, mode="file", file_name="data/temperature.log"):
        self.mode = mode
        self.file_name = file_name
        logger = logging.getLogger(self.producer)
        if mode == "file":
            handler = logging.FileHandler(file_name, mode="w", encoding="utf-8")
        else:
            handler = logging.StreamHandler()
        format_ = "%(levelname)s - %(message)s"
        formatter = logging.Formatter(format_)
        handler.setFormatter(formatter)
        # handler.setLevel('DEBUG')
        logger.setLevel("DEBUG")
        logger.addHandler(handler)
        self.logger = logger

    def temperature_measurement(self, duration=60):
        self.logger.info("{} {} {}".format(self.producer, self.owner, self.number))
        msg = "{0} C".format
        for m in range(duration):
            temp = random.randint(20, 40)
            if temp < 30:
                self.logger.debug(msg(temp))
            elif 30 <= temp <= 35:
                self.logger.warning(msg(temp))
            elif temp > 35:
                self.logger.critical(msg(temp))
            time.sleep(0.5)


my_phone = Phone("Samsung", "698-172-294", "Piotr Opała")
# my_phone.logs_configuration('stream')
my_phone.logs_configuration("file")
my_phone.temperature_measurement(10)
