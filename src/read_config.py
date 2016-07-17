import json
import os
from pprint import pprint


def read_config(config_file):
    with open(config_file) as config_file:
        config = json.load(config_file)
        return config


if __name__ == '__main__':
    api_file = os.path.dirname(os.path.realpath(__file__)) + "/json/api_config.json"
    config = read_config(api_file)
    pprint(config)