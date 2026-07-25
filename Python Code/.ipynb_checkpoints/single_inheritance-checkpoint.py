class information:
    name = input("enter your name: ")
    sub = input("enter your subject: ")
    def teacher(self):
        print(f"Teacher name is {self.name} and subject is {self.sub}")
class division(information):
    div = input("enter your division: ")
    def divis(self):
        print(f"Teacher name is {self.name} or Subject is {self.sub} and division {self.div}")
a = division()
print(a.divis())