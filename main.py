import requests
import os
from smtplib import SMTP
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL")  
APP_PASSWORD = os.environ.get("APP_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")
MY_LAT = 17.09281440497354
MY_LONG = 82.06943564250437

weather_params = {
    'lat': 17.09281440497354,
    'lon': 82.06943564250437,
    'appid':OPENWEATHER_API_KEY,
    'cnt':4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?",params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_ids = []
will_rain = False

for hour_data in range(0,len(weather_data["list"])):
    weather_ids.append(weather_data['list'][hour_data]['weather'][0]['id'])

    if weather_ids[hour_data] < 700:
        will_rain = True

if will_rain:
      print(weather_ids)
      with SMTP("smtp.gmail.com",port=587) as connection:
              connection.starttls()
              # tls : transport layer security : securing our connection to the email server
              connection.login(user=MY_EMAIL, password=APP_PASSWORD)
              
              connection.sendmail(
                      from_addr=MY_EMAIL,
                      to_addrs=TO_EMAIL,
                      msg=f"Subject: Rain Alert\n\nIt's going to rain today, Bring Umbrella"
        )
