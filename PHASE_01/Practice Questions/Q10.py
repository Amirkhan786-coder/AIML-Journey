print("----Function----")

print("1.----Defining a Function----")
def greet(name):
    return f"Hello, {name}!"    
greeting = greet("Amir")
print(greeting)


print("2.----Function with Default Arguments----")
def greet(name="Guest"):
    return f"Hello, {name}!"
greeting = greet()
print(greeting)

print("3.----Function with Variable-length Arguments----")
def greet(*names):
    return "Hello, " + ", ".join(names) + "!"
greeting = greet("Amir", "Ali", "Sara")
print(greeting)

print("4.----Function with Keyword Arguments----")
def greet(**kwargs):
    return "Hello, " + ", ".join(kwargs.values()) + "!"
greeting = greet(name1="Amir", name2="Ali", name3="Sara")
print(greeting)

print("5.----Function with Return Value----")
def add(a, b):
    return a + b
result = add(5, 3)
print("Result of addition:", result)

print("----Function with No Return Value----")
def greet(name):
    print(f"Hello, {name}!")
greet("Amir")


print("----Function with Multiple Return Values----")
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result

sum_val, diff_val = calculate(10, 5)
print("Sum:", sum_val)
print("Difference:", diff_val)

print("----Function with Nested Functions----")
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 5
result = outer_function(3)
print("Result of outer function:", result)


print("----Function with Lambda Function----")
square = lambda x: x ** 2
result = square(5)
print("Square of 5:", result)

print("----Function with Map, Filter, and Reduce----")
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Even numbers:", even_numbers)
print("Sum of numbers:", sum_of_numbers)

print("----scope of Variables----")
x = 10  # Global variable
def my_function():
    x = 5  # Local variable
    print("Inside function, x =", x)
    print("Global x =", globals()['x'])
my_function()
print("Outside function, x =", x)

print("----Function with Docstring----")
def greet(name):
    """This function greets the person with the given name."""
    return f"Hello, {name}!"
print(greet("Amir"))
print(greet.__doc__)

print("----Function with Annotations----")
def add(a: int, b: int) -> int:
    return a + b
result = add(5, 3)
print("Result of addition:", result)

print("----Function with Recursion----")
print("Factorial of a number using recursion:")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(25)
print("Factorial of 25:", result)


print("----Fibonacci Sequence----")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            next_number = fib_series[i - 1] + fib_series[i - 2]
            fib_series.append(next_number)
        return fib_series

fib_sequence = fibonacci(10)
print("Fibonacci sequence:", fib_sequence)

print("----Fibonacci using Recursion----")
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

for i in range(7):
    print(fibonacci(i))

print("----sum of n natural numbers----")
def total(n):

    if n == 0:
        return 0

    return n + total(n-1)

print(total(5))

