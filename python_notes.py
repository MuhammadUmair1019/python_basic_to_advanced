# ---------------------------------------------------------------------------------
# Conditional Statements (if-else) and Loops

# Age comparison using if-else
age = 17

if age < 18:
    # User is below 18 years old
    pass  # Placeholder, doesn't perform any action
    # print("You are below 18")

# Asking user's age and playing a game based on age condition
age = int(input("Please enter your age: "))

if age > 18:
    print("Congrats! You can play this game")
else:
    print("Sorry, you can't play this game :(")

# Number Guessing Game
import random

winning_num = random.randint(0, 100)
print(winning_num)
guessing_num = int(input("Please enter a number: "))

if guessing_num == winning_num:
    print("Congratulations, you win the game")
elif guessing_num < winning_num:
    print("Too low")
else:
    print("Too high")

# Watching movie exercise based on user input
name, age = input("Please enter your name and age (space-separated): ").split(" ")
name_first_char = name[0]

if (name_first_char == 'a' or name_first_char == 'A') and int(age) > 10:
    print("You can watch the movie 'Coco'")
else:
    print("Sorry, you can't watch the movie 'Coco'")

# Ticket Pricing based on age
age = int(input("Please enter your age: "))

if age == 0 or age < 0:
    print("You can't watch")
elif 0 < age <= 3:
    print("Ticket price: Free")
elif 3 < age <= 10:
    print("Ticket price: 150")
elif 10 < age <= 60:
    print("Ticket price: 250")
else:
    print("Ticket price: 200")

# Checking character existence and empty string
name = "umair"

if 'u' in name:
    print("Exists")
else:
    print("Doesn't exist")

# Check if string is empty or not
name = "umair"

if name:
    print("Not empty")
else:
    print("Empty")

# Sum of digits of a number
numbers = input("Enter a number: ")
total = 0
i = 0

while i < len(numbers):
    total += int(numbers[i])
    i += 1

print("Sum of digits:", total)

# Counting occurrence of each letter in a word
name = input("Please enter your name: ")

name = name.lower()
temp_var = ""
i = 0

while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]}: {name.count(name[i])}")
    i += 1

# For loop example - calculating sum of numbers
total = 0

for i in range(1, 11):
    total += i

print("Total sum:", total)

# Calculate sum of digits in a number entered by the user
numbers = input("Enter a number: ")
total = 0

for i in range(len(numbers)):
    total += int(numbers[i])

print("Sum of digits:", total)

# Counting occurrence of each letter in a word using for loop
name = input("Please enter your name: ")
name = name.lower()
temp_var = ""

for i in range(len(name)):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]}: {name.count(name[i])}")

# step argument in for loop 
for i in range(0, 11, 2):
    print(i)
for i in range(10, -1):
    print(i)

# ---------------------------------------------------------------------------------
# Strings
# A string is a collection of characters enclosed in single or double quotes.
first_name = "Muhammad"
last_name = "Umair"

# Concatenate strings
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# You can also concatenate a string and a number by converting the number to a string.
print(first_name + str(3))

# Repetition of strings
print(first_name * 3)

# Input from the user
name = input("What is your name: ")
print("Hello " + name)

# Using int() to convert input to integers
num_1 = int(input("Please enter number 1: "))
num_2 = int(input("Please enter number 2: "))
total = num_1 + num_2
print("Total is:", total)
# Note: You can add integers and floats, but the result will always be a float.

# Declaring multiple variables in one line
name, age = "Umair", "24"
print("Name:", name)
print("Age:", age)

# Taking two inputs in one line, separated by a space
name, age = input("Enter your name and age: ").split(" ")
print("Name:", name)
print("Age:", age)

# String formatting using format()
print("Hello {} your age is {}".format(name, age))

# String formatting using f-strings (Python 3.6+)
print(f"Hello {name} your age is {age}")

# Taking and calculating the average of three numbers
num1, num2, num3 = input("Enter three numbers: ").split(" ")
average = (int(num1) + int(num2) + int(num3)) / 3
print(f"The average of three numbers: {average}")

# String indexing
language = "Python"

# Indexing allows you to access individual characters in a string. Indices start from 0 for the first character.
# Using negative indices counts from the end, with -1 representing the last character.
print("Last character:", language[-1])  # Access the last character (n)
print("Second character:", language[1])  # Access the second character (y)

# String slicing
# Slicing allows you to extract a portion of a string based on the start and stop positions.
# Syntax: [start argument : stop argument - 1]
print("Sliced from index 0 to 2:", language[0:2])  # Returns "Py"
print("Sliced from start to end:", language[:])  # Returns the complete string "Python"
print("Sliced from index 1 to the end:", language[1:])  # Returns "ython" (starts from the second character)
print("Sliced from the start to index 3:", language[:3])  # Returns "Pyt" (goes up to the fourth character)

# Step Argument (Stride) in String Slicing
# String slicing allows you to extract substrings from a string. The step argument specifies how many characters to skip.
lang = "PythonProgramming"
# Syntax for slicing with a step argument: [start : stop : step]
# Start and stop are inclusive, while the step determines the interval between characters.

# Example 1: Using a positive step to extract every second character.
print("Every second character:", lang[0::2])  # Starts from index 0, takes every 2nd character.

# Example 2: Using a negative step to reverse the string.
print("Reversed string:", lang[::-1])  # Reverses the string.

# Example 3: Using a step to skip characters in the middle.
print("Skip characters:", lang[1:12:3])  # Starts from index 1, stops at index 12, and takes every 3rd character.

# Example 4: Combining slicing and step to extract a substring.
substring = lang[3:10:2]  # Starts from index 3, stops at index 10, and takes every 2nd character.
print("Custom substring:", substring)

# Example 5: Slicing with negative indices and step argument.
reverse_substring = lang[-5:-1:1]  # Starts from the 5th character from the end, stops at the 1st character from the end.
print("Reverse substring:", reverse_substring)

# String Methods
name = "Muhammad Umair"

# len() function
print(len(name))

# lower() method
print(name.lower())

# upper() method
print(name.upper())

# title() method
print(name.title())

# count() method
print(name.count("u"))

# lstrip() remove spaces left of the str
# rstrip() remove spaces right of the str
# strip()  remove spaces both side of the str

# to remove space inside the string use replace method
print(name.replace(" ", "")) # 

# Take input and print back user name in reverse order
name = input("Enter your name: ")
print(f"Name is reverse order: {name[::-1]}")

# Take two comma seprated inputs from user
# output name length, count the character
name, char = input("Enter name and find character string in space seprated: ").split(" ")

print(f"{name}: {len(name.strip())} (length) \n{char.strip()} : {name.strip().lower().count(char.strip())} (times)")

# find and replace methods in strings
sentence = "he is a very good developer and he is a very good character"

# Using the replace method to replace spaces with underscores
modified_sentence = sentence.replace(" ", "_")
print("Sentence with spaces replaced:", modified_sentence)

# Using the find method to find the first occurrence of a word in a string
word_to_find = "is"
first_occurrence = sentence.find(word_to_find)
print(f"Index of the first '{word_to_find}' occurrence:", first_occurrence)

# Using the find method to find the second occurrence of a word in a string
# Find the position of the word starting after the first occurrence
second_occurrence = sentence.find(word_to_find, first_occurrence + 1)
print(f"Index of the second '{word_to_find}' occurrence:", second_occurrence)

# center method in strings

# Define a string
text = "Python"

# Using the center method to center the text within a string of a specified width
centered_text = text.center(len(text) + 4, '*')
print(f"Centered Text: '{centered_text}'")

# Using center method with a larger width than the string length
centered_text_larger_width = text.center(len(text) + 8, '-')
print(f"Centered Text (larger width): '{centered_text_larger_width}'")

# Explanation:

# The `center()` method is used to center a string within a specified width. It takes two arguments:
# - The first argument is the width of the resulting string.
# - The second argument (optional) is the character used to fill the space around the original string. If not specified, it defaults to a space.

# In the provided example:
# - The string "Python" is centered within a width of 10 characters, using asterisks (`*`) as the fill character.
# - Additionally, the string "Python" is centered within a width of 20 characters, using hyphens (`-`) as the fill character.

# This method is useful for formatting text and ensuring it appears centered within a specified space.

print("--------------------------------------------------------------------------")
# ---------------------------------------------------------------------------------
# Variables in Python
# Variables can store strings, numbers, and other data types.
num = 1
print("Number:", num)

# Rules for declaring variables
# 1- Variable names cannot start with a number and cannot use special characters.
# 2- Letters and underscores (_) are allowed.

# Naming conventions
snake_case_variable = "Umair"  # Snake case writing (Recommended)
CamelCaseVariable = "Umair"     # Camel case writing

print("--------------------------------------------------------------------------")
# ---------------------------------------------------------------------------------
# Calculations in Python
# Basic arithmetic operations and operator precedence
print("2 + 2 * 2 =", 2 + 2 * 2)
print("2 / 4 =", 2 / 4)      # Floating-point division
print("2 // 4 =", 2 // 4)     # Integer division
print("2 ** 3 =", 2 ** 3)     # Exponentiation
print("2 ** 0.5 =", 2 ** 0.5)   # Square root
print("Rounded result of 2 ** 0.5 to 4 decimal places:", round(2 ** 0.5, 4))

# Precedence and Associativity rules
# Parentheses -> Highest
# Exponentiation (**) -> Right to Left
# Multiplication (*), Division (/), Floor Division (//), Modulus (%) -> Left to Right
# Addition (+), Subtraction (-) -> Left to Right

print("Calculation (2 + 3) * 5 / 2 % 6:")
# Calculation steps:
# (2 + 3) * 5 / 2 % 6
# 5 * 5 / 2 % 6
# 25 / 2 % 6
# 12.5 % 6

# ---------------------------------------------------------------------------------
# Output -> Line A \n Line B
print("Line A \\n Line B")

# Printing specific patterns and escape sequences
print("This is \\\\ double backslash")
print("This is /\\/\\/\\/\\ mountain back")
print("He is\tawesome")  # Use tab (\t) instead of manual spaces
print("\\\" \\n \\t \'")  # Print special characters as an input

# Using a raw string to ignore escape sequences
print(r"\" \n \t \'")

# ---------------------------------------------------------------------------------
# Escape sequences
print("Hello \"Expertizo\" Team")
print('Hello \'Expertizo\' Team')
print("Hello world \\")  # Print a backslash using an escape sequence
print("Helloo\b world")   # Use backspace (\b) to remove extra characters
print("Hello\tworld")    # Use tab (\t) for indentation
print("Hello\nworld")    # Use a newline character (\n) for line breaks