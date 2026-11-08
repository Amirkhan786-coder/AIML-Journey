print("----Dictionaries----")

# Creating a dictionary
print("1.----Creating a Dictionary----")    
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)
print("Length of dictionary:", len(my_dict))

print("2.----Accessing Elements----")
# Accessing values using keys
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

print("3.----Modifying Elements----")
# Modifying values using keys
my_dict["name"] = "Bob"
my_dict["age"] = 35
print("Modified dictionary:", my_dict)

print("4.----Adding Elements----")
# Adding new key-value pairs
my_dict["country"] = "USA"
print("Dictionary after adding elements:", my_dict)

print("5.----Removing Elements----")
# Removing elements using keys
del my_dict["city"]
print("Dictionary after removing an element:", my_dict)

print("6.----Dictionary Methods----")
# Using dictionary methods
print("Keys:", my_dict.keys ())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

print("7.----Iterating through a Dictionary----")
# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("8.----Nested Dictionaries----")
# Creating a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 35}
}
print("Nested dictionary:", nested_dict)

print("Dictionary comprehension:")
# Creating a dictionary using comprehension
squared_dict = {x: x**2 for x in range(5)}
print("Squared dictionary:", squared_dict)

