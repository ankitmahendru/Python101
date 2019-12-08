# Examples of Strings
str1 = 'hello'
str2 = "world"
str3 = "I'm going for a run"

# Printing the strings
print("Hello World!!")
print('Hello World!!!')

# Escape Sequences
print('hello \nworld')
print('hello \t world')

# Length of a String
print(len(str1))
print(len(str3))

#
# String indexing and string slicing
#

myString = "Hello World"
print(myString[6])

# Reverse Indexing
print(myString[-2])

# Slicing
myString = 'abcdefghijk'

print(myString[2:])

print(myString[:3])

print(myString[3:8])

# Step Size

print(myString[::2])

print(myString[2:9:3])

# Reverse a String

print(myString[::-1])

#
# String Properties
#

# Immutablility
name = "Samwise Gamgee"

# name[0] = 'P' # This won't work

last_letters = name[1:]

print(last_letters)

last_letters = "P" + last_letters

print(last_letters)

last_letters = last_letters * 10

print(last_letters)

#
# String Methods
#

# Upper Method

print(name.upper())

# Lower Method
print(name.lower())

# Split Method
print(name.split('A'))

# Format Method
print('Name entered is {}'.format(name))

print("The {2} {1} {0}".format("fox", "brown" , 'quick'))

print('The {q} {b} {f} '.format(f='fox', b="brown", q="Quick"))

# F strings

print(f"Hello , {name}")

age = 60

print(f"Name = {name} ,  Age = {age}")