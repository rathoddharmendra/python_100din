import requests
from datetime import datetime
import time
from geopy.distance import geodesic
from conn import Connection

# Berlin Latitude and Longitude
LAT = 52.520008
LNG = 13.404954

conn = Connection()

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if LAT - 5 <= iss_latitude <= LAT + 5 and LNG - 5 <= iss_longitude <= LNG + 5:
        return (True, iss_latitude, iss_longitude)
    return (False, iss_latitude, iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.


def is_dark():
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if current_hour() >= sunset or current_hour() < sunrise:
        return True
    return False    

def current_hour():
    return datetime.now().hour


while True:
    values = is_iss_overhead()
    if is_dark() and values[0]:
        conn.send_email(
            to_address='rathoddharmendra.business@gmail.com', 
            subject='Look Up 👆🏻', 
            body=f'ISS has been spotted in the sky {geodesic((LAT,LNG),(values[1], values[2]))} away')
        print(f'ISS is seen {geodesic((LAT,LNG),(values[1], values[2]))} away')
    else:
        print(f'ISS is very far, around {geodesic((LAT,LNG),(values[1], values[2]))} away')
    
    time.sleep(1800)

                

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



