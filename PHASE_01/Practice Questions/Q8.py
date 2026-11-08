print("----Sets----")


print("1.----Creating a Set----")
my_set = {1, 2, 3, 4, 5}    
print("Set:", my_set)

print("2.----Accessing Elements----")
# Sets are unordered collections, so we cannot access elements by index.
# We can iterate through the set to access its elements.
for element in my_set:
    print("Element:", element)

print("3.----Adding Elements----")
my_set.add(6)
print("Set after adding an element:", my_set)
my_set.update([7, 8, 9])
print("Set after adding multiple elements:", my_set)

print("4.----Removing Elements----")
my_set.remove(3)
print("Set after removing an element:", my_set)
my_set.discard(10)  # Discarding an element that doesn't exist won't raise an error
print("Set after discarding an element:", my_set)

print("5.----Set Operations----")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)
print("Is Set A a subset of Set B?", set_a <= set_b)
print("Is Set A a superset of Set B?", set_a >= set_b)
print("Are Set A and Set B disjoint?", set_a.isdisjoint(set_b))


print("6.----Set Methods----")
my_set = {1, 2, 3, 4, 5}
print("Length of set:", len(my_set))
print("Is 3 in the set?", 3 in my_set)
print("Is 6 not in the set?", 6 not in my_set)
print("Copy of the set:", my_set.copy())
print("Clearing the set...")
my_set.clear()
print("Set after clearing:", my_set)
print("Deleting the set...")
del my_set  
print("Set deleted.")