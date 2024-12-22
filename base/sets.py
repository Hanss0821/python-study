# 无序，唯一对象
# {"a","b",20} 无key的dict 无重复元素
# new Set()
mySet = {1, 2, 3, 1, 1}
mySet2 = set({1, 1, 1, 3, 5})
mySet3 = set([1, 2, 1, 4, 5, 6])

# add
mySet.add(10)
mySet.add(10)
# discard delete
mySet.discard(10)
# clear
mySet.clear()
newSet = mySet.copy()

print(mySet)
print(mySet2)
print(mySet3)


a = {1, 3, 4, 5}
b = {3, 4, 7, 8}

print(a.difference(b))  # a-b {1,5}
print(b.difference(a))  # b-a {7,8}
print(a.intersection(b))  # a & b {3,4}
print(b.intersection(a))  # b & a {3,4}
print(a.union(b))  # a | b {1,3,4,5,7,8}
print(b.union(a))  # b | a {1,3,4,5,7,8}

# a与b没有交集 返回true isdisjoint
print(a.isdisjoint(b))  # false
# a是否b子集合 issubset
print(a.issubset(b))  # false
# a是否b超集（父集） issuperset
print(a.issuperset(b))  # false

# type() === typeof
print(type('asas'))  # <class 'str'>
print(type(3.0))  # <class 'float'>
