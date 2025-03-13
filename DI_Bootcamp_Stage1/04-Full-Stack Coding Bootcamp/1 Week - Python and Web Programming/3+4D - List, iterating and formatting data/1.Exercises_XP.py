#TODO: Exercise 1 : Favorite Numbers -- Instructions -- 1. Create a set called my_fav_numbers with all your favorites numbers. 2. Add two new numbers to the set. 3. Remove the last number. 4.Create a set called friend_fav_numbers with your friend’s favorites numbers. 5. Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers = set({13, 9, 555, 666})
# print(my_fav_numbers)
# #NOTE: {9, 666, 555, 13}
# my_fav_numbers.add("589")
# my_fav_numbers.add("991")
# print(my_fav_numbers)
# #NOTE: {'589', '991', 9, 555, 13, 666}
# #NOTE: Delete the last number: impossible because it is a set
# friend_fav_numbers = set({78, 96, 5412, 6589, 687})
# print(friend_fav_numbers)
# #NOTE: {96, 5412, 6589, 78, 687}
# #NOTE:Concatenate the last number: impossible because it is a set
# friend_fav_list = list(friend_fav_numbers)
# list_fav_numbers = list(my_fav_numbers)
# our_fav_numbers = list_fav_numbers + friend_fav_list
# print(our_fav_numbers)
#NOTE:['589', '991', 9, 555, 13, 666, 96, 5412, 6589, 78, 687]

#TODO: Exercise 2: Tuple -- Instructions -- Given a tuple which value is integers, is it possible to add more integers to the tuple?

# tuple_A = (88, 99, 1111)
# print(tuple_A)
# #NOTE: No,  Tuple is immutable.

#TODO: Exercise 3: List -- Instructions -- 1. Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"]; 2. Remove “Banana” from the list. 3. Remove “Blueberries” from the list. 4. Add “Kiwi” to the end of the list. 5. Add “Apples” to the beginning of the list. 6. Count how many apples are in the basket. 7. Empty the basket. 8. Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)
# #NOTE: ['Banana', 'Apples', 'Oranges', 'Blueberries']
# basket.remove("Banana")
# print(basket)
# #NOTE: ['Apples', 'Oranges', 'Blueberries']
# basket.remove("Blueberries")
# print(basket)
# #NOTE: ['Apples', 'Oranges']
# basket.append("Kiwi")
# print(basket)
# #NOTE: ['Apples', 'Oranges', 'Kiwi']
# basket.insert(0, "Apples")
# print(basket)
# #NOTE: ['Apples', 'Oranges', 'Kiwi']
# appels = basket.count("Apples")
# print(appels)
# #NOTE: 2
# basket.clear()
# print(basket)
# #NOTE: []

#TODO: Exercise 4: Floats -- Instructions -- 1. Recap – What is a float? What is the difference between an integer and a float? 2. Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence). 3. Can you think of another way to generate a sequence of floats?

#NOTE: 1. Float is decimal number, integer is a whole number or digit
# seq_list= [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5] #What does it means "don't hard code the sequence"?
#NOTE: 2. The Python range() works only with integers. It doesn’t support the float type or with "numpy module"

#TODO: Exercise 5: For Loop -- Instructions -- 1. Use a for loop to print all numbers from 1 to 20, inclusive. 2. Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# numbers = range(1, 21)
# for num in numbers:
#	 print(num)
#NOTE: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

# for num, dig in enumerate(numbers):
#	 if num % 2 != 0:
# 		print(dig)
#NOTE: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

#TODO: Exercise 6 : While Loop -- Instructions -- Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# user_proposition = input("What is my name?\n")
# while user_proposition != "AnnaSpirit":
#	 user_proposition = input('Again, what is my name?\n ')
# print("BRAVO!")

#TODO: Exercise 7: Favorite fruits --Instructions -- 1. Ask the user to input their favorite fruit(s) (one or several fruits). 2. Store the favorite fruit(s) in a list (convert the string of words into a list of words). 3. Now that we have a list of fruits, ask the user to input a name of any fruit. 3a. If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”. 3b. If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# fruits_fav = input("Write at least 3 fruits, separated by a space\n")
# fruit_list = fruits_fav.split(" ")
# print(fruit_list)
# #NOTE: ['Lime', 'Lemon', 'Mango']
# user_fruit = input("Choose 1 fruit\n")
# if user_fruit in fruit_list:
#	 print("Bon Appetit")
# else:
#	 print("you choose a new one, try it...")

#TODO: Exercise 8: Who ordered a pizza ? -- Instructions -- 1. Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings. 2. As they enter each topping, print a message saying you’ll add that topping to their pizza. 3. Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# top_ping = input("Add the topping you want on your pizza\n Enough? write 'quit'\n")
# topping_count = 0
# while top_ping != "quit":
#	 top_ping = input("Add your toppings or if you have finish, write: 'quit'\n")
#	 print("we will add to your pizza!")
#	 topping_count = topping_count + 1

# total_price = 10 + (2.5 * topping_count)
# print(f"You have: 1 pizza that cost:10) + {topping_count} toppings (each topping price is 2.5) so the total price is {total_price} ")
# #NOTE: You have: 1 pizza that cost:10) + 5 toppings (each topping price is 2.5) so the total price is 22.5

#TODO: Exercise 9: Cinemax --Instructions-- A movie theater charges different ticket prices depending on a person’s age.  1. if a person is under the age of 3, the ticket is free. 2. if they are between 3 and 12, the ticket is $10. 3. if they are over the age of 12, the ticket is $15. 4. Ask a family the age of each person who wants a ticket. 5. Store the total cost of all the family’s tickets and print it out. 6. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21. 7. Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list. 8. At the end, print the final list.

# family = input("Enter the age of each person who needs ticket, separated by a space\n")
# family = family.split(" ")
# #HACK: convert family_list into integer
# list_family = [int(age) for age in family]
# print(list_family)
# #NOTE: ['5', '12', '16', '22', '45', '88', '89']
# print(f"You're {len(family)} persons")
# #NOTE: 7

# price = []
# for age in list_family:
#	 if age < 3:
#		 price.append(0)
#	 elif 3 <= age <= 12:
#		 price.append(10)
#	 elif age > 12:
#		 price.append(15)
# # print(price)
# #NOTE: [10, 10, 15, 15, 15, 15, 15]
# print(f"For your cinema entrance you will pay: {sum(price)}")

#TODO: Exercise 10 : Sandwich Orders --Instructions-- Using the list below : sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"] 1. The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders. 2. We need to prepare the orders of the clients: 3. Create an empty list called finished_sandwiches. 4. One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list. 5. After all the sandwiches have been made, print a message listing each sandwich that was made, such as: I made your tuna sandwich I made your avocado sandwich I made your egg sandwich I made your chicken sandwich

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
print(f"You're order: {sandwich_orders}")
#NOTE: You're order: ['Tuna sandwich', 'Pastrami sandwich', 'Avocado sandwich', 'Pastrami sandwich', 'Egg sandwich', 'Chicken sandwich', 'Pastrami sandwich']
while "Pastrami sandwich" in sandwich_orders:
	sandwich_orders.remove("Pastrami sandwich")
print("Sorry! Deli has run out of pastrami.")
#NOTE: Sorry! Deli has run out of pastrami.
print(sandwich_orders)
#NOTE: ['Tuna sandwich', 'Avocado sandwich', 'Egg sandwich', 'Chicken sandwich']

finished_sandwiches = []
for sand in sandwich_orders[:]:  #HACK: We go through a copy of the list
	sandwich_orders.remove(sand)
	finished_sandwiches.append(sand)
	print(f"Your {sand} is ready.")

print("Remaining orders:", sandwich_orders)
print("Finished orders:", finished_sandwiches)
