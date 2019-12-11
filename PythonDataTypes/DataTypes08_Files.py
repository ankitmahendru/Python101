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

contents = myfile.readline()

print(contents)

myfile.close()

with open('test.txt', mode= 'r' ) as fa :
        print(fa.read())

with open('test.txt', mode='a') as fb:
        fb.write('\n This is the Forth Line')

with open('test2.txt', mode='w') as fc:
    fc.write('New File Created')
with open('test2.txt') as fd :
    print(fd.read())

