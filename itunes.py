# Jason
"""java script object notation text based format a bunchof text formatted in a standard way"""
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()


response = requests.get(
    "https://itunes.apple.com/search?entity=musicTrack&limit=1-50&term=" + sys.argv[1]
)
print(json.dumps(response.json(), indent =2 ))

o = response.json()
for result in o ["results"]:
    print(result["trackName"])
