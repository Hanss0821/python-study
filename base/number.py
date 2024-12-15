import math
print(3 + 5)

print(9/3)  # 除法会变float
print(10 % 5)

print(2**3)
print(3**2)

# abs 绝对值 |x|
print(abs(-10))  # 10

# pow 幂运算 2**3
print(pow(2, 10))  # 1024

# max 求最大值
print(max(1, 2, 3, 4, 5))  # 5

# min 求最小值
print(min(1, 2, 3, 4, 5))  # 1

# round 四舍五入
print(round(1.6))  # 2

# .5 偶数进，基数舍
print(round(1.5))  # 2->2
print(round(2.5))  # 3->2

# 类型转换
print(str(10) + '3')  # '10'
print(int(10.1))  # 10
print(float(10))  # 10.0


# 常数
print(math.e)
print(math.pi)
# 向下取整
print(math.floor(3.9))
# 向上取整
print(math.ceil(3.1))
