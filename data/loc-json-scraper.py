import requests
import os
import json

coll = "photos"
term = "mrg"
limit = "1000"


def downloadData(coll, term, limit):
    url = r"https://www.loc.gov/{}/?q={}&fo=json&c={}".format(
        coll, term, limit)
    r = requests.get(url)
    print(type(r.content))
