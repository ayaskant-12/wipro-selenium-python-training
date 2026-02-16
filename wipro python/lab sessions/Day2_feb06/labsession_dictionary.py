# Create a dictionary with student roll number as key and name as value. Print the dictionary.
student = {
    101: "ayaskant",
    102: "Rohit",
    103: "Ayesha"
}
print(student)
# Access the value of a key that exists and one that does not exist
print("roll no 101", student.get(101))
print("roll no 104", student.get(104))
# Update the value of an existing key in a dictionary.
student.update({102: "Amit"})
print(student)
# Delete a key from a dictionary using:
#   del
#   pop()
del student[102]
print(student)
student.pop(103)
print(student)
# Find the number of key–value pairs in a dictionary.
print(len(student))
# Print only:
#   keys
#   values
#   key–value pairs
print(student.keys())
print(student.values())
print(student.items())