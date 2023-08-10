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
