"""Module for requesting information from Strava API about athlets and activities"""
__author__ = 'Mykhailo Voitashevskyi'

import yaml

STRAVA_API_URL = "https://www.strava.com/api"
CONFIG_FILE = "strava_config.yml"

def read_config():
    with open(CONFIG_FILE, 'r') as stream:
        try:
            dict_config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
