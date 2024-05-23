import requests

endpoints="http://127.0.0.1:8000/car/list"
getrespose=requests.get(endpoints)
# print(getrespose.json())
print(getrespose.status_code)