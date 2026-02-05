class calculator:
    def __init__(self, n):
        print("your answer here")
        self.n = n
    
    def getInfo(self):
        print(f"cub of {self.n} is {self.n*self.n*self.n}")

    def squre(self,getInfo):
        print(f"squre of {self.n} is {self.n*self.n}")

z = calculator(int(input("enter the number: ")))
z.getInfo()
z.squre()
    