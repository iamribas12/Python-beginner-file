Std_Name = input("Enter your name : ")

marks = int(input("Enter Marks: "))
if(marks >= 90):
    print("Grade of {0} is A".format(Std_Name))
elif(marks >= 80):
    print("Grade of {0} is B".format(Std_Name))
elif(marks >= 70):
    print("Grade of {0} is C".format(Std_Name))
else:
    print("Grade of {0} is D".format(Std_Name))
