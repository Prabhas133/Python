Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Slicing
a = "Codegnan"
a[0:3]
'Cod'
a[0:4]
'Code'
a[4:8]
'gnan'
a[:4]
'Code'
a[:8]
'Codegnan'
a[4:]
'gnan'
a = "Work until you succeed"
a[6:11]
'ntil '
a[5:11]
'until '
a[11:15]
'you '
a[11:14]
'you'
a[:5]
'Work '
a[:4]
'Work'
a[15:]
'succeed'
b = "Codegnan it solutions"
b[9:11]
'it'
b[0:8]
'Codegnan'
b[13:]
'olutions'
b[12:]
'solutions'
#negative
a = "Vijayawada is royal city"
a[-6:-10]
''
a[-10:-6]
'roya'
a[-10:-7]
'roy'
a[-10:-5]
'royal'
a[-4:]
'city'
a[-25:-15]
'Vijayawad'
a[-25:-16]
'Vijayawa'
a[-25:-14]
'Vijayawada'
b= "vizag is city of destiny"
b[-7:]
'destiny'
b[-14:-11]
'ity'
b[-15:-11]
'city'
b[-24:-19]
'vizag'
#Striding
a = "Python"
a[0:7:2]
'Pto'
a[0:7:1]
'Python'
a[0:4:1]
'Pyth'
a[0:4:2]
'Pt'
c = "data science"
c[::]
'data science'
c[::1]
'data science'
c[::2]
'dt cec'
c[::5]
'dsc'
c[5:8:0]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c[5:8:0]
ValueError: slice step cannot be zero
c[5:8:]
'sci'
c[5:8:1]
'sci'
c[5:11:1]
'scienc'
c[5:12:1]
'science'
c[5:12:2]
'sine'
c[5:12:3]
'see'
c[5:12:4]
'sn'
c[5:12:5]
'sc'
c[5:12:6]
'se'
c[5:12:7]
's'
#Not increment because required letter not in word print only s letter.
a = "cloud computing"
a[::5]
'c u'
>>> a[::4]
'cdmi'
>>> a[::8]
'cm'
>>> a[2:]
'oud computing'
>>> a[:9]
'cloud com'
>>> a[3:11]
'ud compu'
>>> a[::2]
'codcmuig'
>>> a[::6]
'cci'
>>> a="Machine Learning"
>>> a[1:9:2]
'ahn '
>>> a[3:14:2]
'hn eri'
>>> a[5:15:4]
'nei'
>>> a[2:12:3]
'cnLr'
>>> a[0:10:1]
'Machine Le'
>>> a = "Python course"
>>> a[-1:-10:-2]
'ero o'
>>> a[-5:-11:-3]
'on'
>>> a[-3:-13:-4]
'r t'
>>> a[5:13]
'n course'
>>> a[0:13]
'Python course'
>>> #Does and don't
>>> a[8:6:2]
''
>>> #In positive striding highest to lowest not possible
>>> a[6:11:2]
' or'
>>> 
>>> a[-7:-4:-2]
''
>>> #In negative striding lowest to highest not possible
>>> a[-4:-7:-2]
'uc'
