Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Set{}
a = {4,5.6,"code",5+9j,True,False}
print(a)
{False, True, (5+9j), 4, 5.6, 'code'}
type(a)
<class 'set'>

#methods
#issubset
a = {1,2,3,5,6,7}
b = {5,6,7}
b.issubset(a)
True
a.issubset(b)
False

#issuperset()
c = {1,2,3,5,6,7}
d = {5,6,7}
c.issuperset(d)
True
d.issuperset(c)
False

#union
#merging of two sets
e = {3,4,5,6,8,9}
f = {1,2,3,9,10}
a.union(b)
{1, 2, 3, 5, 6, 7}
e.union(f)
{1, 2, 3, 4, 5, 6, 8, 9, 10}
#Set does not allows a duplicate values

#intersection()
g = {3,4,5,6,7,8}
h = {3,4,6,1,2,4,6}
g.intersection(h)
{3, 4, 6}
#it will print common values from both sets.

#update()

i = {10,20,30,40,50}
j = {40,50,60,70,80}
i
{50, 20, 40, 10, 30}
i.update(j)
i
{70, 40, 10, 80, 50, 20, 60, 30}
#Updating - the sets i is updated j values is updated to i than output prints {70, 40, 10, 80, 50, 20, 60, 30}.
j.update(i)
j
{70, 40, 10, 80, 50, 20, 60, 30}


#difference
k = {4,5,6,7,8,9,10,11}
l = {3,4,5,6,7,11,12,13}
a.difference(b)
{1, 2, 3}
b.difference(a)
set()
k.difference(k)
set()
k.difference(l)
{8, 9, 10}
l.difference(k)
{3, 12, 13}
#It will k values and avoid common values in the both sets

#symmetric_difference
a = {3,4,5,6,7,8,9}
b = {1,3,5,7,8,11,13}
a.symmetric_difference(b)
{1, 4, 6, 9, 11, 13}
b.symmetric_difference(a)
{1, 4, 6, 9, 11, 13}
#it will print normal values in the both sets and avoid commom values and print both sets values in output.

#intersection_update
a = {3,4,5,6,7,8,9}
b = {1,3,5,7,8,11,13}
a.intersection_update(b)
a
{8, 3, 5, 7}
b
{1, 3, 5, 7, 8, 11, 13}
b.intersection_update(a)
b
{8, 3, 5, 7}
#it will print common values from both sets and updating the set a and b


#difference_update
a = {3,4,5,6,7,8,9}
b = {1,3,5,7,8,11,13}
a.difference_update(b)
a
{4, 6, 9}
b
{1, 3, 5, 7, 8, 11, 13}
b.difference_update(a)
b
{1, 3, 5, 7, 8, 11, 13}


#symmetric_difference_update
a = {3,4,5,6,7,8,9}
b = {1,3,5,7,8,11,13}
a.symmetric_difference_update(b)
a
{1, 4, 6, 9, 11, 13}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}
b
{3, 4, 5, 6, 7, 8, 9}


#pop
>>> a = {4,5,6,8,9,7}
>>> a.pop()
4
>>> #pop is deleting the starting value from set and should not any agrument in the pop(5) gives error
>>> 
>>> 
>>> #remove
>>> a.remove(5)
>>> a
{6, 7, 8, 9}
>>> #5 remove from set
>>> 
>>> #discard
>>> a = {4,5,6,8,9,7}
>>> a.discard(7)
>>> a
{4, 5, 6, 8, 9}
>>> 
>>> #copy
>>> a = {4,5,6,8,9,7}
>>> a.copy()
{4, 5, 6, 7, 8, 9}
>>> 
>>> #clear
>>> a = {4,5,6,8,9,7}
>>> a.clear()
>>> a
set()
>>> 
>>> b = set()
>>> b.add(2)
>>> b
{2}
>>> #add means adding the values in set
>>> 
>>> #len
>>> a = {4,5,6,8,9,7}
>>> len(a)
6
>>> #not allow count method in the set
>>> 
>>> #not allow index method in the set
>>> 
>>> a = {4,5,6,7,8}
>>> b = {4,5,6,9,10,11}
>>> a.isdisjoint(b)
False
>>> #because same values is present in both sets prints output false other wise true.
>>> 
