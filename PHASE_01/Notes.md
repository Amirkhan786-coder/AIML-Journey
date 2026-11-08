# PHASE 01 — PYTHON FUNDAMENTALS



Complete Detailed Notes

Beginner to Advanced

B.Tech CS-AI/ML



These notes cover all 17 topics from your Phase 01 Python Fundamentals roadmap. They are designed for learning, notebook practice, college preparation, coding interviews, and building a strong foundation for AI/ML engineering.

How to study these notes:

- Definition: English definition for exams and interviews.
- Explanation: Simple Hinglish explanation.
- Syntax: Correct Python syntax.
- Example: Practical code.
- Important points: Concepts you must remember.
- Practice: Questions to test your understanding.

# 1. Variables & Data Types

## 1.1 What is Python?

Definition: Python is a high-level, interpreted, general-purpose programming language known for its simple syntax and readability.

Explanation: Python ek programming language hai jiske through hum computer ko instructions dete hain. AI, ML, Data Science, Automation, Web Development aur Software Development mein iska use hota hai.

Example:

```
print("Hello, World!")
```

Output:

```
Hello, World!
```

## 1.2 Variables

Definition: A variable is a named memory reference used to store and access data in a program.

Explanation: Variable ek container/reference ki tarah hota hai jisme hum data store karte hain.

```
name = "Amir"age = 20marks = 85.5print(name)print(age)print(marks)
```

Output:

```
Amir
20
85.5
```

### Rules for naming variables

1. Variable name can contain letters, numbers and underscores.
2. It cannot start with a number.
3. Spaces are not allowed.
4. Python keywords cannot be used.
5. Variable names are case-sensitive.

```
student_name = "Amir"  # Validage2 = 20              # Valid_marks = 90            # Valid# 2age = 20             # Invalid# student name = "A"    # Invalid
```

### Multiple variable assignment

```
a, b, c = 10, 20, 30print(a, b, c)
```

Same value:

```
x = y = z = 100
```

Swapping:

```
a = 10b = 20a, b = b, aprint(a, b)
```

## 1.3 Data Types

Definition: Data types specify the kind of value a variable stores and the operations that can be performed on it.

Python's important built-in data types:

| Data type | Example     | Meaning              |
| --------- | ----------- | -------------------- |
| int       | `10`        | Integer              |
| float     | `10.5`      | Decimal              |
| complex   | `2+3j`      | Complex number       |
| str       | `"Hello"`   | Text                 |
| bool      | `True`      | Boolean              |
| list      | `[1, 2, 3]` | Mutable collection   |
| tuple     | `(1, 2, 3)` | Immutable collection |
| set       | `{1, 2, 3}` | Unique elements      |
| dict      | `{"a": 10}` | Key-value pairs      |
| NoneType  | `None`      | No value             |

### Checking data types

```
a = 10b = 10.5c = "Python"d = Trueprint(type(a))print(type(b))print(type(c))print(type(d))
```

### Type conversion (Type Casting)

Converting one data type into another.

```
x = "100"a = int(x)b = float(x)c = str(100)print(a + 50)  # 150print(b)       # 100.0print(c)       # "100"
```

Important conversions:

```
int()float()str()bool()list()tuple()set()
```

Remember: `input()` always returns a string unless you explicitly convert it.

```
age = int(input("Enter age: "))print(age + 1)
```

## 1.4 Dynamic Typing

Python is dynamically typed. You do not need to declare a variable's type before assigning a value.

```
x = 10print(type(x))x = "Python"print(type(x))
```

## 1.5 Mutable vs Immutable

| Mutable         | Immutable          |
| --------------- | ------------------ |
| Can be modified | Cannot be modified |
| List            | Tuple              |
| Dictionary      | String             |
| Set             | Integer            |
|                 | Float              |

Example:

```
numbers = [10, 20, 30]numbers[0] = 100print(numbers)
```

Output:

```
[100, 20, 30]
```

A string cannot be modified directly:

```
name = "Amir"# name[0] = "S"  # TypeError
```

# 2. Input / Output

## 2.1 Output Function — print()

Definition: The `print()` function displays information on the screen.

```
print("Hello Python")print(100)print(10 + 20)
```

### Important print parameters

sep: Separates multiple values.

```
print("Python", "Java", "C++", sep=" | ")
```

Output:

```
Python | Java | C++
```

end: Controls what appears at the end of a print statement.

```
print("Hello", end=" ")print("Amir")
```

Output:

```
Hello Amir
```

## 2.2 Input Function — input()

Definition: The `input()` function accepts user input from the keyboard.

```
name = input("Enter your name: ")print("Welcome", name)
```

### Taking numerical input

```
num1 = int(input("Enter first number: "))num2 = int(input("Enter second number: "))print("Sum:", num1 + num2)
```

### Taking multiple inputs

```
a, b = map(int, input("Enter two numbers: ").split())print(a + b)
```

### Formatted output (f-strings)

An f-string allows variables and expressions to be inserted into strings.

```
name = "Amir"age = 20print(f"My name is {name} and I am {age} years old.")
```

### Other formatting methods

```
name = "Amir"print("Hello {}".format(name))print("Hello %s" % name)
```

Important: Prefer f-strings in modern Python.

# 3. Operators

Definition: Operators are symbols or keywords that perform operations on variables and values.

## 3.1 Arithmetic Operators

| Operator | Meaning        | Example        |
| -------- | -------------- | -------------- |
| `+`      | Addition       | `10 + 5 = 15`  |
| `-`      | Subtraction    | `10 - 5 = 5`   |
| `*`      | Multiplication | `10 * 5 = 50`  |
| `/`      | Division       | `10 / 5 = 2.0` |
| `//`     | Floor division | `10 // 3 = 3`  |
| `%`      | Modulus        | `10 % 3 = 1`   |
| `**`     | Power          | `2 ** 3 = 8`   |

Example:

```
a = 10b = 3print(a + b)print(a // b)print(a % b)print(a ** b)
```

## 3.2 Comparison Operators

These operators compare two values and return `True` or `False`.

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal to              |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

```
a = 10b = 20print(a == b)print(a < b)print(a != b)
```

## 3.3 Logical Operators

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses the Boolean result         |

```
age = 20print(age > 18 and age < 30)print(age < 18 or age > 60)print(not age > 18)
```

## 3.4 Assignment Operators

```
x = 10x += 5x -= 2x *= 2x /= 2x //= 2x %= 2x **= 3
```

## 3.5 Membership Operators

Check whether an element exists in a sequence or collection.

- `in`
- `not in`

```
languages = ["Python", "Java", "C++"]print("Python" in languages)print("Ruby" not in languages)
```

## 3.6 Identity Operators

- `is`
- `is not`

They check whether two references point to the same object.

```
a = [1, 2, 3]b = ac = [1, 2, 3]print(a is b)  # Trueprint(a is c)  # Falseprint(a == c)  # True
```

Important interview question: Difference between `==` and `is`.

- `==` compares values.
- `is` compares object identity.

## 3.7 Bitwise Operators

These operate on the binary representation of integers.

| Operator | Meaning     |
| -------- | ----------- |
| `&`      | AND         |
| `\\|`    | OR          |
| `^`      | XOR         |
| `~`      | NOT         |
| `<<`     | Left shift  |
| `>>`     | Right shift |

```
a = 5b = 3print(a & b)print(a | b)print(a ^ b)print(a << 1)print(a >> 1)
```

# 4. Conditions (Decision Making)

Definition: Conditional statements allow a program to execute different blocks of code depending on whether conditions are true or false.

## 4.1 if statement

```
age = 20if age >= 18:    print("Eligible to vote")
```

## 4.2 if-else

```
age = 16if age >= 18:    print("Adult")else:    print("Minor")
```

## 4.3 if-elif-else

Used when multiple conditions need to be checked.

```
marks = 85if marks >= 90:    print("Grade A+")elif marks >= 80:    print("Grade A")elif marks >= 70:    print("Grade B")else:    print("Grade C")
```

## 4.4 Nested if

An if statement inside another if statement.

```
age = 22has_id = Trueif age >= 18:    if has_id:        print("Entry allowed")    else:        print("ID required")else:    print("Entry denied")
```

## 4.5 Ternary Operator

Short form of if-else.

```
age = 20result = "Adult" if age >= 18 else "Minor"print(result)
```

## 4.6 Match-Case

Python 3.10+ supports structural pattern matching.

```
day = 2match day:    case 1:        print("Monday")    case 2:        print("Tuesday")    case 3:        print("Wednesday")    case _:        print("Invalid day")
```

# 5. Loops

Definition: Loops are used to execute a block of code repeatedly until a condition is satisfied or a sequence is exhausted.

## 5.1 for loop

Used to iterate over a sequence.

```
for i in range(1, 6):    print(i)
```

Output:

```
1
2
3
4
5
```

### Understanding range()

`range(start, stop, step)`

```
range(1, 10, 2)
```

Generates:\
`1, 3, 5, 7, 9`

Remember: The stop value is excluded.

## 5.2 while loop

Repeats as long as the condition is true.

```
i = 1while i <= 5:    print(i)    i += 1
```

## 5.3 break

Terminates the loop immediately.

```
for i in range(1, 10):    if i == 5:        break    print(i)
```

## 5.4 continue

Skips the current iteration.

```
for i in range(1, 6):    if i == 3:        continue    print(i)
```

## 5.5 pass

A placeholder statement that does nothing.

```
for i in range(5):    if i == 2:        pass    print(i)
```

## 5.6 Nested Loops

A loop inside another loop.

```
for i in range(1, 4):    for j in range(1, 4):        print(i, j)
```

## 5.7 Loop with else

The `else` block executes when the loop completes normally without `break`.

```
for i in range(3):    print(i)else:    print("Loop completed")
```

## 5.8 Useful Loop Patterns

Multiplication table

```
num = 5for i in range(1, 11):    print(f"{num} x {i} = {num * i}")
```

Factorial

```
num = 5fact = 1for i in range(1, num + 1):    fact *= iprint(fact)
```

Reverse counting

```
for i in range(10, 0, -1):    print(i)
```

# 6. Strings

## 6.1 What is a String?

Definition: A string is an immutable sequence of Unicode characters enclosed in single, double, or triple quotes.

```
name = "Python"
```

## 6.2 String Indexing

Indexing means accessing individual characters.

```
text = "PYTHON"print(text[0])   # Pprint(text[1])   # Yprint(text[-1])  # N
```

[Python Strings | Cloud For Everybody](https://images.openai.com/static-rsc-4/bFdcO3EOawuv9jiGcpi6U3qEUFf6mrTde5KMyJAoVTY_xiAwovVqFcfCClZdVLnvpnFRLBRTDIAKg7Z4vEm_TA1Q7DAUUCkLf4eYOo7MA5LzUx_ZwGfczc6QrloA9742qCsvbyn1MHIKGN_yXpCdGxePz87nJePfuE8m1A0Iu-o?purpose=inline)

[medium.com](https://medium.com/cloud-for-everybody/mastering-python-strings-a-complete-guide-a4a9db97c366?utm_source=chatgpt.com)

## 6.3 String Slicing

Syntax:

```
string[start:stop:step]
```

```
text = "PYTHON"print(text[0:3])   # PYTprint(text[2:])    # THONprint(text[:4])    # PYTHprint(text[::-1])  # NOHTYP
```

## 6.4 Important String Methods

| Method         | Purpose                       |
| -------------- | ----------------------------- |
| `upper()`      | Uppercase                     |
| `lower()`      | Lowercase                     |
| `title()`      | Title case                    |
| `capitalize()` | Capitalize first character    |
| `strip()`      | Remove surrounding whitespace |
| `lstrip()`     | Remove left whitespace        |
| `rstrip()`     | Remove right whitespace       |
| `replace()`    | Replace text                  |
| `split()`      | Convert string into list      |
| `join()`       | Join strings                  |
| `find()`       | Find substring position       |
| `count()`      | Count occurrences             |
| `startswith()` | Check starting text           |
| `endswith()`   | Check ending text             |
| `isdigit()`    | Check digits                  |
| `isalpha()`    | Check alphabets               |
| `isalnum()`    | Check letters and digits      |

Examples:

```
text = "  hello python  "print(text.upper())print(text.strip())print(text.replace("python", "world"))print(text.split())
```

### String concatenation

```
first = "Hello"second = "World"print(first + " " + second)
```

### String formatting

```
name = "Amir"score = 95print(f"{name} scored {score}%")
```

### Important properties

- Strings are immutable.
- Strings support indexing and slicing.
- Strings support iteration.
- Strings store Unicode text.

# 7. Lists

## 7.1 What is a List?

Definition: A list is an ordered, mutable collection that allows duplicate elements and can store values of different data types.

```
numbers = [10, 20, 30, 40]
```

## 7.2 List Indexing and Slicing

```
numbers = [10, 20, 30, 40, 50]print(numbers[0])print(numbers[-1])print(numbers[1:4])
```

[🧠 What is Slicing in Python?](https://images.openai.com/static-rsc-4/BBi0vPyXTG8GeOwhm7PXDFEAVmivgl9K9eICXwblygZFN_WWXI9Jh0rd4ImYhO7g_sbDAbO07ARIE_dxTMjH5gUTVpYLsIEE07mha1YkVB5KBXxf_qrWUEsXetltWBEIP3_xut-YZXzJVQuxaJobxejjdn-pYm5O-KmgLG8Dl_s?purpose=inline)

[notechit.com](https://notechit.com/what-is-slicing-in-python?utm_source=chatgpt.com)

## 7.3 List Methods

| Method      | Purpose                      |
| ----------- | ---------------------------- |
| `append()`  | Add one element at end       |
| `extend()`  | Add multiple elements        |
| `insert()`  | Add at specific index        |
| `remove()`  | Remove first matching value  |
| `pop()`     | Remove and return an element |
| `clear()`   | Remove all elements          |
| `index()`   | Find element position        |
| `count()`   | Count occurrences            |
| `sort()`    | Sort the list                |
| `reverse()` | Reverse the list             |
| `copy()`    | Create a shallow copy        |

Examples:

```
numbers = [10, 20, 30]numbers.append(40)numbers.insert(1, 15)numbers.remove(20)print(numbers)
```

### Difference between append() and extend()

```
a = [1, 2]a.append([3, 4])print(a)# [1, 2, [3, 4]]b = [1, 2]b.extend([3, 4])print(b)# [1, 2, 3, 4]
```

## 7.4 List Comprehension

Definition: List comprehension is a concise way to create lists using an expression and optional conditions.

```
squares = [x**2 for x in range(1, 6)]print(squares)
```

With condition:

```
even = [x for x in range(1, 11) if x % 2 == 0]print(even)
```

## 7.5 Nested Lists

A list containing other lists.

```
matrix = [    [1, 2, 3],    [4, 5, 6],    [7, 8, 9]]print(matrix[0][1])
```

Output: `2`

## 7.6 List Copying

```
a = [1, 2, 3]b = a.copy()       # Shallow copyc = a              # Same object
```

Important concepts:

- Shallow copy
- Deep copy
- Aliasing
- Nested list behavior

# 8. Tuples

## 8.1 What is a Tuple?

Definition: A tuple is an ordered, immutable collection that allows duplicate values.

```
numbers = (10, 20, 30)
```

## 8.2 Creating Tuples

```
a = (1, 2, 3)b = 10, 20, 30c = (5,)  # Single-element tuple
```

Remember: A single-element tuple needs a comma.

## 8.3 Accessing Tuple Elements

```
data = ("Amir", 20, "AI/ML")print(data[0])print(data[-1])print(data[0:2])
```

## 8.4 Tuple Methods

Only two primary methods:

```
numbers = (10, 20, 10, 30)print(numbers.count(10))print(numbers.index(20))
```

## 8.5 Tuple Packing and Unpacking

```
student = ("Amir", 20, "AI/ML")name, age, branch = studentprint(name)print(age)print(branch)
```

## 8.6 List vs Tuple

| List                      | Tuple                      |
| ------------------------- | -------------------------- |
| Mutable                   | Immutable                  |
| `[]`                      | `()`                       |
| More modification methods | Two main methods           |
| Used for changing data    | Used for fixed collections |

AI/ML application: Tuples are useful for fixed dimensions, coordinates, and returning multiple values from functions.

# 9. Sets

## 9.1 What is a Set?

Definition: A set is an unordered collection of unique, hashable elements.

```
numbers = {10, 20, 30, 10}print(numbers)
```

Output contains each unique element only once.

## 9.2 Creating an Empty Set

```
a = set()
```

Important: `{}` creates an empty dictionary, not an empty set.

## 9.3 Set Methods

| Method      | Purpose                               |
| ----------- | ------------------------------------- |
| `add()`     | Add one element                       |
| `update()`  | Add multiple elements                 |
| `remove()`  | Remove an element; error if absent    |
| `discard()` | Remove an element; no error if absent |
| `pop()`     | Remove an arbitrary element           |
| `clear()`   | Remove all elements                   |
| `copy()`    | Copy a set                            |

## 9.4 Set Operations

[Set Operations | Agent Factory](https://images.openai.com/static-rsc-4/t4zqQMaw_V5Vc1_H6ycOgGK2rWS8f1xOdX3PgCJDi5MZCpf1wAxVtqD9TYvPoDPMvLebm0M9lb5S_B1UWpnDs7noJNlwGStyvgqVH0u4HTLNT9jPpONxrDSDXCXu2WjnfDePwLBV-pxRrqYpya8HUxe07v-mQvDA-qC0y2tO5-c?purpose=inline)

[agentfactory.panaversity.org](https://agentfactory.panaversity.org/docs/Programming-in-the-AI-Era/set-frozenset-gc/set-operations?utm_source=chatgpt.com)

```
A = {1, 2, 3, 4}B = {3, 4, 5, 6}print(A | B)  # Unionprint(A & B)  # Intersectionprint(A - B)  # Differenceprint(A ^ B)  # Symmetric difference
```

| Operation            | Meaning                              |
| -------------------- | ------------------------------------ |
| Union                | All unique elements                  |
| Intersection         | Common elements                      |
| Difference           | Elements in A but not B              |
| Symmetric difference | Elements in either set, but not both |

Other useful methods:

```
A.issubset(B)A.issuperset(B)A.isdisjoint(B)
```

Practical application: Removing duplicates from data.

```
data = [1, 2, 2, 3, 3, 4]unique_data = list(set(data))print(unique_data)
```

Note: Set conversion does not guarantee preserving the original order.

# 10. Dictionaries

## 10.1 What is a Dictionary?

Definition: A dictionary is a mutable mapping that stores data in key-value pairs.

```
student = {    "name": "Amir",    "age": 20,    "branch": "AI/ML"}
```

## 10.2 Accessing Values

```
print(student["name"])print(student.get("age"))
```

Difference:

- `student["key"]` raises `KeyError` if the key is missing.
- `student.get("key")` returns `None` by default.

## 10.3 Adding and Updating

```
student["marks"] = 90student["age"] = 21print(student)
```

## 10.4 Dictionary Methods

| Method         | Purpose                   |
| -------------- | ------------------------- |
| `keys()`       | Get all keys              |
| `values()`     | Get all values            |
| `items()`      | Get key-value pairs       |
| `get()`        | Safely retrieve a value   |
| `update()`     | Add or update entries     |
| `pop()`        | Remove a specified key    |
| `popitem()`    | Remove last inserted pair |
| `clear()`      | Remove everything         |
| `copy()`       | Create a shallow copy     |
| `setdefault()` | Get key or insert default |

## 10.5 Dictionary Iteration

```
student = {    "name": "Amir",    "age": 20,    "marks": 90}for key, value in student.items():    print(key, value)
```

## 10.6 Nested Dictionary

```
students = {    "student1": {        "name": "Amir",        "marks": 90    },    "student2": {        "name": "Rahul",        "marks": 85          }}print(students["student1"]["name"])
```

## 10.7 Dictionary Comprehension

```
squares = {x: x**2 for x in range(1, 6)}print(squares)
```

AI/ML application: Dictionaries are commonly used for JSON data, API responses, configuration, feature mappings, and frequency counting.

# 11. Functions

## 11.1 What is a Function?

Definition: A function is a reusable block of code designed to perform a specific task.

Explanation: Ek hi code ko baar-baar likhne ke bajay function banakar multiple times call kar sakte hain.

## 11.2 Creating a Function

Syntax:

```
def function_name():    # Code    pass
```

Example:

```
def greet():    print("Hello Amir")greet()
```

## 11.3 Function with Parameters

```
def greet(name):    print("Hello", name)greet("Amir")
```

## 11.4 Return Statement

The `return` statement sends a result back to the caller.

```
def add(a, b):    return a + bresult = add(10, 20)print(result)
```

Difference:

- `print()` displays output.
- `return` sends a value back to the calling code.

## 11.5 Types of Function Arguments

1\. Positional arguments

```
def student(name, age):    print(name, age)student("Amir", 20)
```

2\. Keyword arguments

```
student(age=20, name="Amir")
```

3\. Default arguments

```
def greet(name="Student"):    print("Hello", name)greet()greet("Amir")
```

\*4. Variable-length positional arguments — args

```
def add(*numbers):    return sum(numbers)print(add(10, 20, 30, 40))
```

\*\*5. Variable-length keyword arguments — kwargs

```
def details(**data):    print(data)details(name="Amir", age=20, branch="AI/ML")
```

## 11.6 Lambda Function

Definition: A lambda function is a small anonymous function written in a single expression.

```
square = lambda x: x**2print(square(5))
```

## 11.7 map(), filter(), reduce()

map(): Applies a function to every element.

```
numbers = [1, 2, 3, 4]result = list(map(lambda x: x*2, numbers))print(result)
```

filter(): Selects elements satisfying a condition.

```
numbers = [1, 2, 3, 4, 5, 6]result = list(filter(lambda x: x % 2 == 0, numbers))print(result)
```

reduce(): Combines elements into a single result.

```
from functools import reducenumbers = [1, 2, 3, 4]result = reduce(lambda a, b: a+b, numbers)print(result)
```

## 11.8 Scope of Variables

Local variable: Created inside a function.

Global variable: Created outside a function.

```
x = 100def show():    y = 50    print(x)    print(y)show()
```

### global keyword

```
x = 10def change():    global x    x = 20change()print(x)
```

### nonlocal keyword

Used to modify a variable in an enclosing function.

```
def outer():    x = 10    def inner():        nonlocal x        x = 20    inner()    print(x)outer()
```

## 11.9 Recursion vs Iteration

Recursion means a function calls itself. Iteration means repeating code using loops.

More details in Topic 12.

# 12. Recursion

## 12.1 What is Recursion?

Definition: Recursion is a programming technique in which a function calls itself to solve a problem by breaking it into smaller subproblems.

Two important parts:

1. Base case — stops recursion.
2. Recursive case — calls the function again with a smaller or simpler input.

## 12.2 Factorial Using Recursion

```
def factorial(n):    if n == 0 or n == 1:        return 1    return n * factorial(n - 1)print(factorial(5))
```

Output:

```
120
```

Understanding:

```
factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
120
```

## 12.3 Fibonacci Series

```
def fibonacci(n):    if n <= 1:        return n    return fibonacci(n-1) + fibonacci(n-2)for i in range(7):    print(fibonacci(i))
```

Output:

```
0
1
1
2
3
5
8
```

## 12.4 Sum of Natural Numbers

```
def total(n):    if n == 0:        return 0    return n + total(n-1)print(total(5))
```

## 12.5 Recursion vs Iteration

| Recursion                       | Iteration                           |
| ------------------------------- | ----------------------------------- |
| Function calls itself           | Uses loops                          |
| Uses call stack                 | Usually uses less call-stack memory |
| Can be elegant for trees        | Often better for simple repetition  |
| May have recursion-depth limits | Avoids recursive-depth limits       |

Important: Python has a recursion limit. Deep recursion may raise `RecursionError`.

# 13. Modules & Packages

## 13.1 What is a Module?

Definition: A module is a Python file containing reusable code, such as functions, variables, and classes.

Example structure:

```
project/
│
├── main.py
└── calculator.py
```

`calculator.py`

```
def add(a, b):    return a + b
```

`main.py`

```
import calculatorprint(calculator.add(10, 20))
```

## 13.2 Different Import Methods

```
import mathprint(math.sqrt(25))
```

Import a specific function:

```
from math import sqrtprint(sqrt(25))
```

Use an alias:

```
import numpy as np
```

Import everything:

```
from math import *
```

Avoid wildcard imports in larger projects because they can cause naming conflicts.

## 13.3 Built-in Modules

| Module        | Purpose                        |
| ------------- | ------------------------------ |
| `math`        | Mathematical operations        |
| `random`      | Random values                  |
| `os`          | Operating system operations    |
| `sys`         | Python interpreter information |
| `datetime`    | Date and time                  |
| `json`        | JSON handling                  |
| `statistics`  | Statistical calculations       |
| `re`          | Regular expressions            |
| `collections` | Specialized containers         |
| `pathlib`     | File paths                     |

Examples:

```
import mathprint(math.factorial(5))import randomprint(random.randint(1, 10))import datetimeprint(datetime.datetime.now())
```

## 13.4 What is a Package?

Definition: A package is a way of organizing related Python modules into a directory structure.

Example:

```
my_project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── calculator.py
    └── helper.py
```

Import:

```
from utils.calculator import add
```

## 13.5 pip

`pip` is Python's package installer.

Install a library:

```
pip install numpy
```

Check installed packages:

```
pip list
```

Save dependencies:

```
pip freeze > requirements.txt
```

Install project dependencies:

```
pip install -r requirements.txt
```

## 13.6 Virtual Environment

A virtual environment keeps project dependencies separate.

Create:

```
python -m venv venv
```

Activate in Windows PowerShell:

```
.\venv\Scripts\Activate.ps1
```

Deactivate:

```
deactivate
```

## 13.7 name == "main"

```
def main():    print("Program started")if __name__ == "__main__":    main()
```

This ensures that the main code runs when the file is executed directly, rather than when it is imported as a module.

# 14. File Handling

## 14.1 What is File Handling?

Definition: File handling is the process of creating, opening, reading, writing, appending, and closing files using a programming language.

Python supports text and binary files.

## 14.2 Opening a File

Syntax:

```
file = open("data.txt", "r")
```

## 14.3 File Modes

| Mode | Meaning                            |
| ---- | ---------------------------------- |
| `r`  | Read                               |
| `w`  | Write; overwrites existing content |
| `a`  | Append                             |
| `x`  | Create; fails if file exists       |
| `b`  | Binary mode                        |
| `t`  | Text mode                          |
| `r+` | Read and write                     |

## 14.4 Writing a File

```
file = open("data.txt", "w")file.write("Hello Python")file.close()
```

## 14.5 Reading a File

```
file = open("data.txt", "r")content = file.read()print(content)file.close()
```

Other methods:

```
file.readline()file.readlines()
```

## 14.6 Appending Data

```
with open("data.txt", "a") as file:    file.write("\nLearning Python")
```

## 14.7 The with Statement

Definition: The `with` statement uses a context manager to manage resources automatically, including closing files after use.

Recommended approach:

```
with open("data.txt", "r") as file:    content = file.read()    print(content)
```

You don't need to manually call `close()` when using `with`.

## 14.8 Working with CSV Files

CSV means Comma-Separated Values.

```
import csvwith open("students.csv", "w", newline="") as file:    writer = csv.writer(file)    writer.writerow(["Name", "Age", "Marks"])    writer.writerow(["Amir", 20, 90])
```

## 14.9 Working with JSON

JSON means JavaScript Object Notation. It is commonly used for API communication and data storage.

```
import jsonstudent = {    "name": "Amir",    "age": 20}with open("student.json", "w") as file:    json.dump(student, file, indent=4)
```

Read JSON:

```
with open("student.json", "r") as file:    data = json.load(file)print(data["name"])
```

# 15. Exception Handling

## 15.1 What is an Exception?

Definition: An exception is an error or unexpected event that occurs during program execution and interrupts the normal flow of the program.

Example:

```
a = 10b = 0print(a / b)
```

Output: `ZeroDivisionError`

## 15.2 try-except

```
try:    a = 10    b = 0    print(a / b)except ZeroDivisionError:    print("Cannot divide by zero")
```

## 15.3 try-except-else

The `else` block runs if no exception occurs in the `try` block.

```
try:    num = int(input("Enter number: "))    result = 10 / numexcept ZeroDivisionError:    print("Cannot divide by zero")except ValueError:    print("Enter a valid integer")else:    print("Result:", result)
```

## 15.4 finally

The `finally` block executes whether an exception occurs or not.

```
try:    print("Program running")except Exception:    print("Error occurred")finally:    print("Program completed")
```

## 15.5 Common Python Exceptions

| Exception             | Reason                          |
| --------------------- | ------------------------------- |
| `NameError`           | Undefined variable              |
| `TypeError`           | Invalid operation between types |
| `ValueError`          | Correct type, invalid value     |
| `IndexError`          | Invalid sequence index          |
| `KeyError`            | Missing dictionary key          |
| `ZeroDivisionError`   | Division by zero                |
| `FileNotFoundError`   | File does not exist             |
| `ImportError`         | Import failure                  |
| `AttributeError`      | Missing attribute               |
| `ModuleNotFoundError` | Module not found                |

## 15.6 Raising Exceptions

The `raise` keyword manually triggers an exception.

```
age = -5if age < 0:    raise ValueError("Age cannot be negative")
```

## 15.7 Custom Exceptions

```
class InvalidAgeError(Exception):    passage = 15if age < 18:    raise InvalidAgeError("Age must be 18 or above")
```

Best practice: Catch specific exceptions instead of using a broad `except Exception` everywhere.

# 16. Object-Oriented Programming (OOP)



Very Important

High Priority for AI/ML Engineering



OOP is one of the most important Python concepts. You will use it while developing large projects, AI applications, APIs, and software systems.

## 16.1 What is OOP?

Definition: Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects and classes, combining data and methods into reusable structures.

Explanation: OOP mein hum real-world entities ko programming ke form mein represent karte hain.

For example:

A student has:

- Name
- Age
- Branch
- Marks

A student can perform:

- Study
- Attend class
- Give exams

In OOP, data represents attributes and actions represent methods.

## 16.2 Class

Definition: A class is a blueprint or template used to create objects.

Example:

```
class Student:    name = "Amir"    age = 20    branch = "AI/ML"
```

Here, `Student` is a class.

## 16.3 Object

Definition: An object is an instance of a class that contains data and can access the methods defined by that class.

```
class Student:    name = "Amir"student1 = Student()print(student1.name)
```

Output:

```
Amir
```

[Sample Animated Lesson Videos – Imagnica](https://images.openai.com/static-rsc-4/nH8hm5bBC3XjDKK4X7CYd2fsgxvM-D2EqBPvWX4XXHhHvaDwhENYmOWWB0PMCp9Y31V-T3Ds9AI1Q8AbXgd7dfCDznnR1nLim7tNFzbJN69XB7A_AEAHasOb-nS8NckaYqkPyrj6z6ofOqIjH-ICnbeVQf1tqTkN5TYFA4B3lMk?purpose=inline)

[imagnica.com](https://imagnica.com/showcase?utm_source=chatgpt.com)

## 16.4 Constructor — init()

Definition: A constructor is a special method used to initialize an object's attributes when an object is created.

Python uses `__init__()` for initialization.

```
class Student:    def __init__(self, name, age, branch):        self.name = name        self.age = age        self.branch = branchstudent1 = Student("Amir", 20, "AI/ML")print(student1.name)print(student1.age)print(student1.branch)
```

Output:

```
Amir
20
AI/ML
```

### Understanding self

`self` refers to the current instance of the class.

```
class Student:    def __init__(self, name):        self.name = name    def show(self):        print(self.name)s1 = Student("Amir")s1.show()
```

Remember:

- `self` is not a Python keyword.
- It is the conventional name for the instance parameter.
- Instance methods receive the instance automatically.

## 16.5 Attributes and Methods

Attributes: Variables belonging to a class or object.

Methods: Functions defined inside a class.

```
class Student:    def __init__(self, name, marks):        self.name = name        self.marks = marks    def display(self):        print(self.name, self.marks)    def check_result(self):        if self.marks >= 40:            print("Pass")        else:            print("Fail")s1 = Student("Amir", 90)s1.display()s1.check_result()
```

## 16.6 Four Pillars of OOP

[AI For Learning and Studying. AI tools — such as ChatGPT, Google’s… | by Dr. Nimrita Koul | Medium](https://images.openai.com/static-rsc-4/FrkgAP78jq1xCKYhGOh9xJmphEVhL5hy7neF3zu6YFpirtxBc088jg2BpgUcVa4QQ56BO-ioSFStjhpISSXEVD1WsCnjsareBqYzcHKvy-Za0X2ADKrQ-5OduzxVu18HFiJ3cv9QPObvzMJTyCv8wNiJv84mjYpNHbeIdIs6eqk?purpose=inline)

[medium.com](https://medium.com/%40nimritakoul01/ai-for-learning-and-studying-608ebef95894?utm_source=chatgpt.com)

### Pillar 1: Encapsulation

Definition: Encapsulation is the process of bundling data and methods together within a class and controlling access to the internal state.

Explanation: Data aur usse related functions ko ek class ke andar organize karna encapsulation hai.

```
class BankAccount:    def __init__(self, balance):        self.__balance = balance    def deposit(self, amount):        if amount > 0:            self.__balance += amount    def get_balance(self):        return self.__balanceaccount = BankAccount(1000)account.deposit(500)print(account.get_balance())
```

Output:

```
1500
```

Python naming conventions:

| Naming   | Meaning                 |
| -------- | ----------------------- |
| `name`   | Public                  |
| `_name`  | Internal-use convention |
| `__name` | Name-mangled attribute  |

Important: Double underscore does not provide absolute security. Python uses name mangling to reduce accidental access and collisions.

### Pillar 2: Inheritance

Definition: Inheritance is an OOP mechanism through which one class acquires attributes and methods from another class.

Explanation: Ek existing class ke features ko doosri class mein reuse karna inheritance hai.

```
class Animal:    def eat(self):        print("Animal is eating")class Dog(Animal):    def bark(self):        print("Dog is barking")d = Dog()d.eat()d.bark()
```

Types of inheritance:

[Inheritance and Access Modifier | LEARN.NETLAB](https://images.openai.com/static-rsc-4/aTdT7WFURKh5sn36Uz3zrXWdyne2Mp3jATXzTqsApka8chU_u5Kf9CBN0tIP0k-jngF5VP4J0whAwQvi5HB_bj8p_djjpjLqx-BgML_BRCgMMStdJB5PM4e-toQmo_wnvS5mcvafPxXMj8uOXMiC8xtjJAFM00rbLdqLZM7PKgM?purpose=inline)

[learn.netlabdte.com](https://learn.netlabdte.com/docs/OOP/InheritanceAndAccessModifier?utm_source=chatgpt.com)

1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance

Single inheritance:

```
class A:    def show(self):        print("Class A")class B(A):    passobj = B()obj.show()
```

Multiple inheritance:

```
class Father:    def skill1(self):        print("Programming")class Mother:    def skill2(self):        print("Communication")class Child(Father, Mother):    passobj = Child()obj.skill1()obj.skill2()
```

Multilevel inheritance:

```
class A:    passclass B(A):    passclass C(B):    pass
```

### super() Function

`super()` allows a child class to access methods of its parent class according to Python's method resolution order.

```
class Animal:    def __init__(self, name):        self.name = nameclass Dog(Animal):    def __init__(self, name, breed):        super().__init__(name)        self.breed = breeddog = Dog("Tommy", "Labrador")print(dog.name)print(dog.breed)
```

### Pillar 3: Polymorphism

Definition: Polymorphism means one interface can represent different behaviors depending on the object or context.

Explanation: Same method name, different classes, different behavior.

```
class Dog:    def sound(self):        print("Bark")class Cat:    def sound(self):        print("Meow")def make_sound(animal):    animal.sound()make_sound(Dog())make_sound(Cat())
```

Output:

```
Bark
Meow
```

Other concepts:

- Method overriding
- Operator overloading
- Duck typing

Method overriding:

```
class Animal:    def sound(self):        print("Animal sound")class Dog(Animal):    def sound(self):        print("Bark")d = Dog()d.sound()
```

The child class provides its own implementation of the inherited method.

Operator overloading:

```
class Number:    def __init__(self, value):        self.value = value    def __add__(self, other):        return self.value + other.valuea = Number(10)b = Number(20)print(a + b)
```

### Pillar 4: Abstraction

Definition: Abstraction hides implementation details and exposes only the essential interface.

Explanation: User ko sirf necessary functionality dikhana, internal implementation hide rakhna.

Python provides the `abc` module for abstract base classes.

```
from abc import ABC, abstractmethodclass Shape(ABC):    @abstractmethod    def area(self):        passclass Circle(Shape):    def __init__(self, radius):        self.radius = radius    def area(self):        return 3.14 * self.radius ** 2c = Circle(5)print(c.area())
```

An abstract class with an unimplemented abstract method cannot normally be instantiated.

## 16.7 Types of Methods

### 1. Instance Method

Works with individual object data.

```
class Student:    def show(self):        print("Instance method")s = Student()s.show()
```

### 2. Class Method

Works with class-level data and receives `cls`.

```
class Student:    college = "ABC College"    @classmethod    def show_college(cls):        print(cls.college)Student.show_college()
```

### 3. Static Method

Does not receive `self` or `cls` automatically.

```
class Calculator:    @staticmethod    def add(a, b):        return a + bprint(Calculator.add(10, 20))
```

| Method   | First parameter    | Typical use           |
| -------- | ------------------ | --------------------- |
| Instance | `self`             | Object data           |
| Class    | `cls`              | Class-level data      |
| Static   | None automatically | Related utility logic |

## 16.8 Property Decorator

The `@property` decorator allows a method to be accessed like an attribute.

```
class Student:    def __init__(self, marks):        self._marks = marks    @property    def marks(self):        return self._marks    @marks.setter    def marks(self, value):        if 0 <= value <= 100:            self._marks = value        else:            raise ValueError("Invalid marks")s = Student(90)print(s.marks)s.marks = 95print(s.marks)
```

## 16.9 Magic / Dunder Methods

Special methods with double underscores.

| Method       | Purpose                           |
| ------------ | --------------------------------- |
| `__init__()` | Initialize object                 |
| `__str__()`  | Human-readable string             |
| `__repr__()` | Developer-oriented representation |
| `__len__()`  | Length behavior                   |
| `__add__()`  | Addition behavior                 |
| `__eq__()`   | Equality behavior                 |
| `__call__()` | Make an object callable           |
| `__iter__()` | Iterator behavior                 |
| `__next__()` | Next iterator value               |

Example:

```
class Student:    def __init__(self, name):        self.name = name    def __str__(self):        return f"Student: {self.name}"s = Student("Amir")print(s)
```

## 16.10 Composition

Definition: Composition is a design technique in which one class contains an object of another class to build complex functionality.

```
class Engine:    def start(self):        print("Engine started")class Car:    def __init__(self):        self.engine = Engine()    def start_car(self):        self.engine.start()        print("Car started")car = Car()car.start_car()
```

## 16.11 OOP vs Procedural Programming

| OOP                      | Procedural                        |
| ------------------------ | --------------------------------- |
| Organized around objects | Organized around functions        |
| Supports inheritance     | No class-based inheritance        |
| Encapsulation supported  | Data and functions often separate |
| Useful for large systems | Useful for simple scripts         |

### OOP Interview Questions

1. What is a class?
2. What is an object?
3. What is a constructor?
4. What is `self`?
5. What are the four pillars of OOP?
6. Difference between abstraction and encapsulation?
7. Difference between overloading and overriding?
8. What is multiple inheritance?
9. What is MRO (Method Resolution Order)?
10. Difference between class method and static method?
11. What is composition?
12. What are magic methods?

# 17. Advanced Python



High Priority

Important for AI/ML Projects



Advanced Python helps you write efficient, reusable, maintainable, and professional code.

## 17.1 List, Dictionary and Set Comprehensions

Comprehensions allow you to create collections in a concise way.

List comprehension:

```
squares = [x**2 for x in range(1, 6)]
```

Dictionary comprehension:

```
squares = {x: x**2 for x in range(1, 6)}
```

Set comprehension:

```
squares = {x**2 for x in range(1, 6)}
```

Conditional comprehension:

```
even = [x for x in range(20) if x % 2 == 0]
```

Nested comprehension:

```
matrix = [[j for j in range(3)] for i in range(3)]print(matrix)
```

## 17.2 Iterators and Iterables

Iterable: An object that can return its elements one by one through iteration.

Examples:

- List
- Tuple
- String
- Dictionary
- Set

Iterator: An object that produces values one at a time using `__next__()`.

Example:

```
numbers = [10, 20, 30]iterator = iter(numbers)print(next(iterator))print(next(iterator))print(next(iterator))
```

Output:

```
10
20
30
```

When no more values are available, Python raises `StopIteration`.

Difference:

| Iterable                  | Iterator                  |
| ------------------------- | ------------------------- |
| Can be iterated over      | Produces next values      |
| Example: list             | Example: `iter(list)`     |
| May create a new iterator | Maintains iteration state |

## 17.3 Generators

Definition: A generator is a special type of iterator that produces values lazily, one at a time.

It uses `yield` instead of returning all results at once.

```
def numbers():    yield 10    yield 20    yield 30for num in numbers():    print(num)
```

Output:

```
10
20
30
```

### Generator with a loop

```
def count(n):    for i in range(1, n + 1):        yield ifor value in count(5):    print(value)
```

### Generator Expression

```
squares = (x**2 for x in range(1, 6))for value in squares:    print(value)
```

Why generators matter:

- Memory-efficient processing.
- Useful for large datasets.
- Useful for streaming data.
- Avoid creating huge lists in memory.

AI/ML example: Processing a large dataset batch by batch.

## 17.4 Decorators

Definition: A decorator is a function that modifies or extends the behavior of another function without directly changing its original source code.

Example:

```
def decorator(func):    def wrapper():        print("Before function")        func()        print("After function")    return wrapper@decoratordef greet():    print("Hello Amir")greet()
```

Output:

```
Before function
Hello Amir
After function
```

### Decorator with arguments

```
def decorator(func):    def wrapper(*args, **kwargs):        print("Function started")        result = func(*args, **kwargs)        print("Function completed")        return result    return wrapper@decoratordef add(a, b):    return a + bprint(add(10, 20))
```

### functools.wraps

Preserves important metadata of the decorated function.

```
from functools import wrapsdef decorator(func):    @wraps(func)    def wrapper(*args, **kwargs):        return func(*args, **kwargs)    return wrapper
```

Applications:

- Logging
- Authentication
- Timing functions
- Caching
- API route handling

## 17.5 Lambda Functions — Advanced Usage

```
students = [    ("Amir", 90),    ("Rahul", 80),    ("Aman", 95)]students.sort(key=lambda x: x[1])print(students)
```

Here, the lambda function defines the sorting key.

## 17.6 \*args and \*\*kwargs — Advanced Understanding

`*args` collects extra positional arguments into a tuple.

```
def total(*args):    return sum(args)print(total(10, 20, 30, 40))
```

`**kwargs` collects extra keyword arguments into a dictionary.

```
def profile(**kwargs):    for key, value in kwargs.items():        print(key, value)profile(name="Amir", branch="AI/ML", year=2)
```

Unpacking:

```
numbers = [10, 20]def add(a, b):    return a + bprint(add(*numbers))
```

```
data = {"name": "Amir", "age": 20}def show(name, age):    print(name, age)show(**data)
```

## 17.7 Scope and Closures

Closure: A closure is an inner function that remembers variables from its enclosing function even after the enclosing function has finished executing.

```
def outer(message):    def inner():        print(message)    return innergreet = outer("Hello Amir")greet()
```

Closures are useful in decorators and function factories.

## 17.8 Shallow Copy and Deep Copy

Shallow copy: Creates a new outer object but keeps references to nested objects.

Deep copy: Recursively creates copies of nested objects.

```
import copyoriginal = [[1, 2], [3, 4]]shallow = copy.copy(original)deep = copy.deepcopy(original)original[0][0] = 100print(shallow)print(deep)
```

## 17.9 Context Managers

Definition: A context manager manages resources and ensures that setup and cleanup operations are handled appropriately.

Example:

```
with open("data.txt", "r") as file:    data = file.read()
```

You can also create your own context manager.

```
from contextlib import contextmanager@contextmanagerdef my_context():    print("Starting")    try:        yield    finally:        print("Ending")with my_context():    print("Inside context")
```

## 17.10 Exception Handling — Advanced

You should understand:

- Custom exceptions
- Exception chaining
- Raising exceptions
- Specific exception handling
- `try`, `except`, `else`, `finally`

Example of exception chaining:

```
try:    int("Python")except ValueError as error:    raise RuntimeError("Conversion failed") from error
```

## 17.11 Regular Expressions (RegEx)

Definition: Regular expressions are patterns used to search, match, and manipulate text.

Python provides the `re` module.

```
import retext = "My phone number is 9876543210"result = re.findall(r"\d+", text)print(result)
```

Important patterns:

| Pattern | Meaning                                 |
| ------- | --------------------------------------- |
| `\d`    | Digit                                   |
| `\D`    | Non-digit                               |
| `\w`    | Word character                          |
| `\s`    | Whitespace                              |
| `.`     | Any character except newline by default |
| `^`     | Start of string                         |
| `$`     | End of string                           |
| `+`     | One or more                             |
| `*`     | Zero or more                            |
| `{n}`   | Exactly n repetitions                   |

Example: Basic email pattern matching.

```
import reemail = "amir@example.com"pattern = r"^[\w.-]+@[\w.-]+\.\w+$"if re.match(pattern, email):    print("Valid format")else:    print("Invalid format")
```

Note: Regex validation checks format; it cannot confirm that an email address actually exists.

## 17.12 Type Hints

Definition: Type hints are annotations that indicate the expected types of variables, parameters, and return values.

```
def add(a: int, b: int) -> int:    return a + bresult: int = add(10, 20)
```

With collections:

```
def get_names() -> list[str]:    return ["Amir", "Rahul"]
```

Type hints improve readability and help static analysis tools. Python does not automatically enforce them at runtime.

## 17.13 Dataclasses

Dataclasses reduce repetitive code when creating classes primarily used to store data.

```
from dataclasses import dataclass@dataclassclass Student:    name: str    age: int    marks: floats = Student("Amir", 20, 90.5)print(s)
```

Python automatically generates methods such as `__init__()` and `__repr__()`.

## 17.14 Collections Module

The `collections` module provides specialized data structures.

Counter:

```
from collections import Counterdata = ["Python", "Java", "Python", "C++"]result = Counter(data)print(result)
```

defaultdict:

```
from collections import defaultdictdata = defaultdict(list)data["AI"].append("Python")data["AI"].append("Machine Learning")print(data)
```

deque:

```
from collections import dequequeue = deque([10, 20, 30])queue.append(40)queue.appendleft(5)print(queue)
```

## 17.15 Functional Programming

Important concepts:

- Pure functions
- Higher-order functions
- Lambda functions
- `map()`
- `filter()`
- `reduce()`
- Immutability
- Function composition

A pure function returns a result based on its inputs without modifying external state or causing observable side effects.

```
def square(number):    return number * numberprint(square(5))
```

## 17.16 Memory Management

Important topics:

- Object references
- Reference counting
- Garbage collection
- Mutable vs immutable objects
- Shallow vs deep copying
- Memory-efficient generators

Python automatically manages most object memory.

Example:

```
import gcprint(gc.isenabled())
```

## 17.17 Multithreading and Multiprocessing

These concepts are important when building real-world applications.

Multithreading: Multiple threads run within one process and share its memory.

Useful for:

- API requests
- Network operations
- File operations
- I/O-bound tasks

```
import threadingdef task():    print("Task running")t1 = threading.Thread(target=task)t1.start()t1.join()
```

Multiprocessing: Multiple processes run independently, each with its own memory space.

Useful for:

- CPU-intensive tasks
- Parallel numerical computations
- Independent data processing

```
from multiprocessing import Processdef task():    print("Process running")if __name__ == "__main__":    p = Process(target=task)    p.start()    p.join()
```

Important: Python's standard CPython build uses a Global Interpreter Lock (GIL) that affects execution of Python bytecode across threads. Multiprocessing can help with CPU-bound parallelism. I/O-bound work can benefit from threading even with the GIL.

## 17.18 Asynchronous Programming — async/await

Used for concurrent I/O operations without blocking the event loop.

```
import asyncioasync def greet():    print("Hello")    await asyncio.sleep(1)    print("Welcome")asyncio.run(greet())
```

Important terms:

- `async`
- `await`
- Coroutine
- Event loop
- `asyncio`

Applications: API calls, asynchronous web applications, network communication.

## 17.19 Debugging and Logging

Debugging: Finding and fixing errors in code.

Useful tools:

- VS Code debugger
- Breakpoints
- Step over
- Step into
- Variable inspection
- Python `pdb`

Logging: Recording program events and errors.

```
import logginglogging.basicConfig(level=logging.INFO)logging.debug("Debug message")logging.info("Application started")logging.warning("Warning message")logging.error("An error occurred")logging.critical("Critical error")
```

Logging levels:

1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL

## 17.20 Unit Testing

Definition: Unit testing is the process of testing individual components or functions to verify that they behave as expected.

Python provides `unittest`.

```
import unittestdef add(a, b):    return a + bclass TestCalculator(unittest.TestCase):    def test_add(self):        self.assertEqual(add(10, 20), 30)if __name__ == "__main__":    unittest.main()
```

Also learn `pytest` later for practical project testing.

## 17.21 Python Best Practices

1. Use meaningful variable names.
2. Follow PEP 8 coding conventions.
3. Use functions to avoid repeated code.
4. Use classes when they improve organization.
5. Handle exceptions properly.
6. Write reusable modules.
7. Use virtual environments.
8. Use type hints where useful.
9. Write tests.
10. Use Git and GitHub for version control.
11. Use logging instead of excessive print statements in applications.
12. Keep code readable and maintainable.


Testing

Reset progress

# 18. Final Python Fundamentals Checklist

Use this checklist to decide whether you have actually completed Phase 01.

# 0%

Overall Phase 01 completion

1\. Python Core

Variables and data types

Input and output

All operators

Conditions

Loops

Strings

2\. Python Collections

Lists and list comprehension

Tuples and unpacking

Sets and set operations

Dictionaries and nested dictionaries

3\. Programming Logic

Functions and arguments

Recursion

Modules and packages

File handling

Exception handling

4\. Object-Oriented Programming

Classes and objects

Constructors and self

Encapsulation

Inheritance

Polymorphism

Abstraction

Methods and decorators

Magic methods and composition

5\. Advanced Python

Comprehensions

Iterators and generators

Decorators and closures

Shallow and deep copy

Context managers

Regular expressions

Type hints and dataclasses

Memory management

Threading and multiprocessing

Async programming

Debugging, logging and testing

