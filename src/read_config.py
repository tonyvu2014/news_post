import json
from pprint import pprint


def read_config(config_file):
    with open(config_file) as config_file:
        config = json.load(config_file)
        return config


if __name__ == '__main__':
    config = read_config('json/api_config.json')
    pprint(config)