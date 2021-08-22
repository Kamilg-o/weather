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