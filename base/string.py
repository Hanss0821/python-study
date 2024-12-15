# 有顺序 连续 字符
s1 = "Aloha"
print(s1[0])

print(s1[-5])  # s1[0]
print(s1[-5] == s1[0])

# slice  [start(inclued):end(excluded) : step(1)] 从左到右的索引区间进行切片
print(s1[0:3])  # s1[:3]
print(s1[2:])
print(s1[0:4:2])  # Ao
print(s1[::2])  # Aoa
print(s1[0:-1])  # Aloh
s1 = "Aloha"
# stop=None 表示切片停止时已经到达左端（包含起始索引 0）
print(s1[::-2])  # A

s2 = 'Hi \n"Lee"'
# \n 换行
print(s2)
# string + number 报错 不会做隐式类型转换

# len
print(len(s1))
# int
print(int("123"))
# float
print(float("123"))

print(s1.upper())
print(s1.lower())
# 检测是否全部大小写
print(s1.isupper())
print(s1.islower())
print(s1.index('h'))  # 查找字符的索引,不存在报错
print(s1.__len__())

print(s1.replace('h', 'H'))  # 全部替换

s3 = "Hello Today Is A Nice Day"
print(s3.split(' '))  # 分割成数组
print(list(s3))

sentence = "  hello world! {}".format([1, 'aaa'])  # 字符串插入变量 类似于js的模板字符串
print(sentence)

# 可指定参数顺序
# 参数部分可以任意数量，模板中通过索引访问需要渲染的参数
print("{2},{1},{0}".format(1, 2, 3))
# 也别名访问
print("{a},{b},{c}".format(a=1, b=2, c=3))

# fstring 3.6+ 模板字符串
myName = "Lee"
print(f"Hello my name is {myName}")

# count 计算某个字符出现的次数
print(s1.count('h'))
# find 相当于indexOf 不存在返回-1
print(s1.find('ccc'))

print(s1.startswith('A'))
print(s1.endswith('a'))

s4 = '10'
print(s4*6)  # 不是做乘法，是做拷贝
