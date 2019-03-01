# -*- coding:utf-8 -*- 
# @Time		:2019/3/1 10:20 AM
# @Author	:Coast Cao

from time import sleep, time
import gc


def mem(way=1):
	print
	time()
	for i in range(10000000):
		if way == 1:
			pass
		else:  # way 2, 3
			del i

	print
	time()
	if way == 1 or way == 2:
		pass
	else:  # way 3
		gc.collect()
	print
	time()


if __name__ == "__main__":
	print
	"Test way 1: just pass"
	mem(way=1)
	sleep(20)
	print
	"Test way 2: just del"
	mem(way=2)
	sleep(20)
	print
	"Test way 3: del, and then gc.collect()"
	mem(way=3)
	sleep(20)