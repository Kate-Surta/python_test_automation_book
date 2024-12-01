# [TI] What are the four main principles (pillars) of Object-Oriented Programming (name and explain)?
# The core principles of OOP are:
#
# Encapsulation (Encapsulation means keeping data (attributes) and the methods that work on that data together in one place (a class).)
# Abstraction (Abstraction involves simplifying complex systems by modeling classes that represent real-world entities while hiding unnecessary details. By defining a class, we focus only on the attributes and behaviors that are relevant to the program, leaving out irrelevant complexities)
# Inheritance (Inheritance allows a class (child) to inherit attributes and methods from another class (parent).)
# Polymorphism (Polymorphism in Python allows objects of different classes to be treated as objects of a common super class. The most common use of polymorphism is when a parent class reference is used to refer to a child class object. )
#
# Write a TestCase class with methods for setup(), run(), and teardown(). Create objects of the TestCase class to represent individual test cases.

class BaseTest:
    def setup(self):
        print("Setting up the test")

    def teardown(self):
        print("Cleaning up the test")

    def run(self):
        print("Run the test")


test = BaseTest()
test.setup()
test.run()
test.teardown()


# Investigate what the Diamond Problem is in the context of multiple inheritance in OOP. How can you mitigate this problem in your designs?
# The Diamond Problem in the context of object-oriented programming (OOP) and multiple inheritance occurs when a class inherits from two classes that both inherit from a single base class. This creates a "diamond" shape in the inheritance diagram, leading to ambiguity.
# - Instead of using multiple inheritance, consider using interfaces or abstract base classes to define common behavior that needs to be implemented by derived classes.
# - Favor composition over inheritance. This means creating classes that contain instances of other classes, rather than inheriting from them.
# - If you must use multiple inheritance, you can explicitly call methods from the desired parent class using the super() function in a specific order, relying on Python's MRO for guidance.
# - Use mixins for shared functionality. Mixins are small classes that provide methods to other classes. They are not intended to stand alone but rather to be included as part of multiple inheritance.

# Implement method overriding in a test automation context. Override a method in the child test class to customize the test execution
class TestCase:
    def run_test(self):
        print("Running test case...")


class IntegrationTest(TestCase):
    def run_test(self):
        print("Running integration test...")


# Create a multiple inheritance example:
# Write a class that inherits from multiple parent classes (e.g., BaseTest and a custom mixin class),
# and check how MRO impacts method calls.

class Animal:
    def do_something(self):
        print("Animal behavior")


class Canine(Animal):
    def do_something(self):
        print("Canine behavior")
        super().do_something()  # Calls Animal's method


class Pet(Animal):
    def do_something(self):
        print("Pet behavior")
        super().do_something()  # Calls Animal's method


class Dog(Canine, Pet):
    def do_something(self):
        print("Dog behavior")
        super().do_something()  # Calls the next class in the MRO (Canine)


# Create an instance of Dog
dog = Dog()
dog.do_something()


# output:
# Dog behavior
# Canine behavior
# Pet behavior
# Animal behavior

# OR

class BaseTest:
    def setup(self):
        print("Setting up the test")

    def teardown(self):
        print("Cleaning up the test")


class SetupMixin:
    def setup(self):
        print("Setting up common tasks")


class LoginTest(SetupMixin, BaseTest):
    def run(self):
        print("Running login test")


test = LoginTest()
test.setup()
test.run()
test.teardown()


# Output:
# Setting up common tasks
# Running login test
# Cleaning up the test


# What are @classmethod and @staticmethod and their main differences?

# Class methods are methods that are called on the class itself,
# not on a specific object instance. Therefore, it belongs to a class level,
# and all class instances share a class method. To define a class method,
# you should use the @classmethod decorator and it takes cls (the class itself)
# as its first parameter. Use @classmethod when you need to access or modify class-level data
# (class variables) or when you want to define a factory method that returns an instance of the class.

# Static methods are defined using the @staticmethod decorator.
# They don't require an instance of the class to be called and don't have access to self or cls.
# Static methods can be used when some processing related to the
# class needs to be done but does not require access to any class or instance variables.

class X:
    def call(self):
        print("Calling from X")


class Y(X):
    def call(self):
        print("Calling from Y")


class Z(X):
    def call(self):
        print("Calling from Z")


class W(Y, Z):
    def call(self):
        super().call()


w = W()
print(W.mro())
w.call()

# Output:
# [<class '__main__.W'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.X'>, <class 'object'>]
# Calling from Y
