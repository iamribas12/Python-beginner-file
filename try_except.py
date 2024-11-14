#Try and except
while(True):
    try:
        a = int(input("Enter : "))
        c = 1/a
        print(c)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as f:
        print(f)


#Try with Else
