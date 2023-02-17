import requests

r = requests.get("https://aworld01.github.io/aw01.io/")

# print(r.text) #to get html text
print(r.status_code) #to check status code