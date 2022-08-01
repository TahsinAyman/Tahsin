import requests

print(requests.get("http://localhost:8080/api/v1/student").json())
