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
print("Slicing using negative numbers", a_list[0])

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


def divide (a, b):
    try:
        return a / b
    except ZeroDivisionError:  # it will catch ZeroDivisionError
        return 0


print("Printing", divide(3, 0))
