Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a = (4,5.6,"code",5+9j,True,False)
>>> print(a)
(4, 5.6, 'code', (5+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> #methods uses
>>> #count
>>> a.count(5+9j)
1
>>> #index
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.index(2)
ValueError: tuple.index(x): x not in tuple
>>> a.index(True)
4
>>> len(a)
6
