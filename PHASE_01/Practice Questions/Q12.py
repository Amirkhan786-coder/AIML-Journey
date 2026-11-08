print("----File Handling----")

print("Opening a File")
file = open("data.txt", "r")

print("Writing a File")
file = open("data.txt", "w")

file.write("Hello Python")

file.close()

print("Reading a File")
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

print("The with Statement")
with open("data.txt", "a") as file:
    file.write("\nLearning Python")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

print("----Working with CSV Files----")

import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Amir", 20, 90])


print("Working with JSON")

import json

student = {
    "name": "Amir",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])