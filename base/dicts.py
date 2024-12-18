# dict key:value

# person
x = 'x'
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'x': {'age': 20}
}
print(person[x])
print(person['name'], person['age'], person['x']['age'])
print(person.get('name'))
print(person.keys())  # Object.keys
print(person.values())  # Object.values
print(person.items())  # Object.entries reruen like tuples

# dict被hash-table处理，无论size多少，取值的时间复杂度都是O(1)
# dict key的条件 1.不可变（引用数据类型不能作为key） 2.hashable 同时满足
# int float string boolean tuple（immutable list）immutable
