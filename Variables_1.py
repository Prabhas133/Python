Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=4;b=0
print(a+b)
4
a,b=2,3
print(a+b)
5
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(c)
10
print(a,b,c)
10 10 10
>>> k,l,m=2,3,4
>>> print(k+l+m)
9
>>> b,v,r = 1,2,3,4,5
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b,v,r = 1,2,3,4,5
ValueError: too many values to unpack (expected 3, got 5)
>>> #UN PACK
>>> d,g,h = (3,4,5)
>>> print(a,b,c)
10 10 10
>>> print(d,g,h)
3 4 5
>>> #no space
>>> first name = "pooja"
SyntaxError: invalid syntax
>>> first_name = "pooja"
>>> print(first_name)
pooja
>>> firstname = "pooja"
>>> print(firstname)
pooja
>>> fname = "Prabhas"
>>> lname = "Naidu"
>>> print(fname+" "+lname)
Prabhas Naidu
>>> print(fname,lname)
Prabhas Naidu
>>> #casesenstive
>>> name = "Codegnan"
>>> print(name)
Codegnan
>>> NAME = "Codegnan"
>>> print(NAME)
Codegnan
>>> Name = "Codegnan"
>>> print(Name)
Codegnan
>>> #delete keyword is del
>>> a = 4
>>> print(a)
4
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
