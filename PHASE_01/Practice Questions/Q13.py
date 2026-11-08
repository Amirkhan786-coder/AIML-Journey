print("----Exception Handling----")

"""a = 10
   b = 0

print(a / b)"""



print("try-except")
try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")




print("try-except-else")
try:
    num = int(input("Enter number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter a valid integer")

else:
    print("Result:", result)




print("finally")

try:
    print("Program running")

except Exception:
    print("Error occurred")

finally:
    print("Program completed")




print("Raising Exceptions")
age1 = -5

if age1 < 0:
    raise ValueError("Age cannot be negative")



print("Custom Exceptions")
class InvalidAgeError(Exception):
    pass

age = 15

if age < 18:
    raise InvalidAgeError("Age must be 18 or above")