# -*- coding:utf-8 -*- 
# @Time		:2018/11/20 11:01 AM
# @Author	:Coast Cao

# mark 1: arg1 and arg2 can both be empty while calling mixed_star （This is the strength of function with *)

def single_star(*arg):
    print(arg)
    print(type(arg))
    print(arg[0])

def double_star(**arg):
    print(arg)
    print(type(arg))
    #keys = *arg        # Error
    print(*arg)
    #for i in (*arg):   # Error
    #    print(i)
    print(arg['a'])
    print(arg.items())

def mixed_star(arg0=0,*arg1,**arg2):
    print(arg0)
    print(type(arg0))
    print(arg1)
    print(arg2)

def main():
    print('single star:')
    single_star('a','b','c')
    #single_star()  # OK
    single_star(('a','b','c'))
    print('\n')

    print('double star:')
    double_star(a='a',b='b')
    #double_star(a:'a') # Error
    #double_star()      # OK
    print('\n')

    # mark 1
    print('mixed star:')
    mixed_star('a','b','c',d='d',e='e',f='f')
    mixed_star(arg0=1,a='a',b='b')
    mixed_star('a','b','c')
    print('\n')

    print('star applied to variable')
    list = ['a','b','c']
    print(*list)
    #print(**list)      # Error
    print('\n')

    dict = {'a':1,'b':2}
    print(*dict)
    #print(**dict)      # Error
    double_star(**dict)
    #double_star(dict)  # Error

main()