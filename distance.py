from my_location import *
from time import time, sleep
from os import system, name


def main():
    print("distance.py")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Iss_Distance:

    def __init__(self):
        self.done = None
        self.lat = 0
        self.long = 0

    def iss_location(self):
        """Returns Current Location of ISS Satellite"""
        url = "http://api.open-notify.org/iss-now.json#"
        response = requests.get(url=url)

        response.raise_for_status()

        data = response.json()

        longitude = data["iss_position"]["longitude"]
        latitude = data["iss_position"]["latitude"]

        iss_position = longitude, latitude
        self.long = float(longitude)
        self.lat = float(latitude)

        return iss_position

    def is_it_close(self):
        """Will see if ISS is +- 5 from My Location, Will run every 60 seconds"""
        is_it_close = True
        start_time = time()
        while is_it_close:
            if MY_LAT - 5 <= self.lat <= MY_LAT + 5 \
                    and MY_LONG - 5 <= self.long <= MY_LONG + 5:
                # Check to see if its nighttime
                if my_time() >= my_sunrise_sunset():
                    print("its close by")
                    return True

            else:
                print("Its not close by. \n")
            self.animation()
            sleep(10.0 - ((time() - start_time) % 10.0))

    def animation(self):
        self.done = True
        while self.done:
            sleep(2)
            print("Fetching in another 10 seconds")
            for x in range(1):
                print("Loading   ", end="")
                sleep(2)  # do some work here...
                print("\rLoading.  ", end="")
                sleep(2)  # do some more work here...
                print("\rLoading.. ", end="")
                sleep(2)  # do even more work...
                print("\rLoading...", end="")
                sleep(2)  # gratuitious amounts of work...
                print("\rLoading   ", end="")
                sleep(1)
            self.done = False
            clear()


if __name__ == "__main__":
    main()
