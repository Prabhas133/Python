#Conditions
#There are three type of conditions only if,elif,else
'''using like
    1. if
    2.if - else
    3.if - elif
    4.if - elif - else
    5.multiple - elif
    6.multiple - if
    7.nested - if'''
#Only using if statments
#comparsion operator - <,>,<=,>=,!=,==

'''a = 10
b = 20
if a<b:
    print("True")'''#maintain indentation

'''a = 10
b = 20
if a>b:
    print("True")'''#output print nothing because a is less than b , but b is great than a then condition not satsified.

'''a = 12
b = 20
if a<=b:
    print("True")'''

'''a = 40
b = 20
if a>=b:
    print("True")'''

'''a = 40
b = 30
if a!=b:
    print("True")'''

'''a = 20
b = 20
if a == b:
    print("True")'''

'''a = "python"
if a == "python":
    print("True")'''

#using runtime input
'''a = int(input("Value a :"))
b = int(input("Value b :"))
if a<b:
    print("True")'''
#OR
'''a = int(input("Value a :"))
if a<50:
    print("True")'''


#using logical operators
#and
'''a = 10
b = 20
if a < b and b > a:
    print("True")'''

'''a = 10
b = 20
if a <= b and b >= a:
    print("True")'''

'''a = 50
b = 60
if a != b and a == b:
    print("True")'''#output print nothing because condiotion not satsified..

#or
'''a = 10
b = 20
if a < b or b > a:
    print("True")'''

'''a = 10
b = 20
if a <= b or b <= a:
    print("True")'''

'''a = 10
b = 20
if a != b or b == a:
    print("True")'''

#not
'''a = 3
b = 6
if not a < b and b > a:
    print("True")'''

'''a = 3
b = 6
if not a < b or b > a:
    print("True")'''

#using Identify operators
#is,is not
'''a = 4
if type(a) is int :
    print("It is a int")
a = 4
if type(a) is not int :
    print("It is a int")
    a = int(input())'''

'''a = 4.5
if type(a) is float :
    print("It is a float")
a = 4.5
if type(a) is not float :
    print("It is a float")
    a = flot(input())'''

'''a = "Prabhas"
if type(a) is str :
    print("It is a string")
a = "Prabhas"
if type(a) is not str :
    print("It is a string")
a = input()'''

'''a = 5+6j
if type(a) is complex :
    print("It is a complex")
a = 5+6j
if type(a) is not complex :
    print("It is a complex")
    a = complex(input())'''

'''a = True
if type(a) is bool :
    print("It is a boolean")
a = True
if type(a) is not bool :
    print("It is a boolean")
    a = bool(input())'''

#using membership operators , in , not in 
'''a = 50,3,5,6,7,8,10
if 50 in a:
    print("True")
a = 50,3,5,6,7,8,10
if 50 not in a:
    print("True")'''

'''a = int(input())
if 30 in a:
    print("True")'''#erorr

'''a = 2,3,4,5,6,7,8,9,10
b = int(input("Value b:"))
if b in a:
    print("True")'''

#only Using if - else statements
#comparsion operators
'''a = 10
b = 20
if a<b:
    print("True")
else:
    print("False")
a = 10
b = 20
if a>b:
    print("True")
else:
    print("False")'''

'''a = 10
b = 20
if a <= b :
    print("True")
else:
    print("False")
if a >= b :
    print("True")
else:
    print("False")'''

'''a = 50
b = 20
if a != b :
    print("True")
else:
    print("False")
a = 50
b = 20
if a == b :
    print("True")
else:
    print("False")'''

#logical operators

'''a = 10
b = 20
if a < b and b > a:
    print("True")
else:
    print("False")
    
a = 10
b = 20
if a > b and b < a:
    print("True")
else:
    print("False")'''

'''a = 10
b = 20
if a <= b and b >= a:
    print("True")
else:
    print("False")
a = 10
b = 20
if a >= b and b <= a:
    print("True")
else:
    print("False")'''

'''a = 50
b = 60
if a != b and a == b:
    print("True")
else:
    print("False")'''#output print nothing because condiotion not satsified..

#or
'''a = 10
b = 20
if a < b or b > a:
    print("True")
else:
    print("False")
a = 10
b = 20
if a > b or b < a:
    print("True")
else:
    print("False")'''

'''a = 10
b = 20
if a <= b or b <= a:
    print("True")
else:
    print("False")
    
a = 10
b = 20
if a >= b or b >= a:
    print("True")
else:
    print("False")'''

'''a = 10
b = 20
if a != b or b == a:
    print("True")
else:
    print("False")'''

#not
'''a = 3
b = 6
if not a < b and b > a:
    print("True")
else:
    print("False")'''

'''a = 3
b = 6
if not a < b or b < a:
    print("True")
else:
    print("False")'''

#using Identify operators
#is,is not,if - else
'''a = 4
if type(a) is int :
    print("It is a int")
else:
    print("It is not a int")

a = 4
if type(a) is not int :
    print("It is not a int")
else:
    print("It is a int")
    a = int(input())'''

'''a = 4.5
if type(a) is float :
    print("It is a float")
else:
    print("It is not a float")
    
a = 4.5
if type(a) is not float :
    print("It is not a float")
else:
    print("It is a float")
    a = flot(input())'''

'''a = "Prabhas"
if type(a) is str :
    print("It is a string")
else:
    print("It is not a string")

a = "Prabhas"
if type(a) is not str :
    print("It is not a string")
else:
    print("It is a string")
a = input()'''

'''a = 5+6j
if type(a) is complex :
    print("It is a complex")
else:
    print("It is not a complex")

a = 5+6j
if type(a) is not complex :
    print("It is not a complex")
else:
    print("It is a complex")
    a = complex(input())'''

'''a = True
if type(a) is bool :
    print("It is a boolean")
else:
    print("It is not a boolean")
a = True
if type(a) is not bool :
    print("It is a boolean")
else:
    print("It is a boolean")
    a = bool(input())'''

#using membership operators , in , not in ,if - else
'''a = 50,3,5,6,7,8,10
if 50 in a:
    print("True")
else:
    print("False")

a = 50,3,5,6,7,8,10
if 50 not in a:
    print("True")
else:
    print("False")'''

'''a = int(input())
if 30 in a:
    print("True")'''#erorr

'''a = 2,3,4,5,6,7,8,9,10
b = int(input("Value b:"))
if b in a:
    print("True")
else:
    print("False")

if b not in a:
    print("True")
else:
    print("False")'''

