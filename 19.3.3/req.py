import requests

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept' : 'application/json'})

print(res.status_code)
print(res.text)

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "psina"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "psina"
    }
  ],
  "status": "available"
}

res = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)

print(res.status_code)
print(res.text)

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.put(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)

print(res.status_code)
print(res.text)

res = requests.delete(f'https://petstore.swagger.io/v2/pet/12')

print(res.status_code)
print(res.text)
