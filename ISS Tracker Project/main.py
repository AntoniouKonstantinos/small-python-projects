import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv(".env")

MY_LAT = 40.618528 # My latitude
MY_LONG = 22.957889 # My longitude
MY_EMAIL = os.getenv("MY_EMAIL") # My Email
MY_PASSWORD = os.getenv("MY_PWD") #App password
TEST_EMAIL = os.getenv("TEST_EMAIL")

def is_iss_above_me():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    lat_diff = abs(MY_LAT - iss_latitude)
    lng_diff = abs(MY_LAT - iss_longitude)

    if lat_diff <= 5 and lng_diff <= 5:
        return True
    else:
        return False

def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    now_hour = time_now.hour

    if now_hour <= sunset or now_hour >= sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if is_iss_above_me() and is_nighttime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TEST_EMAIL,
                msg="Subject:LOOK UP\n\nHey look up the ISS is currently over your head"
            )



