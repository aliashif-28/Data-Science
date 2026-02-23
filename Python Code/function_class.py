class ashif:
    name = input("enter your name: ")
    fname = input("enter your father name: ")
    mname = input("enter your mother name: ")
    mno = int(input("enter your moblie number: "))
    gender = input("enter your gender (Male / female / other): ")
    add = input("enter your full addresh: ")
    pin = int(input("enter the pin code: "))

    def getInfo(self):
        print(f'''hello !\nmr.. {self.name}\nyour fathe name is Mr.. {self.fname}. 
        He is a good man. \n your mother miss.. {self.mname}.she is a house wife.\n 
        if you need any help then you call on this number is {self.mno} and they will surely help you.
        \n mr.. {self.name} your are {self.gender}.\n you live in {self.add}. {self.pin}''')
    
    
    def greet(self):
        print(f"\n\nmr.. {self.name} your full information here\n\n")


ali = ashif()
ali.greet()
ali.getInfo()