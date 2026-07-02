Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a = {"name" : "prabhs" , "city" : "vija"}
print(a)
{'name': 'prabhs', 'city': 'vija'}
type(a)
<class 'dict'>
#dictonary is in pair format ,but set is just print the values in the set.

a = {"name" : "prabhs" , "maild" : "prabhas@gamil.com" ,"mobileno" : "4561851438"}
print(a)
{'name': 'prabhs', 'maild': 'prabhas@gamil.com', 'mobileno': '4561851438'}
#dictonary methods
a.key() #key()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.key() #key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
a.keys()
dict_keys(['name', 'maild', 'mobileno'])

#values()
a.values()
dict_values(['prabhs', 'prabhas@gamil.com', '4561851438'])

#items()
a.items()
dict_items([('name', 'prabhs'), ('maild', 'prabhas@gamil.com'), ('mobileno', '4561851438')])

a = {"python","course","month"}
a
{'month', 'course', 'python'}
#update()
a.update({"name" : "prabhas"})
a
{'name', 'month', 'course', 'python'}
a = {"course":"python","institue" : "codegnan","month" : "july"}
a
{'course': 'python', 'institue': 'codegnan', 'month': 'july'}
a.update({"name" : "prabhas"})
a
{'course': 'python', 'institue': 'codegnan', 'month': 'july', 'name': 'prabhas'}

a.update({"name" : "prabhas"},{"year" : 2026})
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.update({"name" : "prabhas"},{"year" : 2026})
TypeError: update expected at most 1 argument, got 2
#because not passes more than 1 argument

a.update({"lastyear" : 2025 , "year" : 2026})#We want pass more than 1 argument like this
a
{'course': 'python', 'institue': 'codegnan', 'month': 'july', 'name': 'prabhas', 'lastyear': 2025, 'year': 2026}

a  = {"year":2026 , "month" : "july"}
a.setdeafult("date",2)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.setdeafult("date",2)
AttributeError: 'dict' object has no attribute 'setdeafult'. Did you mean: 'setdefault'?
a.setdeafult("data",2)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.setdeafult("data",2)
AttributeError: 'dict' object has no attribute 'setdeafult'. Did you mean: 'setdefault'?
a.setdefault("data",2)
2
a
{'year': 2026, 'month': 'july', 'data': 2}
#it is automatically default the in the dictonary and pushes into it

a = {"time" : 2 , "hours" : 1 , "min" : 3}
a.pop("time") #pop will delete key and don't passes position number in pop()
2
a
{'hours': 1, 'min': 3}
a.popitem()
('min', 3)
#it will pop key and value from last of the dictonary.
a
{'hours': 1}

a = {"college" : "IIITDMK" , "branch" : "cse"}
a.get("college")#read the key value and everytime key passes in get argument .
'IIITDMK'
#asscessing
a["branch"]
'cse'


#copy()
a = {"time" : 2 , "hours" : 1 , "min" : 3}
b = a.copy()
b
{'time': 2, 'hours': 1, 'min': 3}

#clear()
a.clear()
a
{}

#We should add values into dictonary use update.
a.update({"Name" : "Prabhas Naidu"})
a
{'Name': 'Prabhas Naidu'}
>>> 
>>> a = {"name" : "prabhas","course" : "python" , "year" : 2026}
>>> len(a)
3
>>> 
>>> #dictonary does not allow duplicates
>>> a.count() #and not allow count method
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.count() #and not allow count method
AttributeError: 'dict' object has no attribute 'count'
>>> 
>>> a = {"name" : "prabhas","course" : "python" , "name" : "prabhas"}
>>> a
{'name': 'prabhas', 'course': 'python'}
>>> #Does not duplicates values
>>> 
>>> a = {"name" : "prabhas","course" : "python" , "name" : "naidu"}
>>> a
{'name': 'naidu', 'course': 'python'}
>>> #It is take new key and value
>>> 
>>> a = {"name1" : "prabhas","course" : "python" , "name2" : "prabhas"}
>>> a
{'name1': 'prabhas', 'course': 'python', 'name2': 'prabhas'}
>>> #because key are differnet for both names.
>>> 
>>> #index()
>>> #in dict object has no attribute 'index'
>>> 
>>> #one key giving no of values using list
>>> a = {"ids" : [10,20,30] , "names" : ["sumanth","prabhas",]}
>>> a = {"ids" : [10,20,30] , "names" : ["sumanth","prabhas","jeesy"]}
>>> a
{'ids': [10, 20, 30], 'names': ['sumanth', 'prabhas', 'jeesy']}
>>> a.update({"marks" : [40,30,60]})
>>> a
{'ids': [10, 20, 30], 'names': ['sumanth', 'prabhas', 'jeesy'], 'marks': [40, 30, 60]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['ids', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['sumanth', 'prabhas', 'jeesy'], [40, 30, 60]])
>>> a.items()
dict_items([('ids', [10, 20, 30]), ('names', ['sumanth', 'prabhas', 'jeesy']), ('marks', [40, 30, 60])])
>>> #passing mupitle values for the one key in dictonary .
>>> 
