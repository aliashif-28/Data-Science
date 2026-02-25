def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(great(int(input("enter the first number: ")),int(input("enter the first number: ")),int(input("enter the first number: ",))))