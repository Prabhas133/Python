Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Indexing
>>> #accessing the use squarebackets[]
>>> a="Vijayawada"
>>> a[0]
'V'
>>> a[3]
'a'
>>> a[0]+a[1]+a[2]+a[3]+a[4]
'Vijay'
>>> a[-1]
'a'
>>> a[-1]+a[-2]+a[-3]
'ada'
>>> b = "I am in class"
>>> b[0]
'I'
>>> a[1]
'i'
>>> a[8]+a[9]+a[10]+a[11]+a[12]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[8]+a[9]+a[10]+a[11]+a[12]
IndexError: string index out of range
>>> [8]+b[9]+b[10]+b[11]+b[12]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    [8]+b[9]+b[10]+b[11]+b[12]
TypeError: can only concatenate list (not "str") to list
>>> b[8]+b[9]+b[10]+b[11]+b[12]
'class'
>>> b[2]+b[3]
'am'
>>> b[0]
'I'
>>> b[5]+b[6]
'in'
>>> b[1]+b[4]+b[7]
'   '
>>> b = "I am Learning Pyhton course"
>>> b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'Pyhton'
>>> b = "I am Learning Python course"
>>> b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'Python'
>>> b[5]+b[6]+b[7]+b[8]+b[9]
'Learn'
>>> b[21]+b[22]+b[23]+b[24]+b[25]+b[26]+b[27]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b[21]+b[22]+b[23]+b[24]+b[25]+b[26]+b[27]
IndexError: string index out of range
b[21]+b[22]+b[23]+b[24]+b[25]+b[26]
'course'
a="Time is very percious"
a[0]+a[1]+a[2]+a[3]
'Time'
a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'percious'
a[8]+a[9]+a[10]+a[11]
'very'
a[13:27]
'percious'
a[8:11]#slicing
'ver'
a[8:12]
'very'
a="Simple is better than complex"#Negative indexing
a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'imple'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'Simple'
a[-12]+a[-11]+a[-10]+a[-9]
'than'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a="I love python"
a[-11]+a[-10]+a[-9]+a[-8]
'love'
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[4:5:1]
'v'
a[6:8:2]
' '
a[6:8:4]
' '
a[7:9:1]
'py'
a[7:10:1]
'pyt'
a[7:10:2]
'pt'
a[7:11:3]
'ph'
a[7:12:3]
'ph'
