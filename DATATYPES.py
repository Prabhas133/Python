Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=10
print(type(a))#know which type of datatype is a .
<class 'int'>
b =4.5
print(type(b))
<class 'float'>
c="Codegnan"
print(type(c))
<class 'str'>
d = 4+7j
print(type(d))
<class 'complex'>
e = True
print(type(e))
<class 'bool'>
f = False
print(type(f))
<class 'bool'>


#DataTypes Conversion
int(6)
6
int(7.50)
7
int("Codegnan")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int("Codegnan")
ValueError: invalid literal for int() with base 10: 'Codegnan'
int(7+5j)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(7+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#For float
float(50)
50.0
float(5.663)
5.663
float("Python")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float("Python")
ValueError: could not convert string to float: 'Python'
float(7+5j)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(7+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
>>> 
>>> #string
>>> 
>>> str(4)
'4'
>>> str(8.5)
'8.5'
>>> str("Code")
'Code'
>>> str
<class 'str'>

>>> str(4+8j)
'(4+8j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> #Complex
>>> complex(50)
(50+0j)
>>> complex(4.50)
(4.5+0j)
>>> complex("Complex")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    complex("Complex")
ValueError: complex() arg is a malformed string
>>> complex(5+5j)
(5+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #bool
>>> bool(5)
True
>>> bool(5.2)
True
>>> bool("bool")
True
>>> bool(5+5j)
True
>>> bool(True)
True
>>> bool(False)
False
