print("----lists----")

print("1.----Creating a List----")
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
print("Length of list:", len(my_list))
print("Type of list:", type(my_list))

print("----Accessing Elements----")
print("First element:", my_list[0])
print("Last element:", my_list[-1])

print("----indexing Lists----")
numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[-1])  # 40

print("----Slicing Lists----")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[1:4])   # ['banana', 'cherry', 'date']
print(fruits[:3])    # ['apple', 'banana', 'cherry']
print(fruits[2:5])   # ['cherry', 'date', 'elderberry']

print("----Modifying Lists----")
my_list[2] = 10
print("Modified list:", my_list)

print("----Adding Elements----")
my_list.append(6)
print("List after append:", my_list)
my_list.insert(2, 15)
print("List after insert:", my_list)
my_list.extend([7, 8, 9])
print("List after extend:", my_list)


print("----Removing Elements----")
my_list.remove(4)
print("List after remove:", my_list)
my_list.pop(2)
print("List after pop:", my_list)
my_list.clear()
print("List after clear:", my_list)
del my_list
print("List deleted.")

a = [4, 2, 8, 1, 2]

print(len(a))
print(a.count(2))
print(a.index(8))

a.sort()
print(a)

a.reverse()
print(a)

b = a.copy()


print("----List Comprehension----")
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared numbers:", squared_numbers)

print("with condition:", [x for x in range(1, 11) if x % 2 == 0])

print("----Nested Lists----")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print() 


print("----List copying----")
a = [1, 2, 3]

b = a.copy()       # Shallow copy
c = a              # Same object
print(a)
print(b)
print(c)
