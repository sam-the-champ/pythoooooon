import random
# list
# importing modules
# if/else block
# while loop
# more string method
# tuples

# list is a datatype and  a data structure that helps to store multiple values in a single variable. 
# It is a collection of items that are ordered and changeable. 
# Lists are defined by enclosing the items in square brackets []
# it is equivalent to an array in other programming languages.
# the difference between list and array in python is that list can store different data types in a single list
# while array can only store one data type in a single array.

skills = ["Python", "JavaScript", "HTML", "CSS", "SQL", "typescript"]
years_of_experience = [2, 3, 1, 1, 2, 1]
about_me = ["😁", "😎", "💻"]
print()
print(skills)
print()
print(years_of_experience)
print()
print(about_me)

tickets = ["Ada", "Grace", "Linus", "Margaret", "Alan"]

print(f"now helping {tickets[0]} with her ticket")
print()
print(f"next in line is {tickets[1]}")
print()
print(f"just added {tickets[-2]} to the list of tickets")

first_word = list("earth")
second_word = list("heart")

print(sorted(first_word))
print(sorted(second_word)) #valid anagram

first_2_word = list("below")
second_2_word = list("elbow")

print(sorted(first_2_word))
print(sorted(second_2_word))  #valid anagram


players = ["Mara", "Devon", "Priya", "Leo"]

random.shuffle(players)
print(players)

dealing = random.choice(players)
    
print(f"Dealing card to {dealing}!")

# use the random module to generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number generated: {random_number}")

# the methods i used on the random module in this file are
# .shuffle() - shuffles the list in place
# .choice() - returns a random element from the list
# .randint() - returns a random integer between the two specified numbers (inclusive)