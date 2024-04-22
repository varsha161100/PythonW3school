# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class


class stu:

    def __init__(self, id, name):
        self.id=id
        self.name=name

    def display(self):
        print("Student ID: {0} \n Student Name: {1} \n**********".format(self.id,self.name))

class subject(stu):
    # def __init__(self, sub1, sub2):
    #     self.sub1=sub1
    #     self.sub2=sub2

    def show(self):
        #  print("Subject 1: {0} \t Subject 2: {1}".format(self.sub1,self.sub2))
        print("hello")

obj1=stu(101,"varsha")
obj2=stu(102,"ruchi")



obj1.display()
obj2.display()


s1=subject(101,"hena")
s1.display()
s1.show()



# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id 

#   def showDetails(self):
#     print(f"The name of Employee: {self.id} is {self.name}")

# class Programmer(Employee):
#   def showLanguage(self):
#     print("The default langauge is Python")


# e1 = Employee("Rohan Das", 400)
# e1.showDetails()
# e2 = Programmer("Harry", 4100)
# e2.showDetails()
# e2.showLanguage()