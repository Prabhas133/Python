#exception handling
#try => Instruction from which we are expecting the exceptions.
#except =>exceptions are raised in try block it will be handle by this block.
#else =>optional (no exceptions).
#finally =>always it will display .
'''
while True:
    a = int(input())
    b = int(input())
    try:
        c = a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("No exceptions")
    finally:
        print("program ends...")'''
#output -
'''
input - 6 6
1
No exceptions
program ends...
input - 6 0
exception is raised
program ends...
'''




'''
while True:
    try:
        a = int(input())
        b = int(input())
        c = a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("No exceptions")
    finally:
        print("program ends...")'''
#output -
'''
3.2
exception is raised
program ends...'''

#regex(regular expression)
#reagular are powerful tools (module) embedd which mainly use to find a pattern with in a given string all statement and file, and we mainly use it texting manipluation .
'''
a = "Codegnan is in vijayawada"
print(a)'''
'''
a = "Codegnan\nis\tin\nvijayawada"
print(a)'''

#rstring #roya string means it will not modifiy any thing 
'''a = r"Codegnan\nis\tin\nvijayawada"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''
\w -> it matches alphanumeric
\W -> it matches non-alpha numeric
\d -> it matches any digit
\D -> it matches non - digit
\s -> it represents white spaces
\S -> it represents non white spaces'''
#compile()
import re
#a = "mat cat cap maths money cash code cup dog donkey mug"
'''b = re.compile(r"m\w\w\w\w")
print(b)'''#output - re.compile('m\\w'), nothing action done

#search()
'''c = b.search(a)
print(c)'''
#output -
'''
re.compile('m\\w\\w\\w\\w')
<re.Match object; span=(12, 17), match='maths'>'''

'''b = re.search(r"m\w+",a)
print(b)'''#output - <re.Match object; span=(0, 3), match='mat'>

#findall()
'''
c = re.findall(r"c\w+",a)#without using the r" also not problem .
print(c)
c = re.findall(r"m\w+",a)
print(*c)#unpack elements
c = re.findall(r"d\w+",a)
print(*c)'''
#output -
'''
['cat', 'cap', 'cash', 'code', 'cup']
mat maths money mug
de dog donkey'''

#split()
'''
f = re.split(r"m",a)
print(f)
e = re.split(r"\S",a)
print(e)
g = re.split(r"\s",a)
print(g)'''
#output -
'''
['', 'at cat cap ', 'aths ', 'oney cash code cup dog donkey ', 'ug']
['', '', '', ' ', '', '', ' ', '', '', ' ', '', '', '', '', ' ', '', '', '', '',
' ', '', '', '', ' ', '', '', '', ' ', '', '', ' ', '', '', ' ', '', '', '', '', '', ' ', '', '', '']
['mat', 'cat', 'cap', 'maths', 'money', 'cash', 'code', 'cup', 'dog', 'donkey', 'mug']
'''

#sub()
'''
f = re.sub("m","a",a)#replace the 'm' to 'a' 
print(f)'''
#output -
'''
aat cat cap aaths aoney cash code cup dog donkey aug'''


#finding digit
'''
b ="year 2026 month 7 date 29"
c = re.findall(r"\d+",b)
print(c)
d = re.findall(r"\D+",b)
print(d)'''
#output -
'''
['2026', '7', '29']
['year ', ' month ', ' date ']'''

a = "code dog donkey"
h = re.findall(r"d\w+",a)
print(h)
#another method 
f = re.findall(r"\bdo\w*",a)#\b means boundary and we can use \w* and \w+
print(f)
#output -
'''
['de', 'dog', 'donkey']
['dog', 'donkey']'''#for removing the de using the boundary method














