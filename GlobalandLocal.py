#Global and local variables
#Variables inside and outside the function is called global and local variables.
#A variable is a defined above the function is acessible to the entire global space is called global variable.
#A variable is inside the function is called local variable 
#4 steps
#First case of global variables
'''a = 4
def c():
    print("Inside is",a)
c()
print("Outside is",a)
'''

#Second case of global variables
'''a = 2
def c():
    a = 5
    a = a**2
    print("Inside is ",a)
c()
print("Outside is ",a)'''


#Third case of global variables and local variables
'''a = 6
def c():
    a = 8
    print("Inside is ",a)
    a = 10
    print("Update value is ",a+5)
    b = 13#local variable
    b = b + a
    print("update Value of b is ",b)
c()
print("Outside is ",a)
#print("Value of b is", b)'''#This print statements is throughs error because b is local variable not a global variables.


#Global keyword
#When user wants access the global variable inside th function directly and carry forward the updated value even outside the function then we need to use global keyword.
'''a = 6
def c():
    global a,b
    print("Inside a is ",a)#it prints a = 6 because it takes global variable from outside 6
    a = 10
    print("Update value a is ",a+5)
    a = 15#update value of a
    b = 13#local variable
    b = b + a
    print("update value of b is ",b)
c()
print("Outside a is ",a)#Here print a = 15 because we are declaring the global keyword inside then it throughs local variable like global variable for output
print("Value of b is",  b)#same as the a, scope of the variables means global and local. '''


#Attendance Tacker
'''def attendance():
    n = int(input("No.of students : "))
    p = 0
    a = 0
    for i in range(1,n+1):
        b = input(f"Students {i} present and absent : ")
        if b == "yes":
            p += 1
        elif b == "no":
            a += 1
    print("--------Attendance Report---------")
    print("Total number of students : ",n)
    print("Total Present students :",p)
    print("Total Absent students : ",a)
    print("\n")
    attendance()
attendance()'''

#patterns
n = int(input())
for i in range(1,n):
    for j in range(1,n)
        print("*",end = " ")
        
