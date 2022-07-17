import requests
from datetime import datetime

MY_LAT = 32.776665
MY_LONG = -96.796989


def my_time():
    """Returns Current Hour 24 Format"""
    time_now = datetime.now()
    return time_now.hour


def my_sunrise_sunset():
    """API CAll to get Sunset/Sunrise, Returns Sunset of My Location"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    jdata = response.json()
    sunrise = jdata["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = jdata["results"]["sunset"].split("T")[1].split(":")[0]

    return sunset
