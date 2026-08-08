#OOPS
#1.A class contains attributes , variables , methods,functions that can be maiplucate the data.
#2.A class is the blueprint of the object
#3.Method are the functions that can be define inside the body of the class
#4.An object is an intiation of the calss.

#FOUR PILLARS

#Polymrophims
#contains four types
#1.operator overloading 2.operator overriding 3.method overloading 4.method overriding

#Intheritance
#contains five types
#1.single 2.multiple 3.multiple level 4.hybrid 5.highardical

#encaplusation
#contains three types 
#1.Public data,_Proctecteddate,__privatedata

#Abrascation
#contains two types
#1.abrscat class , abrsact method

#Syntax
'''
class classmate():
    #attributes
    name = "Prabhas"
    age = 22
    place = "Vija"
    def fname(methods_name):
        print("Statements......")
a = classmate()
a.fname()'''


#class declaration
'''
class details():
    name = "Prabhas"
    age = 22
    place = "vija"
    def display(self):
        print(f"Name : {self.name}, Age : {self.age}, Place : {self.place}")
    def any(nani):
        print(f"Name : {nani.name}, Age : {nani.age}, Place : {nani.place}")
a = details()
#print(dir(a))
a.display()
a.any()'''

#object intantiation
'''
class details():
    def data(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = details()
#print(dir(a))
a.data("Prabhas",22,"vijayawada")#assing the data to the name,age,place
a.display()
b = details()
b.data("Sumanth",21,"Vijayawada")
b.display()'''

#object initialization
'''class details():
    #creating constructor ,we give data directly in the class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = details("Prabhas",22,"Vijayawada")
a.display()'''

#runtime input - 3rd methods
'''
class details():
    #creating constructor ,we give data directly in the class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
name = input()
age = int(input())
place = input()
a = details(name,age,place)
a.display()'''
#OR
'''
class details():
    #creating constructor ,we give data directly in the class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = details(input("name:"), int(input("Age:")),input("place:"))
a.display()'''

#OR
'''
class details():
    #creating constructor ,we give data directly in the class
    def __init__(self):
        self.name = input("name:")
        self.age = int(input("Age:"))
        self.place = input("place:")
    def display(self):
        print(self.name,self.age,self.place)
a = details()
a.display()'''

#diff b/w _ and __
#when user wants to create a variable with __ our python interpertor treat has special variable to avoid names confilts, methods and inner classes.
'''
class employee():
    def __init__(self):
        self.name = input("Name : ")
        self._mailid = input("Email : ")#name and mailid public variables
        self.__salary = int(input("Salary : "))#it is private variable
a = employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)#throughs error
print(a._employee__salary)#we should it call with class name and after that private variable like this "_employee__salary"
'''    

#Task
'''
while True:
    class employee():
        def __init__(self):
            print("Employee 1")
            self.name = input("Name : ")
            self._mailid = input("Email : ")#name and mailid public variables
            self.__salary = int(input("Salary : "))#it is private variable
    class employee1():
        def __init__(self):
            print("\n")
            print("Employee 2")
            self.name = input("Name : ")
            self._mailid = input("Email : ")#name and mailid public variables
            self.__salary = int(input("Salary : "))#it is private variable
    class employee2():
        def __init__(self):
            print("\n")
            print("Employee 3")
            self.name = input("Name : ")
            self._mailid = input("Email : ")#name and mailid public variables
            self.__salary = int(input("Salary : "))#it is private variable
    a = employee()
    b = employee1()
    c = employee2()
    #print(dir(a))

    #print(a.__salary)#throughs error
    o = int(input(Choose the employee details
                                        1.Employee1 
                                        2.Employee2
                                        3.Employee3
                                        Enter the option - ))

    if o == 1:
        print(a.name)
        print(a._mailid)
        print(a._employee__salary)
    elif o == 2:
        print(b.name)
        print(b._mailid)
        print(b._employee1__salary)
    elif o == 3:
        print(c.name)
        print(c._mailid)
        print(c._employee2__salary)
    else:
        print("Invalid option")
        pass
        print("\n")'''












        
        

        

