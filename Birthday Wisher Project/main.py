import pandas
import smtplib
import datetime as dt
from random import randint
import os
from dotenv import load_dotenv

load_dotenv(".env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PWD")

now = dt.datetime.now()
current_date = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays = data.set_index(['month', 'day']).to_dict(orient="index")

if current_date in birthdays:
    random_letter = f"letter_templates/letter_{randint(1, 3)}.txt"

    with open(random_letter) as letter:
        text = letter.read()
        message = text.replace("[NAME]", birthdays[current_date]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays[current_date]["email"],
            msg=f"Subject:Happy Birthday\n\n{message}"
        )




