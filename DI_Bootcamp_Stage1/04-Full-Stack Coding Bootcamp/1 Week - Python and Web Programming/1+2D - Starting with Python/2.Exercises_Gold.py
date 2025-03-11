# #TODO: Exercise 1 : Hello World-I love Python - : Instructions - Print the following output in one line of code: Hello world Hello world Hello world Hello world I love python I love python I love python I love python

# print("Hello world " * 4 + "I love python " * 4)
# #NOTE: Hello world Hello world Hello world Hello world I love python I love python I love python I love python

#TODO: Exercise 2 : What is the Season ? - Instructions -- 1. Ask the user to input a month (1 to 12). 2. Display the season of the month received :Spring runs from March (3) to May (5), ummer runs from June (6) to August (8), Autumn runs from September (9) to November (11), Winter runs from December (12) to February (2).

month = input("Enter a month (1 to 12): ")
month = int(month)
if month in [3, 4, 5]:
	print("Spring")
elif month in [6, 7, 8]:
	print("Summer")
elif month in [9, 10, 11]:
	print("Autumn")
else:
	print("Winter")

# option 1 #NOTE: Enter a month (1 to 12): 8
# NOTE: Summer
# option 2 #NOTE: Enter a month (1 to 12): 12
# NOTE: Winter
# option 3 #NOTE: Enter a month (1 to 12): 4
# NOTE: Spring
# option 4 #NOTE: Enter a month (1 to 12): 10
# NOTE: Autumn


