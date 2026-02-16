import requests
from requests.auth import HTTPBasicAuth

try:
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame", auth=HTTPBasicAuth('username', 'password'), timeout=5)
    print(response)
    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        print(data)
    else:
        print(f"Error: Recieved status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")