#TODO: Exercises 1 + 2: Use the terminal --https://octopus.developers.institute/courses/collection/103/course/501/section/1292/chapter/213 --

# #TODO: Exercise 3 : Outputs -- Instructions -- Predict the output of the following code snippets: A. 3 <= 3 < 9, B. 3 == 3 == 3, C. bool(0), D. bool(5 == "5"), E. bool(4 == 4) == bool("4" == "4"), F. bool(bool(None)), G. x = (1 == True) y = (1 == False) a = True + 4 b = False + 10 print("x is", x) print("y is", y) print("a:", a) print("b:", b)

# #A.
# print(3 <= 3 < 9)
# #NOTE: True
# #B.
# print(3 == 3 == 3)
# #NOTE: True
# #C.
# print(bool(0))
# #NOTE: False
# #D.
# print(bool(5 == "5"))
# #NOTE: False
# #E.
# print(bool(4 == 4) == bool("4" == "4"))
# #NOTE: True
# #F.
# print(bool(bool(None)))
# #NOTE: False
# #G.
# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10
# print("x is", x)
# #NOTE: x is True
# print("y is", y)
# #NOTE: y is False
# print("a:", a)
# #NOTE: a: 5
# print("b:", b)
# #NOTE: b: 10

# #TODO: Exercise 4 : How many characters in a sentence ? -- Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable). ´´´y_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,  sunt in culpa qui officia deserunt mollit anim id est laborum.´´´

# lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,  sunt in culpa qui officia deserunt mollit anim id est laborum."
# print(len(lorem_text))
# #NOTE: 446

#TODO: Exercise 5: Longest word without a specific character - Instructions --1. Ask the user to input the longest word they can without the character “A”. 2. Each time a user successfully sets a new longest word, print a congratulations message.

long_word = ""
while True:
	word = input("Could you find the longest word without the character 'A': ")
	#HACK: just verify upper or lower case!
	if "a" in word.lower():
		print("False! The word contain the letter 'A'. Try Again!")
	elif len(word) > len(long_word):
		long_word = word
		print("Whoa! You've just unlocked **UltraMegaSuperCaliFragilisticExpialiLongestWordMode**!")
	else:
		print("Congrats! You’ve just leveled up in the Dictionary Boss Battle! Keep going!")
	continu = input("Are you brave enough to keep going? (yes/no)")
	if continu.lower() != "yes":
		break 
#HACK: other if for 2 messages, success or not!
if long_word:
	print(f"The longest word you entered is: {long_word}")
else:
	print("😢 Oops! You never entered a valid word without 'A'.")

#option 1 #NOTE: Could you find the longest word without the character 'A': Banana
#NOTE: False! The word contain the letter 'A'. Try Again!
#NOTE: Are you brave enough to keep going? (yes/no)yes
# option 2 NOTE: Could you find the longest word without the character 'A': bedcovering
#NOTE: Whoa! You've just unlocked **UltraMegaSuperCaliFragilisticExpialiLongestWordMode**!
#NOTE: Are you brave enough to keep going? (yes/no)yes
# option 3 NOTE: Could you find the longest word without the character 'A': belongingnesses
#NOTE: Whoa! You've just unlocked **UltraMegaSuperCaliFragilisticExpialiLongestWordMode**!
#NOTE: Are you brave enough to keep going? (yes/no)no
#NOTE: The longest word you entered is: belongingnesses

#INFO: SOLUTION: 15 Letters words without 'A': belongingnesses, benightednesses, beseemingnesses, bespottednesses, bibliophilistic, biodestructible, bioengineerings, biogeochemistry, bioluminescence, bioprospectings, biopsychologies, biotechnologies, biotechnologist, bittersweetness, bloodcurdlingly, bloodguiltiness, bloodlessnesses, bloodthirstiest, bouleversements, boundlessnesses, bounteousnesses, bountifulnesses, bourgeoisifying, boustrophedonic, bronchiolitises, bronchoscopists, brotherlinesses, bumptiousnesses, businesspersons, butterflyfishes, centrosymmetric, cercopithecoids, ceremoniousness, cheerlessnesses, chemolithotroph, chemoprevention, chemoreceptions, childlessnesses, childlikenesses, chincherinchees, chloroethylenes, cholecystectomy, cholecystitides, cholecystitises, cholecystokinin, cholecystostomy, chondrophorines, chondroskeleton, chronobiologies, chronobiologist, churrigueresque, circumferentors, circumincession, circuminsession, circumlocutions, circumpositions, circumscription, circumscriptive, circumspections, circumspectness, circumvolutions, citriculturists, cloudlessnesses, coconsciousness, collectednesses, colliquescences, colorlessnesses, colourfulnesses, combustibleness, comfortlessness, compendiousness, competentnesses, competitiveness, complementisers, complementizers, completednesses, complexednesses, compositenesses, comprehensively, comprehensivise, comprehensivize, compressibility, comptrollership, computerphobics, conceitednesses, concentricities, concernednesses, concertednesses, concertmeisters, concertmistress, condescendences, condescendingly, conducivenesses, conductiometric, confectioneries, confidingnesses, confirmednesses, congresspersons, congruousnesses, conjunctiveness.

#INFO: https://capitalizemytitle.com/wordfinder/doesnt-contain/a/