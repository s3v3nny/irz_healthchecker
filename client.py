import requests

response = requests.get('http://sloth-2.suslovd.ru:8080')
print(type(response.text))
