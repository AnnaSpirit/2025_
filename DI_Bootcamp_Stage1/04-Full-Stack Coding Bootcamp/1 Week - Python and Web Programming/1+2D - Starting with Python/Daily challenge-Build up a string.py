import random

# TODO: 
# Instructions: 
# 	1. Using the input function, ask the user for a string. The string must be 10 characters long.
# 		a. If it’s less than 10 characters, print a message which states “string not long enough”.
# 		b. If it’s more than 10 characters, print a message which states “string too long”.
# 		c. If 	it’s 10 characters, print a message which states “perfect string” and continue the exercise.

user_input = input("Please enter a string: ")
if len(user_input) < 10:
#HACK: len() - longueur de la chaine de caractere
	print("string not long enough")
elif len(user_input) > 10:
	print("string too long")
else:
	print("perfect string")

#INFO: How reload the user_input if it's not 10 characters long?
user_input = ""
while len(user_input) != 10:
	user_input = input("Please enter a string: ")
	if len(user_input) < 10:
	#HACK: len() - longueur de la chaine de caractere
		print("string not long enough")
	elif len(user_input) > 10:
		print("string too long")
	else:
		print("perfect string")

    # 2. Then, print the first and last characters of the given text. (The user enters "HelloWorld" Then you have to print: H, d)

print(user_input[0], user_input[-1])
#HACK: 0 - 1er caractere, -1 - dernier caractere
#HACK: OU  print(user_input[0] + ", " + user_input[-1])

    # 3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example: (The user enters "HelloWorld" Then, you have to construct the string character by character: H, He, Hel, ... , HelloWorld.

for i in range(len(user_input)):
	print(user_input[:i+1])
#HACK: range() - pour avoir une liste de 0 a la longueur de la chaine de caractere
#HACK: i+1 - pour que le dernier caractere soit inclus

    # 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example: Hlrolelwod

user_input = list(user_input)
random.shuffle(user_input)
print(''.join(user_input))
#HACK: list() - pour transformer la chaine de caractere en liste
#HACK: random.shuffle() - pour melanger les elements de la liste aleatoirement
#HACK: ''.join() - pour transformer la liste en chaine de caractere

#INFO: How to redo the shuffle 10 time for example?
for i in range(10):
	user_input = list(user_input)
	random.shuffle(user_input)
	print(''.join(user_input))