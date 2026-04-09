import requests
url =" http://127.0.0.1:5000/data"

data={
    "name":"XYZ",
    "age": 25
}

response = requests.post(url,json=data)

print(response.json())