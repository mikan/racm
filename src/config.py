# -*- coding: utf-8 -*-

import yaml

CONFIG_FILE_PATH = "racm.yaml"
DEFAULT_CONFIG = {
    "port.default": 5555,
    "adb.path": "",
    "custom1.enable": 2,
    "custom2.enable": 2,
    "custom3.enable": 2,
    "custom1.label": "Custom 1",
    "custom2.label": "Custom 2",
    "custom3.label": "Custom 3",
    "custom1.command": "",
    "custom2.command": "",
    "custom3.command": "",
    "hosts": []
}


class RacmConfig(object):
    dict = None

    def __init__(self):
        try:
            with open(CONFIG_FILE_PATH) as f:
                self.dict = yaml.load(f)
        except IOError as (no, error):
            try:
                with open(CONFIG_FILE_PATH, "w") as f:
                    f.write(yaml.dump(DEFAULT_CONFIG))
                with open(CONFIG_FILE_PATH) as f:
                    self.dict = yaml.safe_load(f)
            except IOError as (no, error):
                print("Can't write config file: " + CONFIG_FILE_PATH)

    @staticmethod
    def get_config_path():
        return CONFIG_FILE_PATH

    def get(self, key):
        try:
            value = self.dict[key]
            return "" if value is None else value
        except KeyError, e:
            return ""

    def get_or_default(self, key, default):
        value = self.get(key)
        return default if not value else value

    def get_enable(self, key):
        return self.get(key) == 1

    def get_3s(self, key):
        value = self.get(key)
        if value == 1:
            return 1
        elif value == 2:
            return 0
        else:
            return -1

    def set(self, key, value):
        self.dict[key] = "" if value is None else value

    def set_3s(self, key, value):
        self.dict[key] = 1 if value else 2

    def add_item(self, host, name):
        self.dict["hosts"].append({"host": host, "name": name})

    def edit_item(self, host, name, row):
        self.dict["hosts"][row] = ({"host": host, "name": name})

    def write(self):
        try:
            with open(CONFIG_FILE_PATH, "w") as f:
                f.write(yaml.dump(self.dict))
            with open(CONFIG_FILE_PATH) as f:
                self.dict = yaml.load(f)
            return True
        except IOError as (no, error):
            print("Can't write config file: " + CONFIG_FILE_PATH)
            return False
