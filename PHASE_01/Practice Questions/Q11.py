print("----modules----")

print("1.----importing a module----")
import math
print("Square root of 16:", math.sqrt(16))

print("2.----importing specific functions from a module----")
from math import pow
print("2 raised to the power of 3:", pow(2, 3))

print("3.----importing a module with an alias----")
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print("Numpy array:", array)

print("4.----importing all functions from a module----")
from math import *
print("Sine of 0:", sin(0))
print("Cosine of 0:", cos(0))
print("Tangent of 0:", tan(0))
print("Logarithm of 1:", log(1))
print("Exponential of 1:", exp(1))
print("Factorial of 5:", factorial(5))
print("Greatest common divisor of 12 and 15:", gcd(12, 15))
print("Least common multiple of 12 and 15:", lcm(12, 15))
print("Pi:", pi)
print("Euler's number:", e)
print("Square root of 25:", sqrt(25))
print("Power of 2 raised to 3:", pow(2, 3))
print("Absolute value of -5:", fabs(-5))
print("Ceiling of 4.2:", ceil(4.2))
print("Floor of 4.8:", floor(4.8))
print("Degrees of pi radians:", degrees(pi))
print("Radians of 180 degrees:", radians(180))
print("Hyperbolic sine of 0:", sinh(0))
print("Hyperbolic cosine of 0:", cosh(0))
print("Hyperbolic tangent of 0:", tanh(0))

print("5.----importing a module from a package----")
import os
print("Current working directory:", os.getcwd())


print("different ways to import modules:")
print("1. import module")
print("2. from module import function")
print("3. import module as alias")
print("4. from module import *")
print("5. import module from package")

print("----creating a module----")
# Create a file named my_module.py with the following content:
# def greet(name):
#     return f"Hello, {name}!"
# Then, you can import and use it in another script:
# import my_module
# print(my_module.greet("Alice"))

print("----creating a package----")
# Create a directory named my_package and add an __init__.py file inside it.

print("----using a package----")
# You can create multiple modules inside the my_package directory and import them as follows:
# from my_package import module1
# from my_package import module2

print("----module search path----")
import sys
print("Module search path:", sys.path)

print("----reloading a module----")
# If you modify a module and want to reload it without restarting the interpreter, you can use
# import importlib
# importlib.reload(module_name)

print("----built-in modules----")
print("1.----math module----")
print("Square root of 16:", math.sqrt(16))
print("Power of 2 raised to 3:", math.pow(2, 3))
print("Sine of 0:", math.sin(0))
print("Cosine of 0:", math.cos(0))
print("Tangent of 0:", math.tan(0))

print("2.----random module----")
import random
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

print("3.----datetime module----")
import datetime
print("Current date and time:", datetime.datetime.now())

print("4.----os module----")
import os
print("Current working directory:", os.getcwd())

print("5.----sys module----")
import sys
print("Python version:", sys.version)
print("Python path:", sys.path)

print("----package---")

"""Definition: A package is a way of organizing related Python modules into a directory structure.

Example:
my_project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── calculator.py
    └── helper.py"""
#from utils.calculator import add


print("----pip---")
#pip install numpy
#pip list
# save dependencies: pip freeze > requirements.txt
#Install project dependencies:pip install -r requirements.txt

print("----Virtual Environment----")
"""A virtual environment keeps project dependencies separate.

Create:
python -m venv venv


Activate in Windows PowerShell:
.\venv\Scripts\Activate.ps1


Deactivate:
deactivate


name == "main"
def main():    print("Program started")if __name__ == "__main__":    main()



This ensures that the main code runs when the file is executed directly, rather than when it is imported as a module."""