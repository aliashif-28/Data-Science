class information:
    name = "ashif"
    def teacher(self,sub):
        self.sub = sub     
class branch(information):
    branch = "computer science"
    def bran(self,diva,divc):
        self.diva = diva
        self.divc = divc
class student(branch):
    student_number_diva = 56
    student_number_divc = 60
    def count(self):
        print(f" Branch {self.branch}\n Teacher name is {self.name}\nTake subject is{self.sub}\n its take a two division {self.diva} & {self.divc}\n student number of division {self.diva} = {self.student_number_diva} and {self.divc} = {self.student_number_divc}\nTotal number of student {self.diva} & {self.divc} = {self.student_number_diva + self.student_number_divc} ")
c = student()
c.teacher("python")
c.bran("A", "C")
c.count()