# #TODO: Given this list:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
# Hint : Look at the index method

list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)
#NOTE: [5, 10, 15, 200, 25, 50, 20]
#NOTE: The first occurrence of 20 is replaced by 200

# HACK:Why only the first 20 has been changed to 200?
# The index() method returns the index of the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.

#TODO: Unpack the following tuple into 4 : a_tuple = (10, 20, 30, 40)
a_tuple = (10, 20, 30, 40)
a= a_tuple[0]
b= a_tuple[1]
c= a_tuple[2]
d= a_tuple[3]
print(a, b, c, d)
#NOTE: 10 20 30 40

# #solution by GPT
# a, b, c, d = a_tuple
# print(a, b, c, d)
# #NOTE: 10 20 30 40

# TODO: Accept a number from the user and print its multiplication table

number = int(input("Enter a number: "))
for i in range(1, 11):
	print(f"{number} x {i} = {number * i}")
#NOTE: Enter a number: 5
#NOTE: 5 x 1 = 5
#NOTE: 5 x 2 = 10 ...
#NOTE: 5 x 10 = 50


#TODO: Print the numbers from 1 to 10 using while loop

n = 1
while n <= 10: 
	print(n)
	n += 1
#NOTE: 1 2 3 4 5 6 7 8 9 10

#TODO: infinite loop & Flag
# while 1 == 1:
#     print("Looping...")

active = True   
#NOTE: see Memo_Truthy_Falsy_Python.docx
while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)
print("Goodbye !")

# TODO: Example with password

password = ""
while password != "hello-world-123":
		password = input("Enter the top secret password: ")
# HACK: how to add a print("Access granted!") before the loop end?
print("Access granted!")
#NOTE: Enter the top secret password: munchkins
#NOTE: Enter the top secret password: read more books
#NOTE: Enter the top secret password: hello-world-123
#NOTE: Access granted!

#TODO: Break

while True: 
    city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
    if city == 'quit':
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")
#NOTE: Please enter the name of a city you have visited (enter 'quit'  when you are finished): Paris
#NOTE: I'd love to go to Paris
#NOTE: Please enter the name of a city you have visited (enter 'quit'  when you are finished): Malaga
#NOTE: I'd love to go to Malaga
#NOTE: Please enter the name of a city you have visited (enter 'quit'  when you are finished): quit
#NOTE: Goodbye !

#TODO: Continue

current_number = 0
while current_number <= 10:
    current_number += 1
    if 3 < current_number < 7: # If the number is between 3 and 7 
        continue                # Go back to the beginning of the loop
    print(current_number)
#NOTE: 1 2 3 7 8 9 10 11