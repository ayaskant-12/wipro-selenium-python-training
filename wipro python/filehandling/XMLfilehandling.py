import xml.etree.ElementTree as ET
from xml.etree.ElementTree import indent

# read xml file
# parsed XML file into a variable tree
tree = ET.parse("C://Users//KIIT//Desktop//wipro python//Dataformats//employee.xml")
root = tree.getroot()     # get the root element
print(root.tag)
# get the first child node / tag
print(root[0].tag)
# get the attributes of the child node
print(root[0].attrib)
# fetch all the attributes in the child node
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)
    emp_name = employee.get("name")
    print(emp_name)

for emp in root.findall("employee"):
    name = emp.find("name").text
    role = emp.find("role").text
    exp = emp.find("experience").text
    print(name, role, exp)
print("\n")
for emp in root.findall("employee"):
    for child in emp:
        print(child.text)
print("\n")
for emp in root.findall("employee"):
    if emp.get("id") == "101":
        for child in emp:
            print(child.text)
print("\n\n")

# write the data into xml

# create the child nodes
# tree = ET.parse("C://Users//KIIT//Desktop//wipro python//Dataformats//writexml.xml")
# create the root element
root = ET.Element("employees")
# create the child elements
emp1 = ET.SubElement(root, "employee", id = "101")
ET.SubElement(emp1, "name").text = "Harsha"
ET.SubElement(emp1, "role").text = "Tester"
ET.SubElement(emp1, "experience").text = "5"
# create the child elements 2
emp1 = ET.SubElement(root, "employee", id = "102")
ET.SubElement(emp1, "name").text = "Amit"
ET.SubElement(emp1, "role").text = "Developer"
ET.SubElement(emp1, "experience").text = "3"
# write to the file
tree = ET.ElementTree(root)
ET.indent(tree, space="    ")
tree.write(
    "C://Users//KIIT//Desktop//wipro python//Dataformats//writexml.xml",
    encoding="utf-8",
    xml_declaration=True
)

# update
tree = ET.parse("C://Users//KIIT//Desktop//wipro python//Dataformats//updatexml.xml")
root = tree.getroot()
for emp in root.findall("employee"):
    if emp.get("id") == "101":
        emp.find("experience").text = "16"
ET.indent(tree, space="    ")
tree.write(
    "C://Users//KIIT//Desktop//wipro python//Dataformats//updatexml.xml",
    encoding="utf-8",
    xml_declaration=True
)