#
# FILES
#

myfile = open('test.txt')

print(myfile.read())


# o/p
#Hello World!
#This is the Second Line.
#This is the third line.

myfile.seek(0)

contents = myfile.read()