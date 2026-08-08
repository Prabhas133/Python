#1.
#a = int(input())
#b = int(input())
'''print("\n")
for i in range(1,a):
    for j in range(1,b):
        print("*",end = " ")
    print()
print("\n")'''
'''for i in range(0,a):
    for j in range(0,b):
        print(i,end = " ")
    print()
print("\n")   ''' 
'''for i in range(1,a):
    for j in range(1,b):
        print(i,end = " ")
    print()
print("\n")'''
'''for i in range(a,0,-1):
    for j in range(1,b):
        print(i,end = " ")
    print()
print("\n")'''
'''for i in range(0,a):
    for j in range(b):
        print(j,end = " ")
    print()
print("\n")'''
'''for i in range(0,a):
    for j in range(b,-1,-1):
        print(j,end = " ")
    print()'''

'''for i in range(1,a):
    for j in range(1,b):
        print(j*2,end = " ")
    print()'''

'''for i in range(a):
    print("*" * a)'''#time complexity will be less
'''
for i in range(2):
    for j in range(3):
        print(j-i+1,end = " ")'''
#pyramid
'''n = int(input())
for i in range(n):#
    print((" "*(n-i-1))+"* "*(i+1))'''#First printing after the printing star
#O(n**2)
'''n = int(input())
for i in range(n):#
    print(("_"*(n-i-1)),end = " ")
    print("* "*(i+1))'''
'''n = int(input())
for i in range(n,0,-1):
    print("*"*(i))'''#right angle triangle printing with stars

'''
#All are one type model of output but different method 
n = int(input())
for i in range(n+1,0,-1):
    for j in range(i-1):
        print(i-j-1,end = " ")
    print()'''

'''n = int(input())
for i in range(n,0,-1):
    for j in range(2,i+2):#but it is reversely prints output 
        print("*",end = " ")
    print()'''
    
'''n = int(input())
for i in range(2,n+2):
    for j in range(2,i+1):
        print(j,end = " ")#Same as first but different logic 
    print()'''
#n = int(input())
'''for i in range(1,n):
    print(i*(((10**i)-1)//9))'''
'''
n = int(input())
for i in range(n):
    print(" "*(n-i-1),end = " ")
    print("* "*(i+1))

 or
n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "* "* (i + 1))'''#pyramid
'''
n = int(input())
for i in range(n):
    for j in range(n,0,-1):
        print(j,end = " ")
    print()'''
'''
n = int(input())
for i in range(n+1):
    for j in range(i,n+1):
        print(j,end =" ")
    print()'''
#output -
'''0 1 2 3 
1 2 3 
2 3 
3 '''

'''n = int(input())
for i in range(n):
    for j in range(n-1,n-i-2,-1):
        print(j,end =" ")
    print()'''
#output -
'''
3 
3 2 
3 2 1 
3 2 1 0 '''

'''n = 4
for i in range(1,n+1):
    print("__" * (n - i) + "* "* i)'''# __ Two sapces 
#output -
'''
      * 
    * * 
  * * * 
* * * *'''
'''n = int(input())
for i in range(n):#
    print((" "*(n-i-1)),end = " ")
    print("* "*(i+1))'''
n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "5 "* (i + 1))
'''n = int(input())
for i in range(n):
    print("* " * n)'''


