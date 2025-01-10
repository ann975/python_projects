import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 38.830391 # Your latitude
MY_LONG = -77.196373 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT -5 <= iss_latitude <= MY_LAT +5 or MY_LONG -5 <= iss_longitude <= MY_LONG + 5


def is_night():
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
    return time_now.hour >= sunset or time_now.hour <= sunrise

while True:
    time.sleep(60) #runs code every minute
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com",port=587 ) as connection:
            connection.starttls()
            connection.login("anc52153@gmail.com","fvqwfkrycjkywfut")
            connection.sendmail(
                from_addr="anc52153@gmail.com",
                to_addrs="anc52153@gmail.com",
                msg="Subject: ISS Overhead\n\nLook up now!"
            )




