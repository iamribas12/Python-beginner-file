# #  FILE HANDLING through python


#                         # READ
# # r = open("README.md","a") 

# # data = r.read()
# # data = r.readline()
# # print(data)

# # print(data)
# # r.close()

#                         # write
# # There are two ways to write in the file using python I/O 
# #i] "w" : overwrite
# #ii] "a": append


# # r.write("\nassalamualaikum ya maasharal muslimeen")

# # r.close()

# with open("README.md","r") as f:
#     print(f.read())



#FOR DELETING the FILE

# import os

# os.remove("REE.md")


with open("locka.txt","r") as f:
    lines = f.readlines()
    print(lines)
    