import requests

r = requests.get("https://google.com")
print(r.status_code)

try:
    br = requests.get("https://googlis3432.com")
    print(br.status_code)
except requests.exceptions.ConnectionError:
    print("Recieved a connection Error")