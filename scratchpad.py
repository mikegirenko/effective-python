from datetime import datetime, timezone
import sys

print(sys.version_info)

empty_list = []
assert not empty_list

not_empty_list = ["Hello"]
assert not_empty_list

a_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("First four:", a_list[:4])  # same as a_list[0:4]
print("Last four:", a_list[-4:])  # same as a_list[4:len(a_list)]
print("Middle two:", a_list[3:-3])
print("Slicing using negative numbers:", a_list[-1])  # last member of the list

# Compute a square of each number on a list
list_of_numbers = [1, 2, 3, 4, 5]
for number in list_of_numbers:
    print(number ** 2)
# The same using list comprehension
squares = [number ** 2 for number in list_of_numbers]
print(squares)

for i in range(5):
    print(i)

# using enumerate to get index of an item on the list
flavor_list = ["vanilla", "pecan", "strawberry"]
for i, flavor in enumerate(flavor_list):
    print(i + 1, flavor)  # + 1 is optional, if not provided, 0 will be used

for i in range(3):
    print("Loop:", i)
    if i == 1:
        break  # using break here will not print 'Printing else'. If not using break, 'Printing else' will print
else:
    print("Printing else")

# try:
#     var = 3 / 0  # it results is ZeroDivisionError: division by zero
# finally:
#     print("ZeroDivisionError")  # but this still prints

try:
    file = open("non_existing_file.txt")  # it results in FileNotFoundError: [Errno 2] No such file or
    # directory: 'non_existing_file.txt'
except FileNotFoundError:  # it will catch FileNotFoundError
    print("I am handling FileNotFoundError and printing text without raising exception. It helps when you dont know "
          "if this file exists")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:  # it will catch ZeroDivisionError and return 0
        return 0


print("Printing", divide(3, 0))


def print_greeting(greeting, *name):  # using Variable Positional Argument *name
    print(greeting, name)


greeting = "Hey"
name = "Mike"
print_greeting(greeting, name)  # it prints Hey ('Mike',)
print_greeting(greeting)  # it prints Hey ()


def print_greeting_again(greeting, name, end="!"):  # using Keyword Arguments with default value
    print(greeting, name, end)


greeting = "Hello"
name = "Jake"
end = "?"
# calling with Keyword Arguments with default value
print_greeting_again(greeting=greeting, name=name, end=end)  # it prints Hello Jake ?
print_greeting_again(greeting=greeting, name=name)  # it prints Hello Jake ! because default value ! is used
print_greeting_again(name=name, greeting=greeting, end=end)  # it prints Hello Jake ? even if arguments order is
# different compared to function definition


class MyObject():
    def __init__(self):
        self.public_field = "this is a public field"
        self.__private_field = "this is a private field"  # a private field

    def get_private_field(self):  # this gives access to a private field
        return self.__private_field


obj = MyObject()
assert obj.public_field == "this is a public field"  # this assertion is true
# assert obj.private_field == "this is a private field"  # this errors out with
# # AttributeError: 'MyObject' object has no attribute 'private_field'
assert obj.get_private_field() == "this is a private field"  # this assertion is true
#  in general, use public fields, "We are all consenting adults here"


time_now = datetime.now()
print(time_now)
