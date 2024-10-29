# oops(Object oriented programming)

# class Number:
#     def sum(self):
#         return self.a + self.b
    
# num=Number()
# num.a=12
# num.b=34
# s=num.sum()
# print(s)


# #Example of Railway form
# class RailwayForm:
#     formType="RailwayForm"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")

# harrysApplication=RailwayForm()
# harrysApplication.name="Harry"
# harrysApplication.train="Rajdhani Express"
# harrysApplication.printData()




# # #Example of a Game
# class Remote:
#     pass

# class Player:
#     def moveRigh(self):
#         pass
#     def moveLeft(self):
#         pass
#     def moveTop(self):
#         pass

# remote1=Remote()
# player1=Player()
# if(remote1.isLeftPressed()):
#     player1.moveLeft()


# class Employee:
#     company="Google"
#     salary=100

# harry=Employee()
# rajni=Employee()
# print(harry.company)
# Employee.company="YouTube"
# print(harry.company)

# #Creating instance attribute salary for both objects  (attribute=adjective,property)
# harry.salary=300
# rajni.salary=400
# print(harry.salary)
# #instance attribute(object attribute) is given priority over the class attribute. (instance=object)
# #print(harry.address) #throws an error as address attribute isn't present in both class and instance


#use of self parameter
class Employee:
    company="Google"
    def getSalary(self):
        print("Salary is 100k")

harry=Employee()
harry.getSalary()

