class Player:
    teamName="LIverPool"
    teamMembers=[]

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.formerTeams=[]
        self.teamMembers.append(self.name)


    def tax(self):
        return (self.salary*0.2)

    def salaryperDay(self):
        return (self.salary/30)


p1=Player("Mark",30000)
p2=Player("Steve",49000)

print("Name:" ,p1.name)
print("TAX:",p1.tax())
print("DAY_SALARY",p1.salaryperDay())
print("Team Members:")
print(p1.teamMembers)