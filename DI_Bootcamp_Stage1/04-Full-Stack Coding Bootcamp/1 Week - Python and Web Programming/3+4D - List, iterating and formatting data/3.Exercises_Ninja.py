#TODO: Exercise 1: Formula --Instructions--1. Write a program that calculates and prints a value according to this given formula: Q = Square root of [(2 * C * D)/H] 2. Following are the fixed values C is 50 H is 30. 3.Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results. For example, if the user inputs: 100,150,180=> The output should be: 18,22,24

# def calcul_q(d):
#     C = 50
#     H = 30
# #HACK: Calcul de Q en utilisant l'opérateur d'exponentiation pour la racine carrée
#     return round(((2 * C * d) / H) ** 0.5)

#HACK: Lecture des valeurs séparées par un espace (exemple : "100 150 180")
# I prefer using space-separated instead of comma-separated string of numbers
# valeurs_input = input("Enter space separated values for D: ")

# valeurs = [int(x) for x in valeurs_input.split()]

# results = [str(calcul_q(d)) for d in valeurs]

# print(" ".join(results))


#TODO: Exercise 2 : List of integers--Instructions--1. Store the list of numbers in a variable. 2.Print the following information: 2.a. The list of numbers – printed in a single line. 2.b. The list of numbers – sorted in descending order (largest to smallest). 2.c. The sum of all the numbers. 3. A list containing the first and the last numbers. 4. A list of all the numbers greater than 50. 5. A list of all the numbers smaller than 10. 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”. 7. The numbers without any duplicates – also print how many numbers are in the new list. 8.The average of all the numbers. 9. The largest number. 10.The smallest number. 11.Bonus: Find the sum, average, largest and smallest number without using built in functions. 12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier. 13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100. 14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50. 15.Bonus: Will the code work when the number of random numbers is not equal to 10?

# 1. Store the list of numbers in a variable
# numbers = [34, 159, 8, 67, 23, 89, 12, 34, 45, 78, 56, 90, 33, 8, 3]

# 2.a. Print the list of numbers on a single line
# print("List of numbers:", numbers)

# 2.b.
# sorted_descending = sorted(numbers, reverse=True)
# print("Sorted in descending order:", sorted_descending)

# 2.c.
# total = sum(numbers)
# print("Sum of all numbers:", total)

# 3.
# first_last = [numbers[0], numbers[-1]]
# print("First and last number:", first_last)

# 4. 
# greater_50 = [n for n in numbers if n > 50]
# print("Numbers greater than 50 :", greater_50)

# 5.
# smaller_10 = [n for n in numbers if n < 10]
# print("Numbers smaller than 10 :", smaller_10)

# 6. 
# numbers_squared = [n**2 for n in numbers]
# # On affiche les résultats sous forme d'une chaîne de nombres séparés par un saut de ligne
# squared_str = "\n".join(str(x) for x in numbers_squared)
# print("Nombres au carré :", squared_str)

# 7. Pour conserver l'ordre d'apparition, on utilise une boucle
# unique_numbers = []
# for n in numbers:
#     if n not in unique_numbers:
#         unique_numbers.append(n)
# print("Numbers without duplicates :", unique_numbers)
# # print("Number of unique numbers :", len(unique_numbers))
# print(f"Number of unique numbers: {len(unique_numbers)} out of {len(numbers)} total.")

# 8. 
# total = 0
# compt = 0

# for a in numbers:
#     total += a
#     compt += 1

# if compt != 0:
#     Average = total / compt
# else:
#     Average = 0  # To avoid division from zero
# print("Average :", Average)

# if numbers:
#     average = sum(numbers) / len(numbers)
# else:
#     average = 0
# print("Average (with integrated fonctions) :", average)

# 9.
# if numbers:  # Check if the List is not empty
#     max_val = numbers[0]
#     for n in numbers:
#         if n > max_val:
#             max_val = n
#     print(f"Among the figures, {max_val} is the largest.")
# else:
#     print("The list is empty.")

# if numbers:
#     max_num = max(numbers)
# else:
#     max_num = None
# print("Nombre maximum (avec fonctions intégrées) :", max_num)

# 10. 
# if numbers:  # Check if the List is not empty
#     min_val = numbers[0]
#     for n in numbers:
#         if n < min_val:
#             min_val = n
#     print(f"Among the figures, {min_val} is the smallest.")
# else:
#     print("The list is empty.")

# if numbers:
#     min_num = min(numbers)
# else:
#     min_num = None
# print("Nombre minimum (avec fonctions intégrées) :", min_num)

# 11.
# def custom_sum(lst):
#     total = 0
#     for n in lst:
#         total += n
#     return total

# def custom_average(lst):
#     if len(lst) == 0:
#         return 0
#     return custom_sum(lst) / len(lst)

# def custom_max(lst):
#     if not lst:
#         return None
#     max_val = lst[0]
#     for n in lst:
#         if n > max_val:
#             max_val = n
#     return max_val

# def custom_min(lst):
#     if not lst:
#         return None
#     min_val = lst[0]
#     for n in lst:
#         if n < min_val:
#             min_val = n
#     return min_val

# print("Sum custom :", custom_sum(numbers))
# print("Average custom :", custom_average(numbers))
# print("Maximum custom :", custom_max(numbers))
# print("Minimum custom :", custom_min(numbers))

# 12.
# user_numbers = []

# for i in range(10):
#     while True:
#         try:
#             n = int(input(f"Enter the number {i+1} (value between -100 and 100) : "))
#             if -100 <= n <= 100:
#                 user_numbers.append(n)
#                 break
#             else:
#                 print("The number must be between -100 and 100. Re-Try.")
#         except ValueError:
#             print("Please enter a valid integer.")
# print("This is your list :", user_numbers)

# 13
# import random
# random_numbers = [random.randint(-100, 100)
# 	for _ in range(10)]
# print("Find the Random numbers :", random_numbers)

# 14
# nb_count = random.randint(51, 150)
# random_list = [random.randint(-100, 100) for _ in range(nb_count)]
# print(f"Number generated numbers: {nb_count}")
# print("Here is the list generated :", random_list)

#15 : 
# NOTE: Answer: Yes, the code works generic without supposing a fixed size of the list. We can recalculate statistics on 'random_list' without problem.

# if random_list:
#     print("Sum :", sum(random_list))
#     print("Average :", sum(random_list)/len(random_list))
#     print("Maximum :", max(random_list))
#     print("Minimum :", min(random_list))
# else:
#     print("Empty list")

#TODO: Exercise 3: Working on a paragraph --Find an interesting paragraph of text online. Paste it to your code, and store it in a variable. Let’s analyze the paragraph. Print out a nicely formatted message saying: 1. How many characters it contains (this one is easy…). 5. How many sentences it contains. 6. How many words it contains. 7. How many unique words it contains. 8. Bonus: How many non-whitespace characters it contains. 9. Bonus: The average amount of words per sentence in the paragraph. 10. Bonus: the amount of non-unique words in the paragraph.

# purim_joke = "Bob, the town’s lovable absent-minded soul, planned a unique Purim costume—a mash-up of pirate flair, clownish fun, and a giant hamantaschen hat. The night before, he imagined perfection, but on Purim day, he overslept. In a rush, he grabbed whatever he could: a striped pirate shirt, a polka-dotted clown wig, and that oversized hat balanced on his head. At the party, Bob’s mismatched look had everyone laughing. Even the local rabbi couldn’t help but smile at his “creative chaos.” His spontaneous ensemble won the “Most Original Costume” award, proving that sometimes a mix-up can turn into the best memory of the day."

# import re 
# #HACK: module Python dédié aux expressions régulières, ce qui offre des outils puissants pour rechercher, manipuler et analyser des chaînes de caractères à l'aide de motifs précis.

# # 4.
# num_characters = len(purim_joke)

# # 5. 
# # sentence end by '.', '!' or '?'
# sentences = re.split(r'[.!?]+', purim_joke)
# sentences = [s.strip() 
# 	for s in sentences
# 	if s.strip() != '']
# num_sentences = len(sentences)

# # 6. 
# # Utilisation d'une expression régulière pour extraire les mots en ignorant la ponctuation
# words = re.findall(r'\w+', purim_joke)
# num_words = len(words)

# # 7. 
# unique_words = set(word.lower()
# 	for word in words)
# num_unique_words = len(unique_words)

# # 8.
# non_whitespace_chars = len(re.findall(r'\S', purim_joke))

# # 9. Calcul de la moyenne de mots par phrase
# aver_words_per_sentence = num_words / num_sentences if num_sentences else 0

# # 10. 
# # On considère ici les mots répétés : total de mots - mots uniques
# non_unique_words = num_words - num_unique_words

# # Affichage des résultats
# print(f"Number of total characters: {num_characters}")
# print(f"Number of sentences: {num_sentences}")
# print(f"Number of total words: {num_words}")
# print(f"Number of unique words: {num_unique_words}")
# print(f"Number of non-whitespace characters: {non_whitespace_chars}")
# print(f"Average words per sentence: {aver_words_per_sentence:.2f}")
# print(f"Number of non-unique words: {non_unique_words}")

#TODO: Exercise 4 : Frequency Of The Words--Instructions--1. Write a program that prints the frequency of the words from the input. Suppose the following input is supplied to the program: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. Then, the output should be: 2:2, 3.:1, 3?:1, New:1, Python:5, Read:1, and:1, between:1, choosing:1, or:2, to:1

ver_python = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

def main():
    input_str = input("Enter the input: ")

    # Split the string into words (by whitespace)
    words = input_str.split()

    # Count the frequency of each word
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Sort the keys (words) lexicographically
    sorted_words = sorted(freq.keys())

    # Create a formatted output string: word:frequency, separated by commas
    result = ", ".join(f"{word}:{freq[word]}" for word in sorted_words)
    print(result)

if __name__ == '__main__':
    main()
#NOTE: 2:2, 3.:1, 3?:1, New:1, Python:5, Read:1, and:1, between:1, choosing:1, or:2, to:1