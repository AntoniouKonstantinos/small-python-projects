import os
from dotenv import load_dotenv
import requests
import smtplib

load_dotenv(".env")

EMAIL = os.getenv("MY_EMAIL")
PWD = os.getenv("MY_PWD")
TEST_ADDRESS = os.getenv("TEST_EMAIL")

api_key = os.getenv("API_KEY")
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters ={
    "lat": 40.6083711,
    "lon": 22.9532841,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

forecasts = data["list"]
will_rain = False

for forecast in forecasts:
    timestamp = int(forecast["weather"][0]["id"])
    if timestamp < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PWD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs= TEST_ADDRESS,
            msg="Subject:Weather Alert!\n\nIt will probably rain in the next 12 hours you better grab an Umbrella"
        )