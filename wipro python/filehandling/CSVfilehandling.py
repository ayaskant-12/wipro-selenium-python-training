import csv

# reading the csv file
with open("C://Users//KIIT//Desktop//wipro python//Dataformats//data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# writing in the csv file
with open("C://Users//KIIT//Desktop//wipro python//Dataformats//write.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "marks"])
    writer.writerow([1,"Rahul", 85])
    writer.writerow([2,"Anita", 90])

with open("C://Users//KIIT//Desktop//wipro python//Dataformats//data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([103, "Kiran", "QA", 88])