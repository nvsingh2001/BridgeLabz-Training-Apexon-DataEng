import json

json_str = (
    '{"name": "Arjun", "age": 22, "location": {"city": "Mumbai", "country": "India"}}'
)

data = json.loads(json_str)

print(data["location"]["city"])
