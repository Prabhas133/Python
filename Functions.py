#Functions
#functions is a block of organized,reuseable code and that is use to preform a single or multiple tasks.
#Python gives a builts-in functions like print,u can make your own function also these are called user defined functions.
#Python blocks begin with the keyword def followed by function name and def().
'''a = 10
b = 20
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)
a = 100
b = 200
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)'''#It is so lenghtly code 


'''def calculate(a,b):#It is a small and simply access the code , no.of tasks at time.
    print("The sum is",a+b)
    print("The diff is",a-b)
    print("The product is",a*b)
calculate(10,20)
calculate(100,200)'''

'''def calculate(a,b):#It is a small and simply access the code , no.of tasks at time.
    print("The integr division is",a//b)
    print("The modules is",a%b)
    print("The power is",a**b)
calculate(10,4)
calculate(2,5)'''

'''def add():
    a = int(input("Enter the value a : "))
    b = int(input("Enter the value b : "))
    print(a+b)
add()'''#only function call and using runtime inputs

'''def add():
  a = int(input("Enter the value a : "))
    b = int(input("Enter the value b : "))
    print(a+b)
    add()
add()'''#Recursion function call without using the while true.Recursion function call work likes while true without mentioning while true loop.

'''def fullname():
    fname = input("First name : ")
    lname = input("Last name : ")
    print((fname + " " + lname).title())
fullname()'''

'''def fullname():
    fname = input("First name : ")
    lname = input("Last name : ")
    result = ((fname + " " + lname).title())
    print(result)
fullname()'''

#Different b/w print and return
#print just show the human user input in a console.
#return will terminate function and gives back a value from function.
#print vs return
'''def add(a,b):
    c = a+b
    d = a-b
    e = a*b
    print(c)
    print(d)
    print(e)
add(5,6)'''

'''def add(a,b):
    c = a+b
    d = a-b
    e = a*b
    #return c# output - 11
    #return d# output - -1
    #return e# output - 30 , It prints only one return at time , because after that terminate it not prints remaining return values.U want to print then comment first return and print second return 
    return (c,d,e)
print(add(5,6))'''


#splitbill() task
'''def splitbill():
    bill = float(input("Enter the bill amount : "))
    persons = int(input("Enter no.of person : "))
    s = bill//persons
    return s
print(splitbill())'''

'''def splitbill():
    bill = float(input("Enter the bill amount : "))
    persons = int(input("Enter no.of person : "))
    s = bill//persons
    print(f"Each preson should pay : {s}")#using the f'sting format
    splitbill()
splitbill()'''


'''def splitbill():
    bill = float(input("Enter the bill amount : "))
    persons = int(input("Enter no.of person : "))
    s = bill//persons
    print("Each preson should pay : {}".format(s))#using the .format method
    splitbill()
splitbill()'''

#add,sub,mul
'''def asm():
    a = int(input("Enter the value a : "))
    b = int(input("Enter the value b : "))
    o = int(input(choose the option
                                            1.add 
                                            2.sub 
                                            3.mul : ))
    if o == 1:
        print("addition : ",a+b)
    elif o == 2:
        print("diiference : ",a-b)
    elif o == 3:
        print("product : ",a*b)
    else:
        print("Invalid options,Try again")
    asm()
asm()'''


#multiple def keyword using
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a = int(input("Enter the value a : "))
    b = int(input("Enter the value b : "))
    o = int(input(choose the option
                                            1.add 
                                            2.sub 
                                            3.mul :))
    if o == 1:
        add()
    elif o == 2:
        sub()
    elif o == 3:
        mul()
    else:
        print("Invalid options,Try again")'''



#keyword and positional arguments
#1.
'''def details(id,name,mailid):
    id  = 10
    name = "Prabhas"
    mailid  = "prabhas@gmail.com"
    print(id,name,mailid)
details(id="id",name = "name",mailid = "mailid")'''#id = "id" , keyword and postional arguments examples problem

#2.   
'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name = "name",mailid = "mailid")
details(id  = 10,name = "Prabhas",mailid  = "prabhas@gmail.com")'''
#output = id name mailid
#10 Prabhas prabhas@gmail.com

#3.
'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name = "name",mailid = "mailid")
details(id  = 10,name = "Prabhas",mailid  = "prabhas@gmail.com")
details(id  = 20,name = "Sumanth",mailid  = "sum@gmail.com")
details(30,"Jessy","jee@gmail.com")
details("s@gmail.com",40,"subbu")#it no guessing exactly what is what data is going into other one 
details(mailid  = "sai@gmail.com",id  = 50,name = "Sai")#here we are mentioning the key for key values , but not giving correct position.'''
#output -
#id name mailid
#10 Prabhas prabhas@gmail.com
#20 Sumanth sum@gmail.com
#30 Jessy jee@gmail.com
#s@gmail.com 40 subbu
#50 Sai sai@gmail.com


#default arguments types 
'''def grocery(items,price):
    print("item is %s"%items)
    print("price is %.2f"%price)
grocery("sugar",100)'''


'''def grocery(items = "rice",price = 150):
    print("item is %s"%items)
    print("price is %.2f"%price)
grocery()'''


'''def grocery(items,price = 160):
    print("item is %s"%items)
    print("price is %.2f"%price)
grocery("Dhal")'''

'''def grocery(items="Wheat",price):#non default argument not follows 
    print("item is %s"%items)
    print("price is %.2f"%price)
grocery(200)'''

#Task
'''def sumanthbarkery(cakename="choclate",price=500,quty="1kg"):
    print("Cake is %s"%cakename)
    print("price is %.2f"%price)
    print("quality is %s"%quty)
sumanthbarkery()
print("\n")    
def sumanthbarkery(cakename,price,quty):
    print("Cake is %s"%cakename)
    print("price is %.2f"%price)
    print("quality is %s"%quty)
sumanthbarkery("blackforest",1000,"2kg")
print("\n")
def sumanthbarkery(cakename,price=2000,quty="3kg"):
    print("Cake is %s"%cakename)
    print("price is %.2f"%price)
    print("quality is %s"%quty)
sumanthbarkery("Redvlvant")
print("\n")
def sumanthbarkery(cakename,price,quty="1.5kg"):
    print("Cake is %s"%cakename)
    print("price is %.2f"%price)
    print("quality is %s"%quty)
sumanthbarkery("choclate",1500,)'''

#* arguments("*" is star used to unpack the elements.)
'''a = [2,3,4,5,6,7,8]
print(a)
print(*a)'''#unpacking the list #output - 2 3 4 5 6 7 8
#output - [2, 3, 4, 5, 6, 7, 8]

'''a = (2,3,4,5,6,7,8)
print(a)
print(*a)'''#output - 2 3 4 5 6 7 8
#output - (2, 3, 4, 5, 6, 7, 8)

'''a = {2,3,4,5,6,7,8}
print(a)#output -{2, 3, 4, 5, 6, 7, 8}
print(*a)'''#output - 2 3 4 5 6 7 8

#dictonary can't use def functions then it works.
'''c = "python"
print(*c)'''#output - p y t h o n

'''a,b,c = 1,2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#error

'''a,b,c = 1,2,3
print(a)
print(b)
print(c)'''

'''*a,b,c = 1,2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,*b,c = 1,2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''*a,b,*c = 1,2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(*c)'''#rise an error because of multiple star not possible


'''a,b,c = "Codegnan"
print(a)
print(b)
print(c)'''#error

'''*a,b,c = "Codegnan"
print(*a)
print(b)
print(c)'''

'''a,*b,c = "Codegnan"
print(a)
print(*b)
print(c)'''

'''a,b,*c = "Codegnan"
print(a)
print(b)
print(*c)'''


        





