import requests
import json

uri = "https://httpbin.org/get"
r = requests.get(uri)
print(r.status_code)
print(r.json())
r_json = r.json()
# res.json() converts the response into json format. now you can extract data from it
print("r_json['headers']['Host']: ", r_json["headers"]["Host"])
#out r_json['headers']['Host']:  httpbin.org

print("r.json() type: ", type(r.json()))    #dict
json_dump =json.dumps(r.json(), indent=4)       ##dumps converts to string.

print("type(json_dump): ", type(json_dump))     ##str
print(json_dump)


# once you get the response, load it using json loads method
# to extract values or to iterate through it

json_load = json.loads(r.text)      ##or
# json_load = json.loads(json_dump)
print('json_load["headers"]["Host"]: ', json_load["headers"]["Host"])