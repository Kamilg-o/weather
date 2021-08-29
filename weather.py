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
            for s, k in self.weather.items():
                s = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d')
                if s == d1:
                    if k == "Rain":
                        print("będzie padać")
                    elif k == "Clear":
                        print("nie będzie padać")
                    else:
                        print("nie wiem")

    def check_from_api(self):
        with open("plik.json", "a") as f:
            f.write("")

            url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

            querystring = {"q": "Warsaw,pl", "lat": "35", "lon": "139", "cnt": "16", "units": "metric or imperial",
                           "lang": "pl"}

            headers = {
                'x-rapidapi-key': self.key_api,
                'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            print("polaczylem sie z api")

            with open("plik.json", "a", newline='') as file:
                file.write(json.dumps(response.json()))
            self.weathershowing()

    def check_from_file(self):
        self.weathershowing()

    def items(self):
        for i, k in self.weather.items():
            i = datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d')
            if k == 'Rain':
                 k = "będzie padać"
            elif k == "Clear":
                k ="nie będzie padać"
            else:
                k ="nie wiem"
            yield i,k


    def __getitem__(self, item):
        return self.weather[item]

    def __iter__(self):
        for i in self.weather.keys():
            i = datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d')
            yield i

wf = WeatherForecast(key_api)
if os.stat("plik.json").st_size == 0:
    wf.check_from_api()
else:
    wf.check_from_file()
print(wf['2021-09-03'])
