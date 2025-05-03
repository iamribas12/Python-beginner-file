# class circle:
#     def __init__(self,radius):
#         self.radius = radius #instance attribute
    
#     def get_area(self):# instance method
#         area = 3.14 * (self.radius**2)
#         print(f"Area of the circle of radius {self.radius} are: {area}")
    
#     def get_perimeter(self):
#         perimeter = 2*3.14 *(self.radius)
#         print(f"perimeter of the circle of radius {self.radius} are: {perimeter}")
    

# circle1 = circle(2)
# circle1.get_area()
# circle1.get_perimeter()

# Q.2

# from datetime import date
# class person:
#     def __init__(self,name,country,dob):
#         self.name = name
#         self.country = country
#         self.dob = dob
    
#     def get_age(self):
#         today = date.today()
#         age = today.year - self.dob.year

#         if today < date(today.year,self.dob.month,self.dob.day):
#             age -= 1
#         return age

# # print(date(2006,6,3))
# # print(date.today())

# person1 = person("sabir","india",date(2026,3,6))
# print(person1.get_age())

# Q.3

# class calculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def add(self): 
#         add = self.num1 + self.num2
#         print(add)
#     def mul(self):
#         mul = self.num1 * self.num2
#         print(mul)
#     def sub(self):
#         sub = self.num1 - self.num2
#         print(sub)
#     def div(self):
#         div = self.num1 / self.num2
#         print(div)
    
# num1 = calculator(5,3)

# num1.sub()

import math

class shape:
    def get_area(self):
        pass
    def get_perimeter(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius **2
    def get_perimeter(self):
        return 2* math.pi * self.radius

class rectangle(shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)
    

class triangle(shape):
    def __init__(self,b,h,s1,s2,s3):
        self.b = b
        self.h = h
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def get_area(self):
        return 0.5 * self.b * self.h
    def get_perimeter(self):
        return self.s1 + self.s2 + self.s3
    

tri1 = triangle(5,6,8,3,6)
print(tri1.get_area())

cir1 = circle(5)

print(cir1.get_perimeter())


