import json

json_str = (
    '{"name": "Arjun", "age": 22, "location": {"city": "Mumbai", "country": "India"}}'
)

data = json.loads(json_str)

print(data["location"]["city"])

data_str = json.dumps(data)

print(data_str)

with open("person.json", "r") as file:
    person_json = json.load(file)

print(person_json)


person_json["1"]["location"] = {"city": "Japlaiguri", "country": "India"}


person_json["3"] = {
    "name": "Ayush",
    "age": 23,
    "location": {"city": "Noida", "country": "India"},
}


with open("person.json", "w") as file:
    json.dump(person_json, file)
