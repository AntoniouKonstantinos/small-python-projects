import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv(".env")

USER = os.getenv("USER")
TOKEN = os.getenv("TOKEN")

endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{endpoint}/{USER}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{endpoint}/{USER}/graphs/{graph_config['id']}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m&d"),
    "quantity": input("How many hours did you code today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)