#range()
#The range written a sequences ,starting from 0 by default and increments by 1 by 1 and stops before a specified number.
#start - stop - step
#start
'''for i in range(20):
    print(i,end = " ")'''#output - 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
#stop
'''for i in range(13,35):
    print(i,end = " ")'''#output - 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 
#steps
'''for i in range(0,30,3):
    print(i,end = ",")
print("\n")
for i in range(5,50,5):
    print(i,end = ",")
print("\n")
for i in range(2,20,2):
    print(i,end = ",")'''

#Grades task
'''while True:
    marks = int(input("Enter the marks : "))
    if marks in range(90,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif  marks in range(71,81):
        print("Grade C")
    elif  marks in range(50,71):
        print("Grade D")
    else:
        print("Fail")'''

'''while True:
    marks = int(input("Enter the marks : "))
    if 91 <= marks <= 100:
        print("Grade A")
    elif 81 <= marks <= 90:
        print("Grade B")
    elif 71 <= marks <= 80:
        print("Grade C")
    elif 50 <= marks <= 70:
        print("Grade D")
    else:
        print("Fail")'''
