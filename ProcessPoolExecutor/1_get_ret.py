# -*- coding:utf-8 -*-
# @Time		:2018/11/27 5:21 PM
# @Author	:Coast Cao
import concurrent.futures
import math
import time
from time import sleep

def func(m, n):
    if(n % 3 == 0):
        sleep(3)
    return "%d-%d response" % (m,n)

nums = [1,2,3,4,5,6,7,8,9,10]
def main():
    st = time.time()

    ret = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for resp in executor.map(func, nums, [100] * len(nums)):
            ret.append(resp)
    print(ret)
    ed = time.time()
    print(ed - st)

if __name__ == '__main__':
    main()