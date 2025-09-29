import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv(".env")

SHEETY_USERNAME = os.getenv("USERNAME")
SHEETY_PWD = os.getenv("PWD")
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.getenv("API_ID")
API_KEY = os.getenv("API_KEY")
SHEET_ENDPOINT = "https://api.sheety.co/639b456bf48161352aee785988093f86/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercise you did: ")

parameters = {
    "query": exercise_text,
}

response = requests.post(ENDPOINT, json=parameters, headers=headers)
data = response.json()
result = data["exercises"]

today = datetime.now()

for exercise in result:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response_sheet = requests.post(url=SHEET_ENDPOINT,
                               json=sheet_inputs,
                               auth=(
                                   SHEETY_USERNAME,
                                   SHEETY_PWD
                               )) #Basic Authentication
result_sheet = response_sheet.json()