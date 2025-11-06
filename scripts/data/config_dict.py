required_content_template = {"version": 1}

minimum_file_handler = {
    "version": 1,
    "loggers": {"__main__": {"handlers": ["main"]}},
    "handlers": {
        "main": {
            "class": "logging.FileHandler",
            "filename": "data/config_dict_minimum_file_handler.log",
        }
    },
}

null_handler = {
    "version": 1,
    "loggers": {"__main__": {"handlers": ["main"]}},
    "handlers": {
        "main": {
            "class": "logging.NullHandler",
        }
    },
}

practical_example = {
    "version": 1,
    "loggers": {"__main__": {"handlers": ["file", "console"]}},
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "level": "CRITICAL",
            "filename": "data/config_dict_practical_example.log",
            "mode": "w",
            "encoding": "utf-8",
            "formatter": "common",
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "common",
        },
    },
    "formatters": {
        "common": {
            "format": "{levelname:10} | {asctime} | {name:8} | {message}",
            "datefmt": "%A, %d. %B %Y %I:%M%p %z",
            "style": "{",
        }
    },
}
