import http.client
import json
import os

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

key = os.getenv("RAPIDAPI_KEY")

headers = {
    "x-rapidapi-key": key,
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
}

conn.request("GET", "/v3/leagues?name=Premier+League&code=GB-ENG", headers=headers)

res = conn.getresponse()
data = res.read()

data = json.loads(data.decode("utf-8"))

leagues = data["response"]

if len(leagues) > 1:
    raise Exception("More than one league in response")

league = leagues[0]
league_id = league["league"]["id"]  # 39 - to be used in other API calls

print(league_id)
