# 有顺序 不可变的list
# 不可变在于成员值不可修改 长度不可修改
tuple1 = (1, "2", 3)
print(len(tuple1))
print(tuple1.count(1))
# print(tuple1[3])  # 越界报错
print(tuple1[1:])
print(tuple1.index(1))  # findIndex

# tuple1[1] = 100  # 不可变

# packing
tuple2 = 1, 2, 3  # tuple packing (1,2,3)
# unpacking
a, b, c = tuple2  # tuple unpacking 类似于解构
print(a, b, c)

perosn = ('John', 20, 'New York')
name, age, city = perosn

x = 25
y = 35
y, x = x, y  # (x,y)
print(x, y)

tuple3 = ([1, 2, 3], 'Hi')
# tuple3[0] = 10 # 不可变 报错
tuple3[0][0] = 10
tuple4 = (1, 2, (3, 8))
print(tuple4)
# tuple 作为dict的key，tuple中的成员都必须是immutable
