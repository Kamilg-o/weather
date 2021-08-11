import sys
import datetime
import time
import requests
import json
import os

today = datetime.date.today()
a = today.strftime("%d-%m-%Y")

api_key = (sys.argv[1])
date = (sys.argv[2]) if len(sys.argv) >= 3 else a
list = {}

d1 = datetime.datetime.strptime(date, "%d-%m-%Y")
d2 = d1 + datetime.timedelta(days=1)
d1 = time.mktime(d1.timetuple())
d2 = time.mktime(d2.timetuple())

with open("plik.json","a") as f:
    f.write("")

if os.stat("plik.json").st_size == 0:
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q": "Warsaw,pl", "lat": "35", "lon": "139", "cnt": "16", "units": "metric or imperial",
                   "lang": "pl"}

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print("polaczylem sie z api")

    with open("plik.json", "a", newline='') as file:
        file.write(json.dumps(response.json()))

    a = json.load(open("plik.json"))
    b = a["list"]
    for i in b:
        list[(i["dt"])] = i["weather"][0]["description"]
    for i, k in list.items():
        if i > d1 and i < d2:
            if k == "słabe opady deszczu":
                print("będzie padać")
            elif k == "bezchmurnie":
                print("nie będzie padać")
            else:
                print("nie wiem")
else:
    a = json.load(open("plik.json"))
    b = a["list"]
    for i in b:
        list[(i["dt"])] = i["weather"][0]["description"]
    for i, k in list.items():
        if i > d1 and i < d2:
            if k == "słabe opady deszczu":
                print("będzie padać")
            elif k == "bezchmurnie":
                print("nie będzie padać")
            else:
                print("nie wiem")


