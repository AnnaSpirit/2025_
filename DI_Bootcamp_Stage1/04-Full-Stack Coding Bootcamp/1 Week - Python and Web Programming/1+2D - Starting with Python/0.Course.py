# #NOTE: This comment is fo result of the code below
# #INFO: Statement of exercise

# HACK: BASIC VALUE TYPES

# # INFO:The type() function returns the type of the object placed in between the parentheses, for example:

# dir (42) 
# #NOTE:The result will be a list of all the methods that can be used with the object 42
# #['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# # type(42)
# # NOTE:the type of the object will be displayed as <class 'int'>
# a = 42 
# # NOTE:Type : <class 'int'>
# type(a)

# #INFO:Let's try to type a decimal
# type(3.14)
# #NOTE:Type : <class 'float'>
# b = 3.14
# type(b)
# #NOTE:Type : <class 'float'>

# #INFO: If you were to type a bit of text

# type("Hello World")
# #NOTE: The result will be <class 'str'>

# hello = "Hello World"
# type(hello)
# #NOTE:Type : <class 'str'>

# # INFO: String syntax; between "" or '', functions: .capitalize, .upper, .lower, .replace
# print('hello'.capitalize()) 
# #NOTE: 'Hello'
# print('hello'.upper()) 
# #NOTE:'HELLO'
# print('HELLO'.lower())
# #NOTE: 'hello'
# print('hello'.replace('hello', 'goodnight'))
# #NOTE: 'goodnight'

# #TODO: EXERCICE: Strings - Syntax & Functions
# description = "strings are..."
# print(description.upper())
# #NOTE: 'STRINGS ARE...'
# print(description.replace ("are", "is"))
# #NOTE: 'strings is...'
# print(description.replace ("are", ""))
# #NOTE: 'strings ...'

# #TODO: EXERCICE: Number - Syntax & Operation -- !!In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years!!
# my_age = int(38)
# print(my_age + 123879)
# #NOTE: 123917

# #TODO: EXERCICE: Type Casting -- !!Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:!!
# bank_balance = '33000'
# phone_number = 0532287514

# print(type(bank_balance))
# #NOTE: <class 'str'>
# print(int(bank_balance))
# #NOTE: 33000
# print(type(phone_number))
# #NOTE: <class 'int'>
# print(str(phone_number))
# #NOTE: 0532287514

# #TODO: EXERCICE: Adding data types together --!!In the python shell, Create a variable called first_name and a variable called last_name, and then print your full name using those two variables.!!
# first_name = "Anna"
# last_name = "LEVY"
# print(first_name + " " + last_name) 
# # or
# print(first_name, last_name)

# #TODO: EXERCICE: Given the following values: ´´´x = 5 y = 10 z = 0 word1 = "hello" word2 = "world"´´´
# # 1. Check if x is less than y and y is greater than z. 2. Verify if word1 is not equal to word2. 3. Use the bool() function to check the boolean value of z and word1.
# x = 5
# y = 10
# z = 0
# word1 = "hello"
# word2 = "world"
# #1. 
# print(x < y and y > z)
# #NOTE: True
# #2.
# print(word1 != word2)
# #NOTE: True
# #3.
# print(bool(z))
# #NOTE: False
# print(bool(word1))
# #NOTE: True

# HACK: VARIABLES  --  variable_name = "variable value",

# #TODO: EXERCICE1 : Syntax, Declaration, name, display, increment, string format (f-strings) -- You have a friend named Alice, and you want to send her a message with the following details: ´´Name: Alice, Age: 30, City: New York, 1. Use f-strings to print a message saying: "Hello, Alice! You are 30 years old and live in New York." 2. Use str.format() to print the same message.´´

# Name = "Alice"
# Age = "30"
# City = "New York"
# #1.
# print(f"Hello, {Name}! You are {Age} years old and live in {City}.")
# #NOTE: Hello, Alice! You are 30 years old and live in New York.
# #2.
# print("Hello, {}! You are {} years old and live in {}.".format(Name, Age, City))
# #NOTE: Hello, Alice! You are 30 years old and live in New York.

# #TODO: EXERCICE 2: -- Ask the user for their age using the input() function and store it in a variable age. 1. Convert the inputted age into an integer and calculate the number of years until they turn 100. 2. Display a message: "You will turn 100 in X years", where X is the number of years calculated.

# age = input("How old are you? ")
# age = int(age)
# years_until_100 = 100 - age
# print(f"You will turn 100 in {years_until_100} years.")

# # #NOTE: How old are you? 38
# # #NOTE: You will turn 100 in 62 years.

# #TODO: EXERCICE 3: Analyze the code ´´age = input("How old are you? ") print(f"You are {age} years old")'' and predict what the outcome will be. Check the results in your python shell.

# age = input("How old are you? ")
# #NOTE: How old are you? 38
# print(f"You are {age} years old")
# #NOTE: You are 38 years old

#HACK: CONDITIONALS

# #TODO: EXERCICE: if statements -- 1. ask the user to enter his/her name 2. use the len() function to check the lenght of the name. if it is less than 5 letter print('You have a short name :)')

# name = input("What is your name? ")
# if len(name) < 5:
# 	print("You have a short name :)")
# #NOTE: What is your name? Anna
# #NOTE: You have a short name :)

# #TODO: EXERCICE: elif, else statement, in, not -- 1. Ask the user for a number between 1 and 100. 2. If the number is a multiple of three, print Fizz. 3. If the number is a multiple of five, print Buzz. 4. If the number is a multiple of both three and five, print FizzBuzz instead.

# number = int(input("Enter a number between 1 and 100: "))
# if number % 3 == 0 and number % 5 == 0:
# # INFO: if number % 15 == 0:
# 	print("FizzBuzz15")
# elif number % 3 == 0:
# 	print("Fizz3")
# elif number % 5 == 0:
# 	print("Buzz5")
# else:
# 	print(number)
# # #NOTE: Enter a number between 1 and 100: 15
# # #NOTE: FizzBuzz
# # #NOTE: Enter a number between 1 and 100: 48
# # #NOTE: Fizz