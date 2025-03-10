# # TODO: Exercise 1 : Hello World -- Print the following output in one line of code: ´´Hello world Hello world  Hello world Hello world´´
# print("Hello world " * 4)
# NOTE: Hello world Hello world Hello world Hello world

# # TODO: Exercise 2: Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

# print((99**3)*8)
# NOTE: 7762392

# TODO: Exercise 3: What is the output ? A. 5 < 3, B. >>> 3 == 3, C. >>> 3 == "3", D. >>> "3" > 3, E. >>> "Hello" == "hello"
# # A.
# print(5 < 3)
# NOTE: False
# # B.
# print(3 == 3)
# NOTE: True
# # C.
# print(3 == "3")
# NOTE: False
# # D.
# print("3" > 3)
# NOTE: TypeError: '>' not supported between instances of 'str' and 'int'
# # E.
# print("Hello" == "hello")
# NOTE: False

# #TODO: Exercise 4 : Your computer brand -- 1. Create a variable called computer_brand which value is the brand name of your computer. 2. Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

# computer_brand = "Acer"
# print(f"I have a {computer_brand} computer.")
# NOTE: I have a Acer computer.

# #TODO: Exercise 5 : Your information -- Instructions: 1. Create a variable called name, and set it’s value to your name. 2. Create a variable called age, and set it’s value to your age. 3. Create a variable called shoe_size, and set it’s value to your shoe size. 4. Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3. 5. Have your code print the info message. 6. Run your code

# name = "Anna"
# age = 38
# shoe_size = 37
# info = f"My name is {name}, I am {age} years old since 1 week and my shoe size is {shoe_size}."
# print(info)
# NOTE: My name is Anna, I am 38 years old since 1 week and my shoe size is 37.

# #TODO: Exercise 6 : A & B Instructions: 1. Create two variables, a and b. 2. Each variable value should be a number. 3. If a is bigger then b, have your code print Hello World.

# a = 13
# b = 7
# if a > b:
# 	print("Hello World")
# NOTE: Hello World


# #TODO: Exercise 7 : Odd or Even -- Instructions: Write code that asks the user for a number and determines whether this number is odd (FR-impair) or even (FR-pair).

# choose_number = input("Choose a number: ")
# choose_number = int(choose_number)
# if choose_number % 2 == 0:
# 	print("This number is even (pair).")
# else:
# 	print("This number is odd (impair).")
# # option 1 # NOTE: Choose a number: 13
# # NOTE: This number is odd (impair).

# # option 2 #NOTE: Choose a number: 66
# # NOTE: This number is even (pair).

# #TODO: Exercise 8 : What’s your name ? -- Instructions: Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
# name = input("What's your name? ")
# if name == "Anna":
# 	print("WOW! It rhymes with banana.")
# else:
# 	print("He does not rhymes with mango.")

# option 1 # NOTE: What's your name? Anna
# NOTE: WOW! It rhymes with banana.

# option 2 #NOTE: What's your name? Guy
# NOTE: He does not rhymes with mango.


# #TODO: Exercise 9 : Tall enough to ride a roller coaster -- Instructions -- 1. Write code that will ask the user for their height in centimeters.	2. If they are over 145cm print a message that states they are tall enough to ride. 3. If they are not tall enough print a message that says they need to grow some more to ride.

# height = input("What is your height in centimeters? ")
# height = int(height)
# if height > 145:
# 	print("You are tall enough to ride.")
# else:
# 	print("You need to grow some more to ride, eat some soup!")
# # option 1 # NOTE: What is your height in centimeters? 150
# # NOTE: You are tall enough to ride.
# # option 2 # NOTE: What is your height in centimeters? 125
# # NOTE: You need to grow some more to ride, eat some soup!


