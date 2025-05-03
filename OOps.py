# #cREATING CLASS

# class student:
#     name = "sabir"


# #CREATING OBJECT
# stud = student()

# print(stud.name)

#   __init__ is the constructer

# class student:
#     college = "SVIMS"
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name

#     #Metods
#     def hello(self):
#         print("marhaban",self.name)

# s1 = student("sabir",19)

# print(s1.college) # OR
# print(student.college)

# s1.hello()

# class Student:
#     def __init__(self,name,eng,hindi,maths):
#         self.name = name
#         self.eng = eng
#         self.hindi = hindi
#         self.maths = maths

#     def get_avg(self):
#         return (self.hindi + self.eng + self.maths)/3
    
# stud1 = Student("sabir",78,48,68)

# print(stud1.get_avg())

# class account:
#     def __init__(self,bal,acc):
#         self.bal = bal
#         self.acc = acc
    
#     def get_balance(self):
#         return self.bal
    
#     def credit(self,amount):
#         self.bal += amount
#         print(f"From Account NO.{self.acc} Rs.{amount} Credited \nCurrent Balance is {self.get_balance()}")

#     def debit(self,amount):
#         self.bal -= amount
#         print(f"From Account NO.{self.acc} Rs.{amount} Credited \nCurrent Balance is {self.get_balance()}")


# sabir = account(10000,2642723086)
# sabir.debit(3000)
# sabir.credit(500)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def get_average(self):
#         total = 0
#         for i in self.marks:
#             total +=i
#         return total / len(self.marks)  # Divide by the actual number of marks

# # Marks and student instance should be outside the class body
# marks = [78, 53, 64]
# s1 = Student("Sabir", marks)
# print(s1.get_average())

# del s1

# print(s1.get_average())   # DEL keyword is used for deleting the properties even any object.


# Inheritance >> •Single-level inheritance

# class car():
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def brek():
#         print("Car has stopped")
    

# class toyota(car):
#     def __init__(self,name):
#         self.name = name
    
# car1 = toyota("fortunar")
# car1.start()


#Inheritance >> Multi-level inheritance

# class car():
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def brek():
#         print("Car has stopped")
    

# class toyota(car):
#     def __init__(self,brand):
#         self.brand = brand
    
#     @staticmethod
#     def get_sitting():
#         print("Four Sitter Car")

# class Fortuner(toyota):
#     def __init__(self, EngineType):
#         self.Type = EngineType
        

# car1 = Fortuner("Petrol")

# Fortuner.start()
# Fortuner.get_sitting()




# Using of SUPER() method

# class car():
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def brek():
#         print("Car has stopped")
    

# class toyota(car):
#     def __init__(self,brand):
#         self.brand = brand
#         super().__init__(type)
    
# s1 = toyota("Fortuner")

# s1.type = "Petrol"

# print(s1.type)

#Class method @classmethod
# class student:
#     name = "Rounak"
#     def __init__(self,name):
#         # self.name = name 
#         # student.name = name
#         self.__class__.name = name

# sa = student("sabir")
# print(sa.name)
# print(student.name)

# Property method @property

# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#     @property
#     def percentage(self):
#         return f"{(self.phy + self.chem + self.maths)/3}%"
    
# sabir = student(78,79,80)
# print(sabir.percentage)
# sabir.chem = 89
# print(sabir.percentage)


# Polymorphism

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(f"{self.real}i + {self.img}j")

    def add(self,num2):
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newReal,newimg)
    
num1 = complex(1,2)
num1.showNum()
num2 = complex(3,4)
num2.showNum()
num3 = num1.add(num2)
print("--------")
num3.showNum()