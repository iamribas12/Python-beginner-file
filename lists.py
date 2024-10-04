# List is the collection of various data of multiple data types in a single variables. 
# Lists are Mutable(can be modified)

lists = [43,53,'sabir',3.5]
def lis(a):
    for i in range(0,len(a)):
        print(a[i],end=" ")

lis(lists)


inp = list(map(int,input("enter the integer values: ").split()))
print(inp)

for i in range(0,len(inp)):
    print(inp[i], end= " ")

#list comprehension:-l
list = [23,54,64,24,64,633,67]
list1 = [it for it in list if it>55]

print(list1)
print(tuple(list1))
print(set(list1))