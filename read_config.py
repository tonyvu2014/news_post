import json
import os
from pprint import pprint


def read_api_config():
    api_file = os.path.dirname(os.path.realpath(__file__)) + "/json/api_config.json"
    with open(api_file) as config_file:
        config = json.load(config_file)
        return config
        
def read_feed_config():
    feed_file = os.path.dirname(os.path.realpath(__file__)) + "/json/feed_config.json"
    with open(feed_file) as config_file:
        config = json.load(config_file)
        return config


if __name__ == '__main__':
    config = read_api_config()
    pprint(config)