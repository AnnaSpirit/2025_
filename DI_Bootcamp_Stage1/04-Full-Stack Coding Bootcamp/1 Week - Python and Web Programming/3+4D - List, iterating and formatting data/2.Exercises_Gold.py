#TODO: Exercise 1: Concatenate lists--Instructions-- Write code that concatenates two lists together without using the + sign.

# list1 = [10, 15, 20, 25, 30]
# list2 = [1, 2, 3]
# res = list1 + list2
# print("Concatenated list:\n" + str(res))

# list1 = [33, 66, 99, 1111, 2222]
# list2 = [42, 52, 62]
# list1.extend(list2)
# #HACK: on etend la liste 1 avec la 2, elle garde le nom de liste 1
# print(list1)

#TODO: Exercise 2: Range of numbers --Instructions-- Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

nuum1 = 0
for element in range(1500, 2500):
    if element % 5 == 0:
        num1 = nuum1 + element
print(num1)

nuum2 = 0
for element in range(1500, 2500):
    if element % 7 == 0:
        num2 = nuum2 + element
print(num2)

print(num1 + num2)

#TODO: Exercise 3: Check the index --Instructions-- Using this variable names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']. Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name. Example: if input is 'Cortana' we should be printing the index 1

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# user_name = input("Please, what is your name?\n")

# # Check if the name is in the list.
# if user_name in names:
#     first_index = names.index(user_name)
#     print(f"The index of the first occurrence of {user_name} is {first_index}.")
# else:
#     print(f"{user_name} is not in the list.")

#TODO: Exercise 4: Greatest Number --Instructions--1. Ask the user for 3 numbers and print the greatest number. Exemple: Input the 1st number: 25, Input the 2nd number: 78, Input the 3rd number: 87 => The greatest number is: 87

# ThreeNumb = input("Input 3 numbers, separated by a space\n")
# ThreeNumb = ThreeNumb.split(" ")

# #HACK: Find the greatest number using max()
# ThreeNumb_L = [int(numB) for numB in ThreeNumb]
# greatest = max(ThreeNumb_L)

# print("The greatest number is:", greatest)

#TODO: Exercise 5: The Alphabet--Instructions-- 1. Create a string of all the letters in the alphabet. 2. Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# vowels = "aeiouy"

# for letter in alphabet:
#     if letter in vowels:
#         print(f"{letter.upper()} is a vowel.")
#     else:
#         print(f"{letter} is a consonant.")


#TODO: Exercise 6: Words and letters--Instructions-- 1.Ask a user for 7 words, store them in a list named words. 2.Ask the user for a single character, store it in a variable called letter. 3.Loop through the words list and print the index of the first appearance of the letter variable in each word of the list. 4. If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

#HACK: Collecting Words: We use a loop to prompt the user 7 times, storing each input in the list words
# words = []
# for i in range(7):
#     word = input(f"Enter word {i+1}: ")
#     words.append(word)
# #2. 
# letter = input("Enter a single character: ")

# #HACK: For each word, the find() method searches for the letter. If found, it prints the first index. Otherwise, it prints a message stating that the letter is not in the word.
# #3. 
# for word in words:
#     index = word.find(letter)  #HACK: .find() returns -1 if the letter is not found
#     if index != -1:
#         print(f"In word '{word}', the letter '{letter}' appears first at index {index}.")
#     else:
# # 4.
#         print(f"Letter '{letter}' does not exist in word '{word}'.")

# #TODO: +++ Count the occurence of 'letter'in 'words'
# for word in words:
#     occurrences = word.count(letter)
#     if occurrences > 0:
#         print(f"Dans le mot '{word}', le caractère '{letter}' apparaît {occurrences} fois.")

#TODO: Exercise 7: Min, Max, Sum --Instructions-- 1. Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. 2. Use the sum() function to see how quickly Python can add a million numbers.

# 1. 
#NOTE: Sum of all number from 1 to 1 000 000 is 500000500000

#TODO: Exercise 8 : List and Tuple--Instructions-- 1. Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number. EX: Suppose the following input is supplied to the program: 34,67,55,33,12,98, Then, the output should be: ['34', '67', '55', '33', '12', '98'] then ('34', '67', '55', '33', '12', '98')

# 1.
# values = input("Enter comma-separated numbers: ")

# # Generate a list
# list_numbers = values.split(',')

# # Generate a tuple
# tuple_numbers = tuple(list_numbers)

# #NOTE: list entre {}
# print("List:", list_numbers)

# # #TODO: Sort the liste but keep both???
# # list_numbers_sort = list_numbers.sort()
# # print("List ordorred:", list_numbers_sort)

# #NOTE: Tuple entre ()
# print("Tuple:", tuple_numbers)


#TODO: Exercise 9 : Random number--Instructions-- 1. Ask the user to input a number from 1 to 9 (including). 2.Get a random number between 1 and 9. Hint: random module. 3.If the user guesses the correct number print a message that says Winner. 4.If the user guesses the wrong number print a message that says better luck next time. 5. Bonus: use a loop that allows the user to keep guessing until they want to quit. 6. Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

games_won = 0
games_lost = 0

while True:
# 1.
    user_input = input("Enter a number from 1 to 9 (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break

# Validate the user input
    if not user_input.isdigit() or not (1 <= int(user_input) <= 9):
        print("Please enter a valid number between 1 and 9.")
        continue
    
    user_number = int(user_input)
    
    # 2. Get a random number between 1 and 9.
    random_number = random.randint(1, 9)
    #NOTE: Ramdom (1 to 9, no 1 to 10 as for index, right?)
    # 3. Check right number.
    if user_number == random_number:
        print("Winner!")
        games_won += 1
    else:
        # 4. Check wrong number.
        print(f"Better luck next time! The random number was {random_number}.")
        games_lost += 1

# 6. Total games won and lost.
print("\nGame over!")
print(f"Total games won: {games_won} and Total games lost: {games_lost}")
