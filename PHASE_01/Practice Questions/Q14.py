print("----Oops----")

print("1.class and object")
class Student:

    name = "Amir"
    age = 20
    branch = "AI/ML"

student1 = Student()
print(student1.age)
print(student1.branch)
print(student1.name)



print("\n\n2.Constructor — init()")
class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

student1 = Student("Amir", 20, "AI/ML")

print(student1.name)
print(student1.age)
print(student1.branch)




print("\n\n3.Understanding self")
class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s1 = Student("Amir")
s1.show()

print("\n\nAttributes and Methods")
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

s1 = Student("Amir", 90)

s1.display()
s1.check_result()


print("\n\nFour Pillars of OOP")
print("Pillar 1: Encapsulation")
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())


print("\nPillar 2: Inheritance")
class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

d = Dog()

d.eat()
d.bark()

print("\nTypes of inheritance:")
print("\nA.Single inheritance:")
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

obj = B()
obj.show()
 

print("\nB.Multiple inheritance:")
class Father:
    def skill1(self):
        print("Programming")

class Mother:
    def skill2(self):
        print("Communication")

class Child(Father, Mother):
    pass

obj = Child()

obj.skill1()
obj.skill2()

print("\nC.Multilevel inheritance:")
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print("super() Function")
#super() allows a child class to access methods of its parent class according to Python's method resolution order.
class Animal:

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Tommy", "Labrador")

print(dog.name)
print(dog.breed)

print("\nPillar 3: Polymorphism")
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())

print("\nA.Method overriding:")
class Animal:

    def sound(self):
        print("Animal sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()

print("\nB.Operator overloading:")
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a + b)

print("\nPillar 4: Abstraction")
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)

print(c.area())

print("\n\nTypes of Methods")
print("\n1. Instance Method")
class Student:

    def show(self):
        print("Instance method")

s = Student()
s.show()

print("\n2. Class Method")
class Student:

    college = "ABC College"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()

print("\n3. Static Method")
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))


print("\n\nProperty Decorator")
class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Invalid marks")

s = Student(90)

print(s.marks)

s.marks = 95
print(s.marks)

"""Magic / Dunder Methods
Special methods with double underscores.
Method	Purpose
__init__()	Initialize object
__str__()	Human-readable string
__repr__()	Developer-oriented representation
__len__()	Length behavior
__add__()	Addition behavior
__eq__()	Equality behavior
__call__()	Make an object callable
__iter__()	Iterator behavior
__next__()	Next iterator value"""

print("\n\nMagic/Dunder Methods")
#Special methods with double underscores.
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

s = Student("Amir")

print(s)

print("\n\nComposition")
#Composition is a design technique in which one class contains an object of another class to build complex functionality.
class Engine:

    def start(self):
        print("Engine started")

class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")

car = Car()
car.start_car()