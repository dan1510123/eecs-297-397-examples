import requests

response = requests.get("http://localhost:5000/display")

print(response.text)


json_response = requests.put("http://localhost:5000/user/Casey?age=27&job=bartender")
print(json_response.json())
