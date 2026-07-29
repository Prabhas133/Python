#Variable length arguments
#Variable length arguements are automatically stores in tuples and we use star arguments
'''def c(*a):
    print(a)
    print(type(a))
c()
c(1,2,3,4,5,6)
b = [7,8,9,10]
c(b)
c(*b)
e = {11,12,13,14}
c(e)
c(*e)
d = {"name" : "prabhas","age" : 22}
c(d)
c(*d)'''
'''#output - ()
<class 'tuple'>
(1, 2, 3, 4, 5, 6)
<class 'tuple'>
([7, 8, 9, 10],)#without star printing output
<class 'tuple'>
(7, 8, 9, 10)
<class 'tuple'>
({11, 12, 13, 14},)#without star printing output
<class 'tuple'>
(11, 12, 13, 14)
<class 'tuple'>
({'name': 'prabhas', 'age': 22},)#without star printing output
<class 'tuple'>
('name', 'age')
<class 'tuple'>'''

#using for loop in fuction
'''def check(*a):
    c = 1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):#don't rise an error use this statement for adding int and str
            c = c + i
            print(c,end = " " )
check()
check(2,3,4,5,6)
check(1,2,2.4,4.5)
check(1,2,2.4,4.5,"python")#typeerror flt + str errot'''
'''output - ()
<class 'tuple'>
(2, 3, 4, 5, 6)
<class 'tuple'>
3 6 10 15 21 (1, 2, 2.4, 4.5)
<class 'tuple'>
2 4 6.4 10.9 (1, 2, 2.4, 4.5, 'python')
<class 'tuple'>
2 4 6.4 10.9 TypeError: unsupported operand type(s) for +: 'float' and 'str'''


#**(kwargs)
'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])#without using dict keyword printing the values
    for i in a.values():
        print(i)
    for i in a.items():
        print(i)
    for i in a:
        print(i,a[i])#without using dict keyword printing the items
check()
d = {"name" : ["sweety","cuty","hearty"],"Fav" : ["Fired Rice sweety" , "cutest of cuty" , "Your my hearty"]}
check(**d)'''
'''output -
{}
<class 'dict'>
{'name': ['sweety', 'cuty', 'hearty'], 'Fav': ['Fired Rice sweety', 'cutest of cuty', 'Your my hearty']}
<class 'dict'>
name
Fav
name
Fav
['sweety', 'cuty', 'hearty']
['Fired Rice sweety', 'cutest of cuty', 'Your my hearty']
['sweety', 'cuty', 'hearty']
['Fired Rice sweety', 'cutest of cuty', 'Your my hearty']
('name', ['sweety', 'cuty', 'hearty'])
('Fav', ['Fired Rice sweety', 'cutest of cuty', 'Your my hearty'])
name ['sweety', 'cuty', 'hearty']
Fav ['Fired Rice sweety', 'cutest of cuty', 'Your my hearty']'''


#both * and ** usage
'''def c(*a,**b):
    d=2
    print(a)
    print(b)
    #print(type(a))
    #print(type(b))
    for i in a:
        d = d + i
        print(d,end = " ")
    for i,j in b.items():
        print("key : ",i)
        print("Value : ",j)
c()
a = [1,2,3,4,5]
b = {"name" : "Prabhas","age" : 24}
c(*a)
c(**b)'''
'''output -()
{}
(1, 2, 3, 4, 5)
{}
3 5 8 12 17 ()
{'name': 'Prabhas', 'age': 24}
key :  name
Value :  Prabhas
key :  age
Value :  24'''


#Mini Project
'''while True:
    def ticket():
        ticket = 1000
        o = int(input(choose the option
                                            1.Male 
                                            2.Female :))
        if o == 1:
            male = int(input("Enter the Male age : "))
            if male >= 60 and male > 0:
                ticket = 1000*0.7
                print("U should pay : ",ticket)
            elif male < 60 and male > 0 :
                print("U should pay : ",ticket)
            else:
                if male < 0:
                    print("Try again,Renter the male age")
            
        elif o == 2:
            female = int(input("Enter the Female age :"))
            if female >= 60 and female > 0:
                ticket = 1000*0.5
                print("U should pay : ",ticket)
            elif female < 60 and female > 0:
                ticket = 1000*0.7
                print("U should pay : ",ticket)
            else:
                if female < 0:
                    print("Try again,Renter the female age")
        else:
            print("Invalid option")

    ticket()'''
#OR
#Using Recursion
'''def Railway():
        ticket = 1000
        o = int(input(choose the option
                                            1.Male 
                                            2.Female :))
        if o == 1:
            male = int(input("Enter the Male age : "))
            if male >= 60 and male > 0:
                ticket = 1000*0.7
                print("U should pay : ",ticket)
                print("Senoir Citizen")
            elif male < 60 and male > 0 :
                print("U should pay : ",ticket)
                print("Normal Citizen")
            else:
                if male < 0:
                    print("Try again,Renter the male age")
            
        elif o == 2:
            female = int(input("Enter the Female age :"))
            if female >= 60 and female > 0:
                ticket = 1000*0.5
                print("U should pay : ",ticket)
                print("Senoir Citizen")
            elif female < 60 and female > 0:
                ticket = 1000*0.7
                print("U should pay : ",ticket)
                print("Normal Citizen")
            else:
                if female < 0:
                    print("Try again,Renter the female age")
        else:
            print("Invalid option")
        Railway()
Railway()'''














