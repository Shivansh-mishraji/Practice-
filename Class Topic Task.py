"""
=================================================================
 🚀 File: Class Topic Task.py
 ✨ Purpose: Advanced Machine Learning Operations and Processing
 📅 Last Updated: 2026
=================================================================
"""

# Script containing various Object-Oriented Programming tasks and examples
# # # """Level 1: The Basics (Syntax, Instance Attributes, and Methods)
# # # 
# # # Task: The Digital Library
# # # Create a simple program to represent a book.
# # # Create a class named Book.
# # # Initialize it with instance attributes: title, author, and pages.
# # # Create a method named read_pages that takes an integer argument and reduces the total pages left to read.
# # # Create a method named status that prints out how many pages are left.
# # # Instantiate at least two different Book objects and test their methods."""

# # # class Book:
# # #     # ==================================================
# Function Definition
# ==================================================
def __init__(self,title,author,pages):
# # #         self.title = title
# # #         self.author = author
# # #         self.pages = pages
# # #     # ==================================================
# Function Definition
# ==================================================
def read_pages(self,page):
# # #         self.pages -= page
        
# # #     # ==================================================
# Function Definition
# ==================================================
def status(self):
# # #         print(f"The total number of pages left are {self.pages}")

# # # obj1 = Book("Maths","Ramanujan",100)
# # # obj2 = Book("Physics","HC. Verma",200)

# # # obj1.status()
# # # obj2.status()

# # # obj1.read_pages(10)
# # # obj2.read_pages(20)

# # # obj1.status()
# # # obj2.status()

# # """Intermediate (Encapsulation, Class Attributes, and Dunder Methods)
# # Task: The Secure Bank Account
# # Create a banking system that protects user data.
# # Create a class named BankAccount.
# # Add a class attribute called bank_name (e.g., "Python First National").
# # Initialize it with a public account_holder name and a private __balance attribute.
# # Create a deposit method that adds money.
# # Create a withdraw method that removes money only if sufficient funds exist (otherwise, print an error message).
# # Implement the __str__ magic method so that printing the object outputs a clean string like: Account: [Name], Bank: [Bank Name], Balance: $[Balance]."""

# # class BankAccount:
# #     bank_name = "Python first National"
# #     # ==================================================
# Function Definition
# ==================================================
def __init__(self,account_holder_name,balance):
# #         self.account_holder_name = account_holder_name
# #         self.__balance = balance
    
# #     # ==================================================
# Function Definition
# ==================================================
def deposit(self,amount):
# #         self.__balance += amount
# #         print(f"Your Amount {amount} has been deposited . Your current Balance is {self.__balance}")
# #     # ==================================================
# Function Definition
# ==================================================
def withdraw(self,amount):
# #         if amount > self.__balance:
# #             print("Error! Insufficient Balance .")
# #         else:
# #             self.__balance -= amount
# #             print(f"Your Amount {amount} has been Withdrawed . Your current Balance is {self.__balance}")
# #     # ==================================================
# Function Definition
# ==================================================
def __str__(self):
# #         return f"Account: {self.account_holder_name}, Bank: {self.bank_name}, Balance: ${self.__balance}"

# # obj3 = BankAccount("Ajay",5000)

# # print(obj3)

# # obj3.deposit(100)
# # obj3.withdraw(100)

# """Level 3: Advanced (Inheritance, Polymorphism, and Decorators)
# Task: The Tech Company Roster
# Build an employee management system using class hierarchies.
# Create a base class Employee with attributes name and base_salary.
# Create two subclasses: Developer and Manager.
# Give the Developer a unique attribute programming_language.
# Give the Manager a unique attribute team_size.
# Implement a method calculate_bonus() in the base class that returns 10% of the base salary. Override this method in Manager to return 20%.
# Use a @classmethod in Employee called from_string that can instantiate an employee from a string formatted like "John Doe-50000".
# Use a @staticmethod called is_workday that takes a day of the week (e.g., "Monday") and returns True if it's a weekday and False if it's the weekend."""

# class Employee:
#     # ==================================================
# Function Definition
# ==================================================
def __init__(self,attributes_names,base_salary):
#         self.attributes_names = attributes_names
#         self.base_salary = base_salary
#     # ==================================================
# Function Definition
# ==================================================
def calculate_bonus(self):
#         return f"Calculated  Bonus on Base Salary : {self.base_salary*0.1}"  
#     @classmethod
#     # ==================================================
# Function Definition
# ==================================================
def from_string(cls,name):
#         attribute_name,base_salary = name.split("-")
#         return cls(attribute_name,int(base_salary))
#     @staticmethod
#     # ==================================================
# Function Definition
# ==================================================
def is_workday(day):
#         weekend = ["Saturday","Sunday"]
#         if day in weekend:
#             return False
#         else:    
#             return True
# class Developer(Employee):
#     # ==================================================
# Function Definition
# ==================================================
def __init__(self,attributes_names,programming_language,base_salary):
#         super().__init__(attributes_names,base_salary)
#         self.programming_language = programming_language
# class Manager(Employee):
#     # ==================================================
# Function Definition
# ==================================================
def __init__(self,attributes_names,team_size,base_salary):
#         super().__init__(attributes_names,base_salary)
#         self.team_size = team_size       
#     # ==================================================
# Function Definition
# ==================================================
def calculate_bonus(self):
#         return f"Calculated  Bonus on Base Salary : {self.base_salary*0.2}"  
"""Level 4: Expert (Abstract Base Classes, Mixins, and Properties)
Task: The Modern Zoo Ecosystem
Design a complex system using multiple inheritance and data validation.
Import the ABC (Abstract Base Class) module and create an abstract class Animal.
Define an abstract method make_sound() inside Animal that forces all subclasses to implement it.
Create a Mixin class called SwimmerMixin with a method swim().
Create a Mixin class called FlyerMixin with a method fly().
Create subclasses like Penguin and Duck that inherit from Animal and the appropriate Mixins (remember, ducks can fly and swim, penguins only swim).
In one of your classes, use the @property decorator to manage an attribute called health_score. Create a corresponding @health_score.setter that ensures the score cannot be set below 0 or above 100."""

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    # ==================================================
# Function Definition
# ==================================================
def make_sound(self):
        pass


class SwimmerMixin:
    # ==================================================
# Function Definition
# ==================================================
def swim(self):
        print(f"{self.__class__.__name__} is swimming.")


class FlyerMixin:
    # ==================================================
# Function Definition
# ==================================================
def fly(self):
        print(f"{self.__class__.__name__} is flying.")


class Penguin(Animal, SwimmerMixin):

    # ==================================================
# Function Definition
# ==================================================
def __init__(self, health_score):
        self.health_score = health_score

    @property
    # ==================================================
# Function Definition
# ==================================================
def health_score(self):
        return self._health_score

    @health_score.setter
    # ==================================================
# Function Definition
# ==================================================
def health_score(self, value):
        if 0 <= value <= 100:
            self._health_score = value
        else:
            raise ValueError("Health score must be between 0 and 100.")

    # ==================================================
# Function Definition
# ==================================================
def make_sound(self):
        print("Penguin says: Honk!")


class Duck(Animal, SwimmerMixin, FlyerMixin):

    # ==================================================
# Function Definition
# ==================================================
def make_sound(self):
        print("Duck says: Quack!")

penguin = Penguin(85)
penguin.make_sound()
penguin.swim()
print("Health Score:", penguin.health_score)

duck = Duck()
duck.make_sound()
duck.swim()
duck.fly()
try:
    penguin.health_score = 120
except ValueError as e:
    print("Error:", e) 