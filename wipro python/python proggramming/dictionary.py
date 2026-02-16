country = {
    "India" : "Delhi",
    "Canada" : "Ottawa",
    "England" : "London"
}
print(country)

# access the values with the keys
print(country["Canada"])

# add elements
country["Italy"] = "Rome"
print(country)

# remove elements
del country["India"]
print(country)

# clear
# country.clear()
# print(country)

# iterate among the dict
for coun in country:
    print(coun)

# length of the dict
print(len(country))

# for integers as a key
my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict)

my_dict = {1: "four", 2: "two", 3: "three", 1: "one"}
print(my_dict)

# tuples as a key
my_dict = {
    (1,2) : "one two",
    3 : "three"
}
print(my_dict)

my_dict = {
    (1,2) : "one two",
    3: "three",
    3: "four"
}
print(my_dict)

# list as key
# my_dict = {1: "Hello", [1,2]: "There you"}
# print(my_dict)

country.pop("Italy")
print(country)
country.popitem()
print(country)
print(country.keys())
print(country.values())
country2 = country.copy()
print(country2)
country.update({"India" : "Delhi"})

# dictionary inside the list
employees = [
    {"id" : 1, "name":"Harsha", "role":"QA"},
    {"id" : 2, "name":"Anil", "role":"Dev"},
    {"id" : 3, "name":"Ravi", "role":"Manager"}
]
print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"], emp["role"])

employees.append({"id" : 4, "name":"Sita", "role":"Tester"})
print(employees)

employees.pop(0)
print(employees)

for emp in employees:
    if emp["name"] == "Harsha":
        print(emp)
