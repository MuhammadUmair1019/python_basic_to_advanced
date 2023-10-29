
# ---------------------------------------------------------------------------------
# Strings
# Collection of characters inside single quote or doube quote
first_name = "Muhammad"
last_name = "Umair"
print(first_name + " " + last_name) 
print(first_name + str(3)) 
print(first_name * 3)

# Take input from user
name = input("What is your name: ")
print("Hello " + name)

# Int function
# Write a program take 2 num as an input and return sum of those number
num_1 = int(input("Please enter number 1: "))
num_2 = int(input("Please enter number 2: "))
total = num_1 + num_2
print("Total is: " + str(total))
# we can add int and float but the final output always be in float

# declear more variables in one line
name, age = "Umair", "24"
print(name, age)

# Take 2 input in one line
# name, age = input("Enter your name and age ").split(" ") # add comma seprated value as well
# print(name, age)

# String formating
print("Hello {} your age is {}".format(name, age)) # use in python 3 

# 3.6 
print(f"Hello {name} your age is {age}") # use in python 3 

num1, num2, num3 = input("Enter three numbers: ").split(" ")
average = (int(num1) + int(num2) + int(num3)) / 3
print(f"The average of three numbers: {average}")


print("--------------------------------------------------------------------------")
# ---------------------------------------------------------------------------------
# Variables in python
# string, num
num = 1
print(num)

# Rules for declearing variables
# 1- Variable cannot start with num and can't use any special character  
# 2- letter, _

# Convention
store_user_name = "Umair" # snake case writing (Recommended)
storeUserName = "Umair" # camel case writting

print("--------------------------------------------------------------------------")
# ---------------------------------------------------------------------------------
# Calculation in python
print(2+2*2)
print(2/4) #floating division
print(2//4) # integer division
print(2**3)
print(2**0.5)
print(round(2**0.5, 4)) # limit the floating point number

# Precedence and Associativity rule 
# Parantheses -> Highest
# Exponent    -> Right TO LEFT
# *, /, //, % -> LEFT TO RIGHT 
# +, -        -> LEFT TO RIGHT

print((2+3)*5/2%6)
# 5 * 5  / 2 % 6
# 25 / 2 % 6
# 12.5 % 6

# ---------------------------------------------------------------------------------
# Output --> Line A \n Line B
print("Line A \\n Line B")

# ***********Print these following lines***************
# this is \\ double backslash
# this is /\/\/\/\ mountain 
# he is   awesome (use escape sequence insted of manual sapces)
# \" \n \t \' (Print this as an input)

print("This is \\\\ double backslash")
print("This is /\\/\\/\\/\\ mountain back")
print("He is\taswsome")
print("\\\" \\n \\t \\\'")
print(r"\" \n \t \'") # raw string

# ---------------------------------------------------------------------------------
# Escape sequence
print("Hello \"Expertizo\" Team")
print('Hello \'Expertizo\' Team')
print("Hello world \\")
print("Helloo\b world")
print("Hello\tworld")
print("Hello\nworld")

