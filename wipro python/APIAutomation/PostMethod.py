import requests

try:

    data = {
            "id": 0,
            "name": "Mario",
            "releaseDate": "2012-05-04",
            "reviewScore": 85,
            "category": "Platform",
            "rating": "Mature"
        }

    response = requests.post("https://videogamedb.uk:443/api/v2/videogame", json = data)
    print(response)
    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        print(data)
    else:
        print(f"Error: Recieved status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")