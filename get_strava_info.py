"""Module for requesting information from Strava API about athlets and activities"""
__author__ = 'Mykhailo Voitashevskyi'

import yaml
from stravalib.client import Client

STRAVA_API_URL = "https://www.strava.com/api"
CONFIG_FILE = "strava_config.yml"


def read_config():
    """Read Strava API config from CONFIG_FILE"""
    with open(CONFIG_FILE, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def get_last_activity_info():
    """Get information about last activity from STRAVA_API_URL"""
    client = Client()
    client.access_token = ACCESS_TOKEN
    athlete = client.get_athlete()

    activities = client.get_activities(limit=1)
    result = {}

    for activity in activities:
        result['activity_name'] = activity.name
        result['activity_url']  = "https://www.strava.com/activities/{id}".format(id=activity.id)
        result['flybys_url']    = "http://labs.strava.com/flyby/viewer/#{id}".format(id=activity.id)
    return result

CONFIG = read_config()
ACCESS_TOKEN = CONFIG['access_token']
