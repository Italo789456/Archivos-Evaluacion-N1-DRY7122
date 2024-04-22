import json
with open("rconf.json", "r") as file:
    ourjson = json.load(file)
print(ourjson)
