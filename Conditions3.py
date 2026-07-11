#multiple - if conditions
'''a = 20
b = 40
if a < b :
    print("lesser")
if b > a:
    print("greater")
if a != b:
    print("Not equal")'''

'''a = 20
b = 40
if a == b :
    print("lesser")
if b > a:
    print("greater")
if a != b:
    print("Not equal")'''#because the if not break the condition and check until loop condition continous .
    

'''a = 20
b = 40
if a == b :
    print("lesser")
if b > a:
    print("greater")
if a >= b:
    print("Not equal")
else:
    print("True")'''


#Nested if
'''a = 4
b = 5
if a < b:
    print("lesser")
    if b > a:
        print("greater")'''

'''a = 5
b = 6
if a > b:
    print("lesser")
    if b > a:
        print("greater")'''#print nothing , because of first condition should satsified after that it allows into remaining conditions.

'''a = 7
b = 11
if a != b:
    print("true")
    if b == a:
        print("greater")
    else:
        print("False")'''

'''a = 7
b = 11
if a == b:
    print("true")
    if b > a:
        print("greater")
else:
    print("False")'''


'''a = 7
b = 11
if a != b:
    print("true")
    if b == a:
        print("greater")
    else:
        print("False")
else:
    print("Not True")''';#Print true and false , because of 1st conditions satsified and 2 not satsified prints else condition false


'''a = 7
b = 11
if a != b:
    print("true")
    if b == a:
        print("greater")
    elif a < b:
        print("less")
    else:
        print("false")'''#print true and less


'''a = int(input())
b = int(input())
if a != b:
    print("true")
    if b == a:
        print("Equal")
    elif a > b:
        print("less")
    else:
        print("false")
else:
    print("Program ends")'''
        
