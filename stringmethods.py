Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#len()
a = "python"
len(a)
6
b = "python course"
len(b)
13
c = ""
len(c)
0
d = " "
len(d)
1
#Count
a = "twinkle twinkle litttle star"
a.count("twinkle")
2
a.count("t")
6
a.count(" ")
3
b = 24567454
b.count(4)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.count(4)
AttributeError: 'int' object has no attribute 'count'
#find a string
a = "code"
a.find("d")
2
a.find("o")
1
b = "Hello"
b.find("l")
2
#it give the position of index for output.

#Escape sequences
#\n - new line
#\t - tab spaces - 4 to 8 b/w space for tab space
a = "name\nmobile\tmailid\ncollege"
print(a)
name
mobile	mailid
college
b = "name : Prabhas Naidu\nMobile-no : 123456789\tMailid : prabhas@gamil.com\nCollege : IIITDMK"
print(b)
name : Prabhas Naidu
Mobile-no : 123456789	Mailid : prabhas@gamil.com
College : IIITDMK
#Replace
a = "wait until you succed"
a.replace("wait","work")
'work until you succed'
a.replace(' ',',')
'wait,until,you,succed'
b = "sumanth is a bad boy"
b.replace('bad','good')
'sumanth is a good boy'
b = "wait wait until u succeed"
b.replace('wait','work')
'work work until u succeed'
b.replace("wait","work",1)
'work wait until u succeed'
b.replace("wait","work",2)
'work work until u succeed'


#lower
b.lower()
'wait wait until u succeed'
b = "HI"
b.lower()
'hi'
#uppper
c = "python"
c.upper()
'PYTHON'
#just p should be than
c[0].upper()
'P'
# we have buit-in for it is captialize
c.capitalize()
'Python'
#Above capitalize

#title
a = "python course"
a.title()
'Python Course'
c = "I am in class"
c.title()
'I Am In Class'


##
a= "java"
a.islower()
True
a.isupper()
False
a.isalpha()
True
d = 1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
#not possible in the string methods

d = "1234"
d.isdigit() #now it possible
True
d.isalnum()
True
#because number present in the given string

e  = "pooja12234"
e.isalnum()
True

a = "hello python"
a.startswith("h")
True
a.endswith("n")
True
#conditions of upper and lower


#Strip
#lstrip(),rstrip()
a = "       prabhas        "
a.strip()
'prabhas'
a = "          prabhas"
a.lstrip()
'prabhas'
KeyboardInterrupt
a = "       prabhas        "
a.lstrip()
'prabhas        '
a.rstrip()
'       prabhas'
a.strip()
'prabhas'
a = "  python course   "
a.strip()
'python course'
a.lstrip()
'python course   '
a.rstrip
<built-in method rstrip of str object at 0x000002A0091AA530>
a.rstrip()
'  python course'


#split
a = "python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b = "I am in vijayawada"
b.split()
['I', 'am', 'in', 'vijayawada']
c = "codegnan"
c.split()
['codegnan']



#join
a = "vijayawada hyd vzg"
"".join(a)
'vijayawada hyd vzg'
a = "vijayawada","hyd","vzg"
"".join(a)
'vijayawadahydvzg'
" ".join(a)
'vijayawada hyd vzg'
"K".join(a)
'vijayawadaKhydKvzg'


#concatenation
a = "Hello"
b = "world"
print(a + " " + b)
Hello world
fname = "Prabhas"
lname = "naidu"
print((fname + " " + lname).title())
Prabhas Naidu


#formatting
a = 5
b = 6
print(a+b)
11
print("sum is",a+b)
sum is 11

#format method
a = "motu"
b = "patlu"
print("hello",a+b)
hello motupatlu
print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> #.foramt method
>>> 
>>> #f'string
>>> a = "sita"
>>> b = "ram"
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> print(f"hello {a} {b}")
hello sita ram
