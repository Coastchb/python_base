# -*- coding:utf-8 -*- 
# @Time		:2019/5/31 3:40 PM
# @Author	:Coast Cao

import itertools
import random

def main():
	ret = itertools.product(range(2), range(5))

	num = 5
	list_ret = list(ret)
	N = len(list_ret)

	for i in range(3):
		print("for iteration %d:" % i)

		random.shuffle(list_ret)

		split_ret = [list_ret[k:k+num] for k in range(int(N/num))]
		print(split_ret)



main()