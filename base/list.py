# 顺序连续的数据
list1 = [6, 7, 8, 9]
list2 = list1[0:2]
print(list2)

# reserve
list1[::-1]

list3 = [1, 2, 1]
print(list3.count(1))  # 2

# concat
print(list1 + list2)

# * 复制
print(list1 * 3)

# list function
friends = ['Wilson', 'Mike', 'Nelson', 'Greg', 'Jimmy']
friends.insert(7, 'Nancy')
print(friends)
# insert 任意位置插入，其余后移
friends.insert(3, "Aaron")
# remove 移除特定元素(传入元素)
friends.remove('Mike')
# 清空数组 clear
# friends.clear()
# sort 排序 默认从小到大
friends.sort()
# reverse [::-1]
friends.reverse()
# append push
friends.append('Hans')
# pop return element
el = friends.pop()


print(el)
print(friends)
# copy 是浅层拷贝
x = [1, {'name': 'a'}]
y = x.copy()
y[0] = 0
y[1]['name'] = 'b'
print(x[len(x) - 1])
print(x)
print(len(friends))
