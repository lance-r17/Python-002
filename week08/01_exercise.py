# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

# list - 容器序列, 可变序列
list_a = [1, 'a']
list_b = list_a
print(list_b is list_a) # True
list_a[1] = 'b'
print(list_b is list_a) # True

# tuple - 容器序列, 不可变序列
tuple_a = tuple([1, 'a'])
try:
    tuple_a[1] = 'b'    # TypeError
except TypeError:
    print('tuple object does not support item assignment')

# str - 扁平序列, 不可变序列
str_a = 'abcdef'
try:
    str_a[0] = 1    # TypeError
except TypeError:
    print('str object does not support item assignment')

# dict - 容器, 可变
dict_a = { 'a': 10, 'b': 'str'}
dict_b = dict_a
print(dict_b is dict_a) # True
dict_a['b'] = 12
print(dict_b is dict_a) # True

# collections.deque - 容器序列, 可变序列
from collections import deque
deque_a = deque([1, 'a'])
deque_b = deque_a
print(deque_b is deque_a) # True
deque_a[1] = 'b'
print(deque_b is deque_a) # True