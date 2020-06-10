import json
import logging


class ConfigLoader:
    """
    This class loads all configurations and stores them in a config_store
    """
    def __init__(self):
        with open("configurations/conf.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        with open("configurations/local_conf.json", "r", encoding="utf-8") as f:
            config_local = json.load(f)

        self.config_store = {**config, **config_local}

    def get(self, key):
        return self.config_store[key]

    def get_logging_level(self):
        if self.config_store['logging_level'] == "debug":
            return logging.DEBUG
        elif self.config_store['logging_level'] == "warn":
            return logging.WARNING
        else:
            return logging.INFO

