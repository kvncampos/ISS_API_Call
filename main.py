from distance import Iss_Distance
from my_location import *
# import smtpdlib

# MY_EMAIL = ?
# MY_PASSWORD = ?
iss = Iss_Distance()

# Print to debug code and test current location
# print(iss.iss_location())
# print(my_sunrise_sunset())

iss.is_it_close()

# if iss.is_it_close():
#     connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()
#     connection.login(MY_EMAIL, MY_PASSWORD)
#     Connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs=MY_EMAIL,
#         msg="Subject: Look up! The ISS is above you."
    )