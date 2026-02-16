# 1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.

import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print("Name:", user["name"])
            print("Email:", user["email"])

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# 2. Send a GET request with query parameter userId=2 and print number of posts returned.

import requests

try:
    params = {"userId": 2}

    response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
    print(response)
    response.raise_for_status()
    posts = response.json()
    print("Number of posts:", len(posts))

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# 3. Write a POST request to create a new resource and verify status code 201.

import requests

try:
    data = {
        "title": "New Post",
        "body": "This is a test post",
        "userId": 1
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)

    print(response)

    if response.status_code == 201:
        print("Resource created successfully!")
        print("Response:", response.json())
    else:
        print("Failed! Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# 4. Explain the difference between data= and json= in requests.post().

# data = sends form-encoded data, used for form submission, convert manually
# json = sends json body, used for rest apis, automatically converts dict to json

# 5. Write code to check if response status code is not 200 and raise an exception.

import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")

    print("Request successful!")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# 6. Fetch all users and print usernames in uppercase.

import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    users = response.json()
    for user in users:
        print(user["username"].upper())

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# 7. Implement timeout handling (2 seconds) and catch Timeout exception.

import requests
from requests.exceptions import Timeout
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=2)
    print("Status:", response.status_code)
except Timeout:
    print("Request timed out!")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# 8. Use Session object to send multiple requests and demonstrate cookie persistence.



# 9. Upload a file using requests and print server response.

import requests

try:
    files = {
        "file": open("sample.txt", "rb")
    }

    response = requests.post(
        "https://httpbin.org/post",files=files)
    print("Status:", response.status_code)
    print("Response:", response.json())

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# 10. Fetch posts and save response JSON into a file named posts.json.

import requests
import json
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",timeout=5)
    response.raise_for_status()
    posts = response.json()
    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)
    print("Posts saved successfully to posts.json")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)