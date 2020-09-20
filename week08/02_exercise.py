# 自定义一个 python 函数，实现 map() 函数的功能。

def new_map(f, iter):
    for i in iter:
        yield f(i)

square = lambda x: x*x
list_a = [1, 2, 3, 4, 5]

print('Results generated from new_map')
for r1 in new_map(square, list_a):
    print(r1)

print('Results generated from map')
for r2 in map(square, list_a):
    print(r2)