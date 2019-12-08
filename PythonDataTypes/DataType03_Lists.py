#
# Lists
#

my_list = [1, 2, 3]

print(my_list)

my_list=['STRING', 100, 23.2]

print(my_list)

print(len(my_list))

print(my_list[-1])

# Concatinating the lists

another_list = ['one' , 'two']

my_list = my_list + another_list

print(my_list)

my_list[0] = "string"

print(my_list)

# Add element to list

my_list.append('THREE')

print(my_list)

# Pop Method

pop_item = my_list.pop(0)

print(my_list)

print(f"Popped Item is {pop_item}")

# Sorting Lists

new_list = ['b', 'c', 'd', 'a', 'e', 'f']
num_list = [5, 6, 8, 1, 2, 0]

new_list.sort()
num_list.sort()

print(new_list)
print(num_list)

# Reversing Lists

new_list.reverse()
num_list.reverse()

print(num_list)
print(new_list)