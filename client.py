import requests
from requests import get

response = requests.get('http://localhost:8080')
print(response.text)
