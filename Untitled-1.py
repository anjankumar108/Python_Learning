# x = 10
# y = "10"
# z = 10.0
# print(type(x), type(y), type(z))


# 1. `2name = "John"`  --invalid
# 2. `name_2 = "Alice"`  --valid
# 3. `_var = 100`  --valid
# 4. `my-variable = 5`  --invalid

# num = 25

# Convert to float
# float_num = float(num)
# print("Float:", float_num)

# Convert to string
# str_num = str(num)
# print("String:", str_num)

# number = float(input("Enter a number: "))  # Convert input to a float

# # Check if the number is positive, negative, or zero
# if number > 0:
#     print(f"{number} is positive.")  # This block runs if the condition is True
# elif number < 0:
#     print(f"{number} is negative.")  # This block runs if the previous condition is False and this one is True
# else:
#     print(f"{number} is zero.")      # This block runs if all previous conditions are False


# fruits = ["apple", "banana", "cherry"]
# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# for i in range(1, 11):
#     print(f"The square of {i} is {i**2}")


# movies = ["Inception", "The Matrix", "Interstellar", "Parasite"]

# for index, movie in enumerate(movies):
#     print(f"Movie {index + 1}: {movie}")

# age: int = 30
# height: float = 5.9
# name: str = "Alice"
# is_student: bool = True

#mutable -- List, Dict, Set
#immutable -- Tuple, String, Frozenset

# my_list = [1, 2, 3]
# my_list.append(4)          # Modifying the list
# print(my_list)             # Output: [1, 2, 3, 4]

# my_dict = {'a': 1, 'b': 2}
# my_dict['c'] = 3           # Adding a new key-value pair
# print(my_dict)             # Output: {'a': 1, 'b': 2, 'c': 3}

# my_set = {1, 2, 3}
# my_set.add(4)              # Adding an element to the set
# print(my_set)              # Output: {1, 2, 3, 4}

# my_tuple = (1, 2, 3)
# try:
#     my_tuple[1] = 4        # This will raise an error
# except TypeError as e:
#     print(e)               # Output: 'tuple' object does not support item assignment

# my_string = "Hello"
# new_string = my_string.replace("H", "J")  # Creates a new string
# print(my_string)                # Output: Hello
# print(new_string)               # Output: Jello

# my_frozenset = frozenset([1, 2, 3])
# try:
#     my_frozenset.add(4)       # This will raise an error
# except AttributeError as e:
#     print(e)                  # Output: 'frozenset' object has no attribute 'add'

# number = 0

# for i in range(1, 6):
#     if i == 3:
#         continue  # Skip the number 3
#     print(i)

# while number < 10:
#     number += 1
#     if number == 5:
#         print("Number is 5, exiting the loop.")
#         break  # Exit the loop when the number is 5
#     if number % 2 == 0:
#         continue  # Skip even numbers
#     print(f"Odd number: {number}")


# import random

# def number_guessing_game():
#     print("Welcome to the number guessing game")
    
#     target_number = random.randint(1, 100)
#     attempts = 0
    
#     while True:
#         try:
#             guess = int(input("take a guess"))
#             attempts +=1
            
#             if guess <  target_number:
#                 print ("Too low, try again")
#             elif guess > target_number:
#                 print("Too high, try again")
#             else:
#                 print("congragulations, you guessed correctly")
#                 break
#         except ValueError:
#             print("enter a valid number")
#             playagain= input ("Do you want to play again?").strip().lower()
#             if playagain !='yes':
#                 print("Thank you for playing")
#                 break

# #run the game
# number_guessing_game()


# def introduce(name,age=25):
#     print(f"Hello, my name is {name} and age is {age} years old. ")

# introduce("anjan")
# introduce("anjan",32)

# def calculate_discount(*args, discount=0):
#     total = sum(args)
    
#     total_after_discount = total - (total*discount/100)
    
#     return total_after_discount

# total1 = calculate_discount(100,20,10)
# print(f"{total1} after discount")

# total2 = calculate_discount(100,20,10,discount=10)
# print(f"{total2} after discount")

# def greet(name="anjan",message="welcome"):
#     print(f"{message} {name}")
    
# greet()
# greet("alice")
# greet("alice",'welcome')

# def logger(func):
#     def wrapper(*args,**kargs):
#         print("function is being executed")
#         return(func(*args,**kargs))
#     return wrapper

# @logger
# def say_hello():
#     print("hello world")
    
# say_hello()
     
# import time    
           
# def time_logger(func):
#     def wrapper(*args,**kargs):
#         start_time = time.time()
#         result = func(*args,**kargs)
#         end_time = time.time()
#         execution_time = end_time-start_time
#         print(f"{execution_time}")
#         return(result)
#     return wrapper
           
# @time_logger   
# def spend_time():
#     time.sleep(2)
#     print("function finished")
    
# spend_time()

# square = lambda x:x**2
# print(square(4))

# Automatic File Categorization
# Duplicate Detection & Handling
# User-Friendly Interface & Logging
# Real-Time Folder Monitoring
# restore file movement

# libraries :
# CLI Interaction -- argparse --handles command line arguments
# file operations -- shutil, os  --move, copy, delete files
# real time monitoring --watchdog
# file type detection --mimetypes
# Logging --logging
# GUI --Pyqt, TKinter

# challenges --solutions 
# handling duplicate files -- naming conventions 
# unknown ext files -- go through content and identify
# permission & access issues -- ask admin access or exception lists 

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
            
#     def display_info(self):
#          print(f"{self.brand}")   
#          print(f"{self.model}")
#          print(f"{self.year}")
         
#     def start_engine(self):
#          print("Engine Started")
         
# my_car = Car("Toyota","Mini",2022)

# my_car.display_info()

# my_car.start_engine()
 
# class BankAccount:
#     bank_name = "Anjan Bank"
    
#     def __init__(self,account_name,balance):
#         self.account_name = account_name
#         self.balance = balance
        
#     def display_info(self):
#          print("self.account_name")
#          print("self.balance")
    
#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"deposit successfull balance is {self.balance}")
#         elif amount <0:
#             print("entered amout is negative")
            
#     def withdraw(self,amount):
#         if 0 < amount < self.balance:
#             self.balance -=amount
#             print(f"withdrawl successfull, balance is {self.balance}")
#         elif amount < 0:
#             print("entered amount is negative")
#         else:
#             print("insufficient funds") 
    
# account = BankAccount("Anjan", 1000)
# account.deposit(500)
# account.withdraw(500)
        
# Define the BankAccount class
# class BankAccount:
#     # Class variable
#     bank_name = "XYZ Bank"
#     total_accounts = 0  # to keep track of total accounts

#     # Constructor to initialize account_holder and balance
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#         BankAccount.total_accounts += 1  # increment total accounts

#     # Method to display account information
#     def display_info(self):
#         print(f"Bank Name: {self.bank_name}")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: ${self.balance}")
#         print(f"Total Accounts: {self.total_accounts}")


# # Create multiple objects of BankAccount
# account1 = BankAccount("John Doe", 1000)
# account2 = BankAccount("Jane Doe", 500)
# account3 = BankAccount("Bob Smith", 2000)

# # Display account information for each account
# print("Account 1 Information:")
# account1.display_info()

# print("\nAccount 2 Information:")
# account2.display_info()

# print("\nAccount 3 Information:")
# account3.display_info()

# # Modify the class variable bank_name for all accounts
# BankAccount.bank_name = "ABC Bank"

# print("\nAfter modifying class variable bank_name:")
# print("Account 1 Information:")
# account1.display_info()

# print("\nAccount 2 Information:")
# account2.display_info()

# print("\nAccount 3 Information:")
# account3.display_info()

# # Modify the instance variable account_holder for account1
# account1.account_holder = "John Smith"

# print("\nAfter modifying instance variable account_holder for account1:")
# print("Account 1 Information:")
# account1.display_info()

# print("\nAccount 2 Information:")
# account2.display_info()

# print("\nAccount 3 Information:")
# account3.display_info()    
            
            
# # Define the Animal parent class
# class Animal:
#     # Method to make a sound
#     def speak(self):
#         print("Animal makes a sound")


# # Define child classes that inherit from Animal
# class Dog(Animal):
#     # Override the speak method to make a dog-specific sound
#     def speak(self):
#         print("Dog barks")


# class Cat(Animal):
#     # Override the speak method to make a cat-specific sound
#     def speak(self):
#         print("Cat meows")


# class Bird(Animal):
#     # Override the speak method to make a bird-specific sound
#     def speak(self):
#         print("Bird chirps")


# # Create objects of the child classes
# dog = Dog()
# cat = Cat()
# bird = Bird()

# # Call the speak method on each object
# print("Dog:")
# dog.speak()

# print("\nCat:")
# cat.speak()

# print("\nBird:")
# bird.speak()

# print("\nParent class Animal:")
# animal = Animal()
# animal.speak()            
        

# Define the Person class
# class Person:
#     # Constructor to initialize name and age
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Define the Student class inheriting from Person
# class Student(Person):
#     # Constructor to initialize name, age, and grade
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)  # Call Person's constructor
#         self.grade = grade

#     # Method to introduce the student
#     def introduce(self):
#         print(f"Hi, I am {self.name}, {self.age} years old, and I am in grade {self.grade}")


# # Create an object of Student
# student = Student("John Doe", 16, 11)

# # Call the introduce method
# student.introduce()
            

# Define the Teacher class
# class Teacher:
#     # Constructor to initialize subject
#     def __init__(self, subject):
#         self.subject = subject

#     # Method to teach the subject
#     def teach(self):
#         print(f"Teaching {self.subject}")


# # Define the Athlete class
# class Athlete:
#     # Constructor to initialize sport
#     def __init__(self, sport):
#         self.sport = sport

#     # Method to play the sport
#     def play(self):
#         print(f"Playing {self.sport}")


# # Define the SportsTeacher class inheriting from both Teacher and Athlete
# class SportsTeacher(Teacher, Athlete):
#     # Constructor to initialize subject and sport
#     def __init__(self, subject, sport):
#         Teacher.__init__(self, subject)  # Call Teacher's constructor
#         Athlete.__init__(self, sport)  # Call Athlete's constructor


# # Create an object of SportsTeacher
# sports_teacher = SportsTeacher("Physical Education", "Football")

# # Call methods from both parents
# print("Teaching:")
# sports_teacher.teach()

# print("\nPlaying:")
# sports_teacher.play()
        
# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def speak(self):
#         return super().speak() + " - Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# animals = [Animal(), Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())

# def multiply_output(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#     return wrapper

# @multiply_output
# def add_numbers(a, b):
#     return a + b

# print(add_numbers(5, 3))
# print(add_numbers(2, 2))


# class Counter:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         self.start += 1
#         return self.start - 1

# c = Counter(1, 4)
# for i in c:
#     print(i, end=" ")


# class MyContext:
#     def __enter__(self):
#         print("Entering context")
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context")
    
#     def hello(self):
#         print("Inside context")

# with MyContext() as ctx:
#     ctx.hello()

# class A:
#     def method(self):
#         return "A"
    
# a = A()
# print(a.method())    

# class B(A):
#     def method(self):
#         return "B" + super().method()

# b = B()
# print(b.method())    

# class C(A):
#     def method(self):
#         return "C" + super().method()
 
# c = C()
# print(c.method())
   
# class D(B, C):
#     def method(self):
#         return "D" + super().method()

# d = D()
# print(d.method())

# d = D()
# print(d.method())

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#         0 1
#         1 1
#         1 2
#         2 3

# gen = fibonacci(4)
# print(list(gen))
# print(list(gen))



# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print(f"result is {result}")
#     finally:
#         print("executing finally clause")

# divide(2, 1)
# divide(2, 0)


# class MetaClass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['new_attribute'] = 'Added by metaclass'
#         return super().__new__(cls, name, bases, attrs)

# class MyClass(metaclass=MetaClass):
#     pass

# obj = MyClass()
# print(obj.new_attribute)


# numbers = [1, 2, 3, 4, 5]
# squared = [(lambda x: x**2)(x) for x in numbers if x % 2 == 0]
# print(squared)

# func = lambda x: [i for i in range(x) if i % 2 == 0]
# print(func(5))


# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius

#     @property
#     def fahrenheit(self):
#         return self._celsius * 9/5 + 32

#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self._celsius = (value - 32) * 5/9

# temp = Temperature(25)
# print(temp.fahrenheit)
# temp.fahrenheit = 77
# print(temp._celsius)


# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print([fibonacci(i) for i in range(7)])
# print(fibonacci.cache_info())


# import asyncio

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     return what

# async def main():
#     print("started")
#     print(await say_after(0, "hello"))
#     print(await say_after(0, "world"))
#     print("finished")

# asyncio.run(main())