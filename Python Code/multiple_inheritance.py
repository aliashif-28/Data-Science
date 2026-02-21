class father:
    f_name = input("enter first name of your father: ")
    f_tital = input("enter last name of your father: ")
    def works(self,work):
        self.work = work

class mother:
    m_name = input("enter your mother name: ")
    def skills(self,skill):
        self.skill = skill

class interduse(father , mother):
    name = input("what is your first name: ")
    def interduse_your_self(self):
        print(f"mr {self.name} {self.f_tital} your are  {self.skill} ")
c = interduse()
c.works(input("what does your father do: "))
c.skills(input("what does your mother do: "))
c.interduse_your_self()