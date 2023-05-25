# Built-in data types: list, tuple, dictionary, set
# Time Complexity: https://wiki.python.org/moin/TimeComplexity

# list: ordered, changeable, all duplicates
# O(1) for index and append, O(n) almost
a = []
a1 = [0] * 26
a2 = [1,2,33,4]
a.append(0)
a.append("2")   # python lists can hold various data types
a.remove("2")   # remove value
a.insert(0, "2")    # index, val
a.pop(1)    # pop index or last val (default)
a.reverse()
a.copy()
for i in a1:
    print(i)
print(a[::-1])  # slicing
print(a + a)    # concatenate two lists

# set: unordered, unchangeable (can add and remove), no duplicate
# O(1) for lookup/insert/del
s1 = set(a2)    # pass an iterable
s2 = {1,2,3,4}
s2.add(2)   # duplicate will be ignored
s2.add("s") # set can hold various data types
s2.remove(2)    # will raise an error if no 2 in set
s2.discard(2)   # will not raise an error
s2.pop()        # will remove a random item, error if pop from empty set
s2.clear()
s3 = {1,2,3,4,"fds"}
for i in s3:
    print(i)
# union two sets
s3.union(s1)
s3.update(s1)
# intersection
s3.intersection_update(s1)
s3.intersection(s2)
# union - intersection:
s3.symmetric_difference(s1)

# dict: ordered, changeable, no duplicates
d = {1:2,2:3,3:4,4:True}    # allow various data types
d.keys()
d.values()
d.items()
if 1 in d: print(True)  # if key in dict
d.update({2:5})
d.popitem() # pop last added item
del d[2]    # del unexisted item will raise an error
d.pop(1)     # remove item with key 1
d.clear()

# tuple: ordered, unchangeable, allow duplicates
t = (1,2,3,3,"s")   # allow various data types
print(t[1])         # 0 indexed
print(t[-1])        # last item, can also use slicing
t1 = t * 2          # duplicates each item in t
t3 = t + t1         # can add like list