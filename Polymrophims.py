#Polymrophims
#Operator overloading
#it shows different behaviour to the different data types

#Methods
'''
a = 2;b = 4
print(a+b)
print(a.__add__(b))#using built in methods
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(10))
#not method for the division print(a.__div__(2))
print(a.__pow__(2))
print(a.__ge__(7))
print(a.__le__(10))
print(a.__eq__(2))'''

#for list
'''
a = [2,3,4,5,6,7,8];b = [4,5,6,7,8,9,10]
print(a+b)
print(a.__getitem__(2))#item index
print(b.__getitem__(3))'''

#for string
'''
a = "python" ; b = "codegnan"
print(a.__add__(b))
print(a.__add__(" "+b))#with space output
print(a.__add__(" "+b).title())
print("Prabhas".__add__(" "+"Naidu"))'''

#operator overriding
'''
class A():
    def __init__(self,a):
        self.a = a
    def __add__(self,value):
       return  self.a * value.b #if we give the self,self in positional arguments throughs error , we should give different argument names like self,value then it is take values operator done.
class B():
    def __init__(self,b):
        self.b = b
x = A(4)
y = B(5)
#x = 4
#y = 5 without classes we are passing the values then it add 4 + 5 =9
print(x+y)'''

#Method overloading
'''
class n():
    def sum(self,a=None,b=None,c=None):
        if a != None and b != None and c != None :
            print("The sum is : ",a+b+c)
        elif a != None and b != None:
            print("The product is : ",a*b)
        else:
            print("program ends...")
a = n()
a.sum()
a.sum(2,4,6)
a.sum(6,3)'''#method is sum remaining overloading like values passing ..

#method overriding
'''
class Animal():
    def speak(self):
        print("Animals can make sounds")
class dog():
    def speak(self):
        print("dog barks")
a = Animal()
b = dog()
a.speak()
b.speak()'''


#Task
#vehicle details
'''
class vehicle():
    def details(self):
        print("Vehicle details")
class vehicleCar(vehicle):
    def __init__(self):
        self.model = "BMW X6"
        self.color = "Black matfinish"
        self.myear = 2024
    def details(self):
        print("Car Details")
        print(f"Model : {self.model} , Color : {self.color} , Myear : {self.myear}")
class vehicleBike(vehicle):
    def __init__(self):
        self.model = "Ninja H2R"
        self.color = "Black"
        self.myear = 2022
    def details(self):
        print("\n")
        print("Bike Details")
        print(f"Model : {self.model} , Color : {self.color} , Myear : {self.myear}")
x = vehicleCar()
y = vehicleBike()
x.details()
y.details()'''

#OR
'''
class Car():
    def vehicle(self):
        print("Thar")
class Bike():
    def vehicle(self):
        print("H2R")
a = Car()
b = Bike()
a.vehicle()
b.vehicle()'''
        
        
