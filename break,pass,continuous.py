#Different b/w break ,pass, continuous
#break is use to terminate the entire loop.
#continuous statement is use to skip the current iteration and the rest of the code to be continue.
#A pass is null statement it does nothing but syntaxicly we need.
#break
'''a = 10
while a > 1:
    print(a,end =" ")
    a = a - 1
    if a == 6:
        break'''#output - 10 9 8 7 

'''a = 10
while a > 1:
    a = a - 1
    if a == 6:
        break
    print(a,end =" ")'''# output - 9 8 7

'''a = "python"
if a == "h":
    break
print(a)'''#error


'''a = "python"
for i in a:
    if i == "h":
        break
    print(i,end = " ")'''# output - p y t

#continuous
'''a = 10
while a > 1:
    print(a,end = " ")
    a = a - 1
    if a == 5:
        continue'''#output - 10 9 8 7 6 5 4 3 2 ,it will be print continue iteration and 10 prints , print statement write after the continue keyword

'''a = 10
while a > 1:
    a = a - 1
    if a == 5:
        continue
    print(a,end = " " )'''#output - 9 8 7 6 4 3 2 1  skip the 5 and the iterate remaining values 

'''for i in range(10):
    if i == 5:
        continue
    print(i,end = " ")'''#output - 0 1 2 3 4 6 7 8 9 
    
'''a = "python"
for i in a:
    if i == "y":
        continue
    print(i,end = " ")'''#output - p t h o n 



#pass
'''a = 10
while a > 1:
    print(a,end = " " )
    a = a - 1
    if a == 5:
        pass'''#output - 10 9 8 7 6 5 4 3 2 it is use for syntax purposes , but it is like place holder

'''for i in range(10):
    if i == 5:
        pass
    print(i,end = " ")'''

'''a = "python"
for i in a:
    if i == "y":
        pass
    print(i,end = " ") '''#output - p y t h o n 




