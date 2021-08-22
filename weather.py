import sys
import datetime
import time
import requests
import json
import os

today = datetime.date.today()
a = today.strftime("%Y-%m-%d")

key_api = (sys.argv[1])
date = (sys.argv[2]) if len(sys.argv) >= 3 else a

d1 = datetime.datetime.strptime(date, "%Y-%m-%d")
d2 = d1 + datetime.timedelta(days=1)
d1 = time.mktime(d1.timetuple())
d2 = time.mktime(d2.timetuple())

class WeatherForecast:

    def __init__(self, key_api):
        self.key_api = key_api
        self.weather = {}

    def weathershowing(self):
        a = json.load(open("plik.json"))
        b = a["list"]
        for i in b:
            self.weather[(i["dt"])] = i["weather"][0]["main"]
        for i, k in self.weather.items():
            if i > d1 and i < d2:
                if k == "Rain":
                    print("będzie padać")
                elif k == "Clear":
                    print("nie będzie padać")
                else:
                    print("nie wiem")