#Encapsulation
#public data
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''

#_protected data
'''
class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__private data
'''
class parent():
    __privatedata="Prabhas"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''

'''
class parent():
    name = "Prabhas"
    _mailid = "ddhanikondaprabhas@gmail.com"
    __salary = 100000
class child(parent):
    def method(self):
        print(self.name,self._mailid,self._parent__salary)#We want call the private data u should mention main class name.
a = child()
a.method()'''
