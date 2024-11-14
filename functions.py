# def multiplication_table(n):
#     for i in n:
#         print(i,end=" ")

# lis = ["sabir","sohail","sarfraz"]

# multiplication_table(lis)

# listt = ["sabir","sohail","sarfraz","arman"]

# def length(n):
#     return len(n)


# print(length(listt))
# print(length(lis))



#Recursion: when a function call itself repeatedly


def recursion(n):
    if n==0:
        return
    print(n)
    recursion(n-1)

# recursion(5) #output:- 5,4,3,2,1


#factorial through recrusion

def fact(n):
    if n==0 or n==1:
        return 1
    return n*(fact(n-1))

print(fact(4))

#Q:- write a recursive function to calculate the sum of first n natural numbers.

def add(n):
    if n == 0:
        return 0
    return n+(add(n-1))


print(add(5))

#Q:- write a recursive function to print all elements in a list.

lisst = ["sabir","alam","arman"]

def appen(list,idx):
    if (idx == len(list)):
        return
    print(list[idx])
    appen(list,idx+1)
    

appen(lisst,0)