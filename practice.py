# Exercise

# Take input and print back user name in reverse order
# name = input("Enter your name: ")
# print(f"Name is reverse order: {name[::-1]}")

# # string methods
# name = "Muhammad Umair"

# # len() function
# print(len(name))

# # lower() method
# print(name.lower())

# # upper() method
# print(name.upper())

# # title() method
# print(name.title())

# # count() method
# print(name.count("u"))


# Take two comma seprated inputs from user
# output name length, count the character

# name, char = input("Enter name and find character string in space seprated: ").split(" ")

# print(f"{name}: {len(name)} (length) \n{char} : {name.lower().count(char)} (times)")


# # find and replace method 
# sentence = "he is a very good developer and he is a very good characte"
# # replace method helps to replace particualr character with our own specify string or word
# print(sentence.replace(" ", "_"))

# # find method helps to find particular index of the given word in a collection of string
# print(sentence.find("is")) # find first finded index
# is_pos1 = sentence.find("is")
# is_pos2 = sentence.find("is", is_pos1 + 1)
# print(is_pos2)


# # find and replace methods in strings

# sentence = "he is a very good developer and he is a very good character"

# # Using the replace method to replace spaces with underscores
# modified_sentence = sentence.replace(" ", "_")
# print("Sentence with spaces replaced:", modified_sentence)

# # Using the find method to find the first occurrence of a word in a string
# word_to_find = "is"
# first_occurrence = sentence.find(word_to_find)
# print(f"Index of the first '{word_to_find}' occurrence:", first_occurrence)

# # Using the find method to find the second occurrence of a word in a string
# # Find the position of the word starting after the first occurrence
# second_occurrence = sentence.find(word_to_find, first_occurrence + 1)
# print(f"Index of the second '{word_to_find}' occurrence:", second_occurrence)


# age = 17
# if(age < 18):
#     pass
#     # print("You are below 18")

# age =  int(input("Please enter your age: "))

# if(age > 18):
#     print("Congrats! you can play this game") 
# else: 
#     print("Sorry you can't play this game :(")


# Number gussing game 
# import random

# winning_num = random.randint(0, 100)
# print(winning_num)
# gussing_num = int(input("Please enter correct num: "))

# if gussing_num == winning_num:
#     print(f"Congrats you win the game")
# elif gussing_num < winning_num:
#     print(f"Too low")
# else:
#     print(f"Too high")


# Exercise - WATCH COCO
# Ask user's name and age if user name start with ('a' or 'A') and age is above 10 then 
# Print 'you can watch coco movie'
# print 'sorry, you can't watch coco'

# name, age = input("Please enter you name and age with space seprated: ").split(" ")
# name_first_char =  name[0]
# if name_first_char == 'a' or name_first_char == 'A' and int(age) > 10:
#     print("You can watch coco movie") 
# else:
#     print("Sorry, you can't watch coco movie")


# show ticket pricing 
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

# age = int(input("Please enter your age: "))

# if age == 0 or age < 0:
#   print("You can't watch")
# elif 0<age<=3:
#   print("Ticket price: Free")
# elif 3<age<=10:
#   print("Ticket price: 150")
# elif 10<age<=60:
#   print("Ticket price: 250")
# else:
#   print("Ticket price: 200")

# name = "umair"
# if 'u' in name: 
#     print("Exist")
# else:
#     print("Not exit")


# check empty or not 
# important
# name = "umair"
# if name:
#   print("Not empty")
# else: 
#   print("Empty")

# print("You didn\'t type anything")

# Sum of digits of a number 

# numbers = input("Enter a numbers: ")
# total = 0
# i = 0

# while i < len(numbers):
#     total += int(numbers[i])
#     i += 1

# print(total)


# Print count for each word of a given number 
# name = input("Please enter your name: ")

# name = name.lower()
# temp_var = ""
# i = 0

# while(i < len(name)):
#     if name[i] not in temp_var:
#       temp_var += name[i]
#       print(f"{name[i]}:{name.count(name[i])}")
#     i += 1

# For loop 
# total = 0
# for i in range(1, 11):
#     total += i
# print(total)


# ask user a number like 123 and calculate sum of digits 1 + 2 + 3
# numbers = input("Enter a numbers: ")
# total = 0

# for i in range(len(numbers)):
#     total += int(numbers[i])

# print(f"Total is: {total}")

# Print count for each word of a given number 
# name = input("Please enter your name: ")

# name = name.lower()
# temp_var = ""

# for i in range(len(name)): 
#     if name[i] not in temp_var:
#       temp_var += name[i]
#       print(f"{name[i]}:{name.count(name[i])}")

# for i in range(10, -1, -1):
#     print(i)


# functions

# def add_two(a, b):
#     return a + b

# print(add_two(5, 4))

# def is_plaindrom(word):
#     reversed_word = word[::-1]
#     if reversed_word == word:
#         return True
#     return False

# print(is_plaindrom("mamas"))


# name = "umair"
# age = 2
# married_status =  False

# num1 = int(input("Please enter your first num: "))
# num2 = int(input("Please enter your second num: "))

# print(f"Total is: {num1 + num2}")


# numbers = [2, 3, 4, 5, 6]
# print(numbers[1:])

# numbers[1:] = [4]
# print(numbers)


# append method 
# insert method 
# extend method 
# pop, remove, del

# count, sort, reverse, clear, copy
# is vs equal
# generate list with range list(range(0, 11))
# find partiuclar index list.index(find_index,  after_index)
# pass list to a function

# Tuples