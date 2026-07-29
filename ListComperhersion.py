#List Comperhresion
#every list comprehersion can be rewirtten as a for loop but every for loop can't be rewitten in list comprehersion.
#Example task
'''n = ["codegnan","python","course"]
l = []
for i in n:
    l.append(i.upper())
print(l)'''

#Example writting in list comprehersion
#a = [expr for var in collection / range] syntax
'''a = ["codegnan","python","course"]
x = [i.upper() for i in a]
print(x)'''

#Tasks
'''a = ["vja","hyd","vzg"]
x = [i.title() for i in a] or [i.capitalize() for i in a] 
print(x)'''#output - ['Vja', 'Hyd', 'Vzg']

'''b = [1,2,3,4,5,6,8,12,13]
y = [i*i for i in b]
print(y)'''#output - [1, 4, 9, 16, 25, 36, 64, 144, 169]
#other methods [pow(i,2)for i in a] or [i**2 for i in a]

'''a = [i for i in range(16)]
print(a)'''#output -  [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

'''print("Even numbers")
x = [i for i in range(16) if i%2 == 0]
print(x)
print("Odd numbers")
x = [i for i in range(16) if i%2 != 0]
print(x)'''

'''x = [i*i for i in range(21) if i%2 == 0]
print(x)'''#output - [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

'''a = ["apples","banana","grapes","mango","kiwi","dragon","berry"]
x = [i for i in a if "a" in i]
print(x)'''#output - ['apples', 'banana', 'grapes', 'mango', 'dragon'] only prints a letter words
'''a = ["apples","banana","grapes","mango","kiwi","dragon","berry"]
x = [i for i in a if "a" not in i]
print(x)''' #output - ['kiwi', 'berry'] only prints not a letter words

'''x = [i*i if i%2 == 0 else i*5 for i in range(31)] #[0, 5, 4, 15, 16, 25, 36, 35, 64, 45, 100, 55, 144, 65, 196, 75, 256, 85, 324, 95, 400, 105, 484, 115, 576, 125, 676, 135, 784, 145, 900]
print(x)'''

a = [1,2,3,4,5]
b = [5,4,3,2,1]
x = [i + j for i,j in zip(a,b) ]
print(x)
#or
x = [a[i] + b[i] for i in range(len(a))]
print(x)
#or
x = [a[i] + b[i] for i in range(5)]
print(x)

