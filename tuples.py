#Tuples: tuples are the built in data type that lets us to create immutable sequence.

tup = (3,5,6,7,3)

print(tup)
'''
tup[2] = 3 #its not permissible in python to modify the tuples
print(tup)
'''

lists = [23,534,5,34,3,5,343,2]

print(tuple(lists))
print(type(lists),type(tup))

