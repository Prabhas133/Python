#Inheritance
#Single inheritance is single parent and two child 
'''
class RBI():#parents class
    cash = 100000
    def avaiable_cash(cls):
        print("Avaiable Cash is : ",cls.cash)
        print("Avaiable Cash is : ",RBI.cash)#Cash in RBI of parents
class SBI(RBI):#child class - 1
    pass
class HDFC(RBI):#child class - 2
    cash = 50000
    def new_cash(cls):
        print("New Cash is : ",cls.cash+cls.cash)
        print("New Cash is : ",cls.cash+RBI.cash)#Cash in RBI of child - 2
a = HDFC()
a.avaiable_cash()
a.new_cash()'''

#OR
'''
class RBI():#parents class
    cash = 100000
    def avaiable_cash(cls):
        #print("Avaiable Cash is : ",cls.cash)
        print("Avaiable Cash is : ",RBI.cash)#Cash in RBI of parents
class SBI(RBI):#child class - 1
    cash = 60000
    def new_cash(cls):
        #print("New Cash of child 1 is : ",cls.cash+cls.cash)
        print("New Cash of child 1 is : ",cls.cash+RBI.cash)
class HDFC(RBI):#child class - 2
    cash = 50000
    def new_cash(cls):
        #print("New Cash of child 2 is : ",cls.cash+cls.cash)
        print("New Cash of child 2 is : ",cls.cash+RBI.cash)#Cash in RBI of child - 2

a = SBI()
b = HDFC()
a.avaiable_cash()
a.new_cash()
b.avaiable_cash()
b.new_cash()'''

#muitple inheritance is two parents and one child
'''
class Father():
    h = float(input("Enter the Height in (meters) : "))
    def height(cls):
        print("Height is : ",cls.h)
class Mother():
    w = int(input("Enter the Weight in (kgs): "))
    def weight(cls):
        print("Weight is : ",cls.w)
class Child(Father,Mother):
    d = input("Enter the DOB in (Date-Month-Year): ")
    def DOB(cls):
        print("DOB of child is : ",cls.d)
a = Child()
a.height()
a.weight()
a.DOB()'''

#muitple level is grand parent and parent and child
'''
class grandparent():
    land = "10 acres"
    def l(c):
        print("Acres of land is :",c.land)
class parent(grandparent):
    house = "10 floor Building"
    def h(h):
        print("House is :",h.house)
class child(parent):
    car = "BMW X6"
    def c(ca):
        print("Car is : ",ca.car)
a = child()
a.l()
a.h()
a.c()'''

#hierarchical inheritance 
#is inheritance where one parent class is inheritaned by muitple child class
'''
class Employee():#parent
    c = "IBM"
    def co(cls):
        print("Company name is : ",cls.c)
class Trainer(Employee):#child - 1
    te = "teachs the code"
    def t(cls):
        print("Trainer is",cls.te)
class Developer(Employee):#child - 2
    de = "develops the code"
    def t(cls):
        print("Developer is",cls.de)
a = Trainer()
a.co()
a.t()
b = Developer()
b.co()
b.t()'''

#Hybrid inheritance
'''
class person():
    def p(self):
        print("Name of the person is Prabhas Naidu")
class Trainer(person):
    def t(self):
        print("Trainer will Teachs the course")
class student(person):
    def s(self):
        print("Study the course")
class program_manager(Trainer,student):
    def details(self):
        print("Manager the schedule of the classes ")
a = program_manager()
a.details()
a.t()
a.s()
a.p()
'''

#super() function.
'''class parent():
    def _init_(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def _init_(self,name,age):
        self.age=age
        self.name=name
        print("chid constructor")
a=child("Prabhas",21)
print(dir(a))
print(a.name)
print(a.age)
#output -

a=child("sai",21)
TypeError: child() takes no arguments'''



class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,age,name):
        self.age= age
        super().__init__(name)
        print("child constructor")
a = child("Prabhas",22)
print(dir(a))
print(a.name)
print(a.age)





































