#Abstraction 
#The method declare without implementation is called abstract method.
'''
class A():
    def method(self):
        pass
obj = A()
obj.method()'''

'''
from abc import ABC,abstractmethod
class A():
    def method(self):
        print("Pyhton")
o = A()
o.method()'''

'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method(self):
        print("Data")
o = A()
o.method()'''

''' 
from abc import ABC,abstractmethod
class A(ABC):
    #@abstractmethod
    def method(self):
        pass
    def method1(self):
        print("Python")
    #@abstractmethod
    def method2(self):
        pass
class B(A):
    def method(self):
        print("Data Science")
    def method2(self):
        print("Machine Learning")
        
o = B()
o.method()
o.method1()
o.method2()'''



                 




                   
