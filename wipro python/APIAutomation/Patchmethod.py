import requests

try:

    data = {
            "id": 7,
            "name": "Ayaskant"
        }

    response = requests.patch("https://videogamedb.uk:443/api/v2/videogame/7", json=data)
    print(response)
    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        print(data)
    else:
        print(f"Error: Recieved status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")