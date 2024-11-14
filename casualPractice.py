# f = open("again.py","r")

# # data = f.read() #we can use literal as a pararmeter into the read() function,
# # #it will only print till the index number which is assigned as the paramete.
# print(data)
# print(f.read(4))

# f.close()

# def concat(*args,sep=" "):
#     return sep.join(args)

# print(concat("mohammed","Sabir","alam"))

# #List comprehension


# combs = [ i for i in range(0,5) if i%2==0]
# print(combs)
        

with open("locka.txt","r+") as f:
    data = f.read()

new = data.replace("Java","Python")

# if "learning" in data:
#     print("yes \"learning\" is exists in the file")

print(new)

with open("locka.txt","w") as f:
    f.write(new)

with open("locka.txt","r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("found")
    else:
        print("Not found")