# -*- coding:utf-8 -*- 
# @Time		:2019/2/28 3:36 PM
# @Author	:Coast Cao

def fun():
	n = 0
	print("label 0")
	yield ("Y %d" % n)

	n += 1
	print("label 1")
	yield  ("Y %d" % n)

	n += 1
	print ("label 2")

def fun1():
	for i in range(10):
		yield ("YY %d" % i)

def main():
	fun()		# no output

	print("output in for loop:")
	for out in fun():
		print("  output from fun():%s" % out)

	print("\n\n")
	for out in fun1():
		print(" output from fun1():%s" % out)
main()
