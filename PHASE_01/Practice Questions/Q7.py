print("----Tuples----")

print("1.----Creating a Tuple----")
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Length of tuple:", len(my_tuple))
print("Type of tuple:", type(my_tuple))

print("2.----Accessing Elements----")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

print("3.----indexing Tuples----")
numbers = (10, 20, 30, 40)
print(numbers[0])   # 10
print(numbers[-1])  # 40    

print("4.----Slicing Tuples----")
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(fruits[1:4])   # ('banana', 'cherry', 'date')
print(fruits[:3])    # ('apple', 'banana', 'cherry')
print(fruits[2:5])   # ('cherry', 'date', 'elderberry')


print("5.----Modifying Tuples----")
# Tuples are immutable, so we cannot modify them directly.
# However, we can create a new tuple by concatenating existing tuples.
new_tuple = my_tuple + (6, 7, 8)
print("New tuple after concatenation:", new_tuple)


print("6.----Tuple Methods----")
my_tuple = (1, 2, 3, 4, 5, 2, 3)
print("Count of 2 in tuple:", my_tuple.count(2))
print("Index of 3 in tuple:", my_tuple.index(3))


print("7.----packing and Unpacking Tuples----")
# Packing
my_tuple = (1, 2, 3)
print("Packed tuple:", my_tuple)

# Unpacking
a, b, c = my_tuple
print("Unpacked values:", a, b, c)

print("8.----Nested Tuples----")
nested_tuple = (1, 2, (3, 4), 5)
print("Nested tuple:", nested_tuple)
print("Accessing nested tuple element:", nested_tuple[2][1])  # Accessing
