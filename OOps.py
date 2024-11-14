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

class Student:
    def __init__(self,name,eng,hindi,maths):
        self.name = name
        self.eng = eng
        self.hindi = hindi
        self.maths = maths

    def get_avg(self):
        return (self.hindi + self.eng + self.maths)/3
    
stud1 = Student("sabir",78,48,68)

print(stud1.get_avg())