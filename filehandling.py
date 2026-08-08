#File handling
#write()
'''
file = open("prabhas.txt","w")
file.write("Pyhton course")
file.close()'''

'''
file = open("prabhas.txt","w")
file.write("Python full stack")
file.close()
'''

#append()
'''
file = open("prabhas.txt","a")
file.write("\n Data science")
file.close()'''


#Using run time input()
'''
file = open("prabhas.txt","w")
file.write(input("Enter the data : "))
file.close()'''

'''
file = open("prabhas.txt","w")
r = input("Enter the data : ")
file.write(r)
file.close()'''

#read
#a = open("prabhas.txt")
#print(a.read()) it will display entire content 
#print(a.readline()) it will display first line 
#print(a.readlines()) it will display in list with \n
#print(a.read(8)) it will display no.of characters


#writelines() it makes every object side by side
'''
a = open("name.txt","w")
b = ["Krishna","Sumanth","Prabhas"]
a.writelines("\n".join(b))
a.close()

a = open("name.txt")
print(a)
'''
a = open("C:\\Users\\Admin\\Documents\\Python\\OOPS\\i.py")#reading file 
print(a.read())
