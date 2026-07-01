Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a = [2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b = [5]
type(b)
<class 'list'>
#Methods in list
a = ["hi","hello","python"]
a.append("cousre")
a
['hi', 'hello', 'python', 'cousre']
#Add at end of the list and should not passes more than 1 agrument in the a.append().
#but passes like this
a.append(["hello","world"])
a
['hi', 'hello', 'python', 'cousre', ['hello', 'world']]
#give like a list and the add in the list and the end of the list.

#extend()
a = ["ml","ai","ds"]
a.extend(["python","c","c++"])
a
['ml', 'ai', 'ds', 'python', 'c', 'c++']
#it is also agrument is add at end .

#insert()
a = ["vija","hyd"]
a.insert(1,"vzg")
a
['vija', 'vzg', 'hyd']
# At particular position we are passing the values.

#Index()
a = ["black","white","pink","red"]
a.index("white")
1
#it's shows the index value of white .

#copy()
a.copy()
['black', 'white', 'pink', 'red']
b = a.copy()
b
['black', 'white', 'pink', 'red']

#count
b.count("pink")
1
#it is counting the how many words in the list , pink is one word in the list prints value 1 at outptut.


#sort()
a = ["grapes","apples","mango","banana"]
a.sort()
a
['apples', 'banana', 'grapes', 'mango']

b = [0,3,4,6,7,8,9,1,2]
>>> b.sort()
>>> b
[0, 1, 2, 3, 4, 6, 7, 8, 9]
>>> #The sort is printing in the order wise
>>> 
>>> #reverse()
>>> a = [7,8,9,10,12,40,60]
>>> a.reverse()
>>> a
[60, 40, 12, 10, 9, 8, 7]
>>> #Reversing the values in the list.
>>> a.
SyntaxError: invalid syntax
>>> 
>>> #pop()
>>> a = ["grapes","apples","mango","banana"]
>>> a.pop()
'banana'
>>> #a.pop(apples) should not pass like the shows error and pop() empty and pass index in pop(2) then pops that value from list.
>>> 
>>> a.pop(1)
'apples'
>>> a
['grapes', 'mango']
>>> #and pop() means completely delete from list .
>>> 
>>> 
>>> #remove
>>> a.remove("grapes")
>>> a
['mango']
>>> #Remove which we want remove from the list that should pass in the agrument like this a.remove("grapes").
>>> 
>>> #len
>>> a = ["pooja","priya","prince","sweety"]
>>> len(a)
4
>>> b = "prahbas"
>>> len(b)
7
>>> #In list len will be take has word and calculate len of the list , in string it is calculating character in the word.
>>> 
>>> #clear
>>> a.clear
<built-in method clear of list object at 0x0000018342193F40>
>>> a.clear()
>>> a
[]
>>> #total list values is cleared
