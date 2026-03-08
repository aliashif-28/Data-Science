while(True):
    class first_user:
        print("1 = rock")
        print("2 = paper")
        print("3 = scissors")
        def getInfo(self):
            self.first_user_name = input("first user enter your name: ")
            self.second_user_name = input("second user enter your name: ")
            print(self.first_user_name)
            self.first_number = int(input("choice the number: "))
            print(self.second_user_name)
            self.second_number = int(input("choice the number: "))
        def greet(self):
            if(self.first_number == self.second_number):
                print("mathch is drow")
            elif(self.first_number == 1 and self.second_number == 2):
                print(self.second_user_name, "is a winner")
            elif(self.first_number == 1 and self.second_number == 3):
                print(self.first_user_name,"is a winner")

            elif(self.first_number == 2 and self.second_number == 1):
                print(self.first_user_name,"is a winner")
            elif(self.first_number == 2 and self.second_number == 3):
                print(self.second_user_name,"is a winner")

            elif(self.first_number == 3 and self.second_number == 1):
                print(self.second_user_name,"is a winner")
            elif(self.first_number == 3 and self.second_number == 2):
                print(self.first_user_name,"is a winner")
            else:
                print("plzz enter the valid number")
    allt = first_user()
    allt.getInfo()
    allt.greet()
    print("for exit this game type n letter")
    a = input("for continue this game enter any letter skip only one letter n(y/n)")
    if(a == "n"):
        break
    else:
        print("\n")
        continue   