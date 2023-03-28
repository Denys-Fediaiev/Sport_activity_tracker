import datetime
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import os
import requests

APP_ID = os.environ["APP_ID"]

API_KEY = os.environ["API_KEY"]

api_endpoint = "https://trackapi.nutritionix.com/"
exercise_endpoint = f"{api_endpoint}v2/natural/exercise"

query = input("tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

params = {
    "query": query,
    "gender": "male",
    "weight_kg": 82,
    "height_cm": 190,
    "age": 21
}
response = requests.post(url=exercise_endpoint, json=params, headers=headers)
exercising_data = response.json()

sheety_end = os.environ["SHEET_ENDPOINT"]

#basic = HTTPBasicAuth(os.environ["USERNAME"], os.environ["PASSWORD"])

for sheet in exercising_data['exercises']:
    sheety_params = {
        "workout":
            {
                "date": datetime.date.today().strftime("%d/%m/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "exercise": sheet["name"].title(),
                "duration": sheet["duration_min"],
                "calories": sheet["nf_calories"]
            }
    }

sheety_headers = {
    "Authorization": f"Basic {os.environ['TOKEN']}"
}
response1 = requests.post(url=sheety_end, json=sheety_params, headers=sheety_headers)
print(exercising_data)
# print(sheety_params["exercise"])
print(response1.text)
#
# print(response.text)
