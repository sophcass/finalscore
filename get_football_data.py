import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    "x-rapidapi-key": "XXXXXxxxxx",
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
}

conn.request("GET", "/v3/leagues", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
