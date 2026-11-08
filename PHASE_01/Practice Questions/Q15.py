print("----Advance Python----")


print("List, Dictionary and Set Comprehensions")

print("\nList Comprehension")
squares = [x**2 for x in range(1, 6)]
print(squares)


print("\nDictionary Comprehension")
squares = {x: x**2 for x in range(1, 6)}
print(squares)

print("\nSet Comprehension")
squares = {x**2 for x in range(1, 6)}
print(squares)


print("\nConditional comprehension:")
even = [x for x in range(20) if x % 2 == 0]
print(even)

print("\nNested comprehension:")
matrix = [[j for j in range(3)] for i in range(3)]

print(matrix)


print("\nIterators and Iterables")
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


print("\nGenerators")
#A generator is a special type of iterator that produces values lazily, one at a time.
#It uses yield instead of returning all results at once.
def numbers():

    yield 10
    yield 20
    yield 30

for num in numbers():
    print(num)

print("\nGenerator with a loop")
def count(n):

    for i in range(1, n + 1):
        yield i

for value in count(5):
    print(value)

print("\nGenerator Expression")
squares = (x**2 for x in range(1, 6))

for value in squares:
    print(value)

"""Why generators matter:
- Memory-efficient processing.
- Useful for large datasets.
- Useful for streaming data.
- Avoid creating huge lists in memory."""

print("\nDecorators")
#A decorator is a function that modifies or extends the behavior of another function without directly changing its original source code.
def decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper

@decorator
def greet():
    print("Hello Amir")

greet()

print("\nDecorator with arguments")
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Function started")

        result = func(*args, **kwargs)

        print("Function completed")

        return result

    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(10, 20))

print("functools.wraps ")
#Preserves important metadata of the decorated function.
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

"""Applications:
- Logging
- Authentication
- Timing functions
- Caching
- API route handling"""

print("\nLambda Functions — Advanced Usage")
students = [
    ("Amir", 90),
    ("Rahul", 80),
    ("Aman", 95)
]

students.sort(key=lambda x: x[1])

print(students)

print("\n*args and **kwargs — Advanced Understanding")
#*args collects extra positional arguments into a tuple.
def total(*args):
    return sum(args)

print(total(10, 20, 30, 40))

#**kwargs collects extra keyword arguments into a dictionary.
def profile(**kwargs):

    for key, value in kwargs.items():
        print(key, value)

profile(name="Amir", branch="AI/ML", year=2)

print("\nUnpacking:")
numbers = [10, 20]

def add(a, b):
    return a + b

print(add(*numbers))

data = {"name": "Amir", "age": 20}

def show(name, age):
    print(name, age)

show(**data)

print("\nScope and Closures")
#A closure is an inner function that remembers variables from its enclosing function even after the enclosing function has finished executing.
def outer(message):

    def inner():
        print(message)

    return inner

greet = outer("Hello Amir")

greet()

print("\nShallow Copy and Deep Copy")
#Shallow copy: Creates a new outer object but keeps references to nested objects.
#Deep copy: Recursively creates copies of nested objects.
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 100

print(shallow)
print(deep)

print("\nContext Managers")
#A context manager manages resources and ensures that setup and cleanup operations are handled appropriately.
"""with open("data.txt", "r") as file:
    data = file.read()"""

print("Creating Own COntext Manager")
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Starting")

    try:
        yield
    finally:
        print("Ending")

with my_context():
    print("Inside context")

print("\nRegular Expressions (RegEx)")
#Regular expressions are patterns used to search, match, and manipulate text.
#Python provides the re module.
import re

text = "My phone number is 9876543210"

result = re.findall(r"\d+", text)

print(result)

"""Important patterns:
Pattern	Meaning
\d	Digit
\D	Non-digit
\w	Word character
\s	Whitespace
.	Any character except newline by default
^	Start of string
$	End of string
+	One or more
*	Zero or more
{n}	Exactly n repetitions"""

print("\nBasic email pattern matching.")
import re

email = "amir@example.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid format")
else:
    print("Invalid format")

print("\nType Hints")
#Type hints are annotations that indicate the expected types of variables, parameters, and return values.
def add(a: int, b: int) -> int:
    return a + b

result: int = add(10, 20)
print(result)

def get_names() -> list[str]:
    return ["Amir", "Rahul"]


print("\nDataclasses")
#Dataclasses reduce repetitive code when creating classes primarily used to store data.
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: float

s = Student("Amir", 20, 90.5)

print(s)

print("\nCollections Module")
#The collections module provides specialized data structures.
from collections import Counter

data = ["Python", "Java", "Python", "C++"]

result = Counter(data)

print(result)

print("\ndefaultdict:")
from collections import defaultdict

data = defaultdict(list)

data["AI"].append("Python")
data["AI"].append("Machine Learning")

print(data)

print("\ndeque:")
from collections import deque

queue = deque([10, 20, 30])

queue.append(40)
queue.appendleft(5)

print(queue)

print("\nFunctional Programming")
"""Important concepts:
- Pure functions
- Higher-order functions
- Lambda functions
- map()
- filter()
- reduce()
- Immutability
- Function composition
A pure function returns a result based on its inputs without modifying external state or causing observable side effects."""
def square(number):
    return number * number

print(square(5))

print("\nMemory Management")
"""Important topics:
- Object references
- Reference counting
- Garbage collection
- Mutable vs immutable objects
- Shallow vs deep copying
- Memory-efficient generators"""

print("Python automatically manages most object memory.")
import gc

print(gc.isenabled())

print("\nMultithreading and Multiprocessing")
print("Multithreading:")
#Multiple threads run within one process and share its memory.
"""Useful for:
- API requests
- Network operations
- File operations
- I/O-bound tasks"""
import threading

def task():
    print("Task running")

t1 = threading.Thread(target=task)

t1.start()
t1.join()

print("\nMultiprocessing:")
#Multiple processes run independently, each with its own memory space.
"""Useful for:
- CPU-intensive tasks
- Parallel numerical computations
- Independent data processing"""
from multiprocessing import Process

def task():
    print("Process running")

if __name__ == "__main__":

    p = Process(target=task)

    p.start()
    p.join()

print("\nAsynchronous Programming — async/await")
#Used for concurrent I/O operations without blocking the event loop.
import asyncio

async def greet():
    print("Hello")

    await asyncio.sleep(1)

    print("Welcome")

asyncio.run(greet())


print("\nDebugging and Logging")

print("Debugging:")
#Finding and fixing errors in code.
"""Useful tools:
- VS Code debugger
- Breakpoints
- Step over
- Step into
- Variable inspection
- Python pdb"""

print("\nLogging:")
#Recording program events and errors.
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")
logging.info("Application started")
logging.warning("Warning message")
logging.error("An error occurred")
logging.critical("Critical error")

print("\nUnit Testing")
#Unit testing is the process of testing individual components or functions to verify that they behave as expected.
#Python provides unittest.
import unittest

def add(a, b):
    return a + b

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

if __name__ == "__main__":
    unittest.main()