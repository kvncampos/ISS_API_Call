from distance import Iss_Distance
from my_location import *

iss = Iss_Distance()

# Print to debug code and test current location
print(iss.iss_location())
print(my_sunrise_sunset())

iss.is_it_close()
