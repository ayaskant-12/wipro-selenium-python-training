import requests,json

try:

    response = requests.delete("https://videogamedb.uk:443/api/v2/videogame/1")
    print(response)
    if response.status_code == 200:
        print("Status code is 200 k")
        try:
            data = response.json()
            print("JSON Response:", data)
        except json.JSONDecodeError:
            print("Deleted successfully. No JSON body returned.")

    else:
        print(f"Error: Recieved status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")