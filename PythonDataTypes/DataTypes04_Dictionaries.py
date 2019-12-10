#
# Dictionaries in Python
#

my_dict = {'key1': 'value1', 'key2' : 'value2'}

print(my_dict['key1'])

dict = {'k1' : 123 , 'k2' : 'String', 'k3' : [1,2,3], 'k4' : {'k41' : 100} }

print(dict['k4']['k41'])

mylist = dict['k3']

print(mylist)

letter = mylist[2]

print(letter)

# OR

print(dict['k3'][2])


# Adding new Key Value

dict['k5'] = 9009

print(dict)

# Replacing Key Value

dict['k5'] =  900

print(dict)

#
# Some functions on Dictionaries
#

print(dict.keys())

print(dict.values())