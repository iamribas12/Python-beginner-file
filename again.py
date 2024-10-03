# while(True):
    
#     print("enter q for quit")
#     intt = input("Enter no: ")
#     try:
#         if intt == 'q':
#             break
#         elif int(intt) >= 30:
#             print("You enter the no. greater than 30")
#         else:
#             print("You entered the no. less than 30")
#     except Exception as f:
#         print(f)



def greet(name):
    print(f"Assalamualaikum habibi,{name}")


# if you want to during the runnig time of module line no. 23 and 24 not to -
# be run then we must have the give the below conditional statement during the execution time.
if __name__ == "__main__":
    name = input("enter your name: ")
    print(name)