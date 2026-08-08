#Without constructor
'''class student():
    name = input()
    age = int(input())
    branch = input()
    def studentdetails(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch
    def display(self):
        print(self.name,self.age,self.branch)
a = student()
a.display()'''

#OR
#With constructor
'''
class student():
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch
    def display(self):
        print(self.name,self.age,self.branch)
name = input()
age = int(input())
branch = input()
a = student(name,age,branch)
a.display()'''

'''
n = input().split()
d = []
a = []
for i in n:
    if i not in  d:
        d.append(i)
    else:
        a.append(i)
print(d)
print(a)'''

'''class c():
    n = "prabhas"
    a = 22
    b = "cse"
    def display(method):
        print("Satements........")
        print(method.n,method.a,method.b)
a = c()
a.display()'''

'''
a = list(map(int,input().split()))
t = int(input())
r = []
for i in a:
    if i > t:
        r.append(i)
print("[" + " ".join(map(str, r)) + "]")
'''

#operator overriding
'''
class A():
    def __init__ (self,a):
        self.a = a
    def __sub__(self,value):
        return self.a // value.b
class B():
    def __init__(self,b):
        self.b = b
a = int(input())
b = int(input())
x = A(a)
y = B(b)
print(x-y)

#OR

class A():
    def __init__ (self):
        self.a = int(input())
    def __sub__(self,value):
        return self.a // value.b#if we give the self,self in positional arguments throughs error , we should give different argument names like self,value
class B():
    def __init__(self):
        self.b = int(input())
x = A()
y = B()
print(x-y)'''


#method overloading
class n():
    def sum(self,a = 10,b = 15 ,c = 14):
        if a != 10 and b != 15 and c != 14 :
            print("The sum is : ",a+b+c)
        elif a != 20 and b != 25:
            print("The product is : ",a*b)
        else:
            print("program ends...")
a = int(input())
b = int(input())
c = int(input())
o = n()
#o.sum() if we not passes any value in sum , else statement
o.sum(a,b,c)
o.sum(a,b)#method is sum remaining overloading like values passing ..

