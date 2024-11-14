# # # WAP to check if a number entered by the user is odd or even

# # num = int(input("Enter the number : "))

# # if(num%2 == 0):
# #     print(f"{num} is Even number")
# # else:
# #     print(f"{num} is Odd Number")



# # #WAP to find the greatest of 3 numbers entered by the user.

# # print("Enter 3 number to compare : ")

# # num1 = int(input())
# # num2 = int(input())
# # num3 = int(input())

# # if(num1 >num2 and num1>num3):
# #     print(f"{num1} is greatest of given 3 numbers")
# # elif(num2>num1 and num2>num3):
# #         print(f"{num2} is greatest of given 3 numbers")
# # elif(num3>num1 and num3>num2):
# #          print(f"{num3} is greatest of given 3 numbers")
# # else:
# #       print("Alhamdulillah allah ne dimag diya hai na, Khudka dimag lagao")


# # #WAP to check if a number is a multiple of 7 or not

# # numm = int(input("Enter the number :"))
# # if(numm%7==0):
# #       print(f"{numm} is multiple of 7")
# # else:
# #       print(f"{numm} not multiple by 7")

# # # ---------------------------------------------------------------------------------------

# # #WAP to add ask to the user his 3 fvrt movies name and store in list
# # movies = []
# # for i in range(1,3+1):
# #       name = input("enter {0} movie : ".format(i))
# #       movies.append(name)

# # print(movies)


# #WAP to check is a list is palindrome or not.

# list1 = [12,45,49,45,12]
# list2 = list1.copy()
# list2.reverse()


# if(list1 == list2):
#     print("it is a palindrome")
# else:
#     print("its not a palindrome")




#Q: print the multiplication table of a number n.
n = int(input("enter n:"))

for i in range(1,11):
    print(i*n)


def fun(n,idx,char):
    for i in n[idx:]:
        print(i,end="")
        if i == char:
            break
    print(end=" ")
dola = "MyNameisSabirAlam"

fun(dola,0,"y")
fun(dola,2,"e")
fun(dola,6,"s")
fun(dola,8,"r")
fun(dola,13,"m")
