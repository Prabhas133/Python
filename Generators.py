'''a=[i for i in range(16)]
print(a)
print(type)'''

#(expr for var in collection/range)
'''a=(i for i in range(16))
print(a)
print(*a)#unpacking the elements , for printing the elements .
print(type(a))'''

'''b=list(a)
print(b)'''

#print (tuple(a))
'''print(set(a))'''

#GENERATOR

#A GENERATOR IS ALSO A FUNCTION WHICH CAN BE USED AS AN ITRERATOR(LOOP) BY PRODUCING GROUP OF VALUES,WHERE WE CAN USE YIELD KEYWORD.

#YIELD VS RETURN

#RETURN WILL TERMINATE THE FUNCTION WHERE AS YIELD CAN PASS THE FUNCTION AND GO ON WITH EVERY SUCCESSIVE ITERATION.

'''a,b = [int(i) for i in input("Enter the values a , b : ").split(",")]
def check(a,b):
    while a<b:
        yield a
        a = a+1
        yield a
print(*check(a,b))'''#output - 2 3 3 4 4 5 5 6 6 7 7 8 8 9


'''a,b = [int(i) for i in input("Enter the values a , b : ").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a = a+1
        yield a
print(*check(a,b))'''#output - 3 4 5 6 7 8 9

'''a,b = [int(i) for i in input("Enter the values a , b : ").split(",")]
def check(a,b):
    while a<b:
        a = a+1
        return a
print(check(a,b))'''#output - 3

'''a,b = [int(i) for i in input("Enter the values a , b : ").split(",")]
def check(a,b):
    while a<b:
        a = a+1
    return a
print(check(a,b))'''#output - 9

#yield v/s return
def mygen():
    return "vja","hyd","vzg"
print(*mygen())

def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())

#next()
d = mygen()
print(next(d))#it will prints new line built-i function.
print(next(d))
print(next(d))
#print(next(d))#throug error StopIteration



