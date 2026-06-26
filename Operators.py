Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#OPERATORS
a=2
b=5
print(a+b)
7
print(a-b)
-3
print(a*b)
10
print(a//b)
0
print(a/b)
0.4
print(a**b)
32
print(a%b)
2


#Assig
#ASSIGNMENT Operator
a = 3
b = 10
print(a+=b)
SyntaxError: invalid syntax
a = 5
a
5
a+=b
a
15
a-=b
a
5
a+=4
a
9
a*=b
a
90
a//=9
a
10
a/=2
a
5.0
a**=5
a
3125.0
a%=5
a
0.0


#In assignment opeartor update value will store in the variable a .


#Comparsion operator

a=4
b=9
a<b
True
a>b
False
a<=b
True
>>> a>=b
False
>>> a!=b
True
>>> a==b
False
>>> 
>>> 
>>> #Logical operator
>>> 
>>> 
>>> a=10
>>> b=15
>>> b>a and a<b
True
>>> a<=b and b>=a
True
>>> a!=b and b!=a
True
>>> a<b or b>a
True
>>> a!=b or b==a
True
>>> not True
False
>>> not False
True
>>> #Before condition we mention the not operator
>>> #And means comparsing both statements are true or not , OR means comparsing both statement and if single statement is correct it will be printiing true .
>>> 
>>> 
>>> #Condition operator
>>> 
>>> a=1,2,3,4,5,6,7
>>> 7 in a
True
>>> 7 not in a
False
>>> 20 in a
False
>>> 
>>> #If value is in variable we are calling the value it is present it will printing true and not there means false.
>>> 
>>> 7 in float
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    7 in float
TypeError: argument of type 'type' is not a container or iterable
