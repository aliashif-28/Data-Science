while(True):
    name = input("If your name is a first, middle, and last name then click y. If your name is a first and last name then click n: ")
    if(name == "y"):
        a = input("enter your name: ")
        part = a.split(" ")
        print(f"your first name is {part[0]}")
        print(f"your middle name is {part[1]}")
        print(f"your last name is {part[2]}")
    elif(name == "n"):
        a = input("enter your name: ")
        part = a.split(" ")
        print(f"your first name is {part[0]}")
        print(f"your last name is {part[1]}")
    else:
        print("invalid input please input only y ya n")

