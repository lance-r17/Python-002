# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数

import time

def timer(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        ret = func(*args,**kwargs)
        print(f'--- {time.time() - start_time} seconds ---')
        return ret
    return inner

@timer
def func_without_args():
    print('start to process func without args')
    time.sleep(1)

func_without_args()

@timer
def func_with_sleep(s):
    print('start to process func with sleep control')
    time.sleep(s)

func_with_sleep(3)