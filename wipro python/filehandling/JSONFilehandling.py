# read, write, modify
import json
with open("C://Users//KIIT//Desktop//wipro python//Dataformats//employee.json", 'r') as file:
    data = json.load(file)
# read the json file - load method()
print(data)
print(data["name"])
with open("C://Users//KIIT//Desktop//wipro python//Dataformats//nestedjson.json", 'r') as file:
    data = json.load(file)
print(data)
email = data["user"]["profile"]["email"]
print(email)

# writing to json file - dump method()

data = {
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}

with open("C://Users//KIIT//Desktop//wipro python//Dataformats//writejson.json", 'w') as file:
    json.dump(data, file)

# modify the json file

# read the json file
# modify the data
# write it back to the file

with open("C://Users//KIIT//Desktop//wipro python//Dataformats//updatejson.json", 'r') as file:
    data = json.load(file)
data["experience"] = 6
with open("C://Users//KIIT//Desktop//wipro python//Dataformats//updatejson.json", 'w') as file:
    json.dump(data, file, indent=4)