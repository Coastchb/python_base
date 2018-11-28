# -*- coding:utf-8 -*- 
# @Time		:2018/11/27 5:21 PM
# @Author	:Coast Cao
import concurrent.futures
import math
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    12346345346654656,
    1234236534564345345,
    1353464357345345345,
    115797848077099,
    115797848077099,
    ]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    st = time.time()
    for number in PRIMES:
        print("%d is prime: %s" %(number, is_prime(number)))
    ed = time.time()
    print("######")
    print(ed - st)
    print("######")

    #### the best ####
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    st = ed
    ed = time.time()
    print("######")
    print(ed - st)
    print("######")

    '''
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for number in PRIMES:
            prime = executor.map(is_prime, number)
            print('%d is prime: %s' % (number, prime))
    st = ed
    ed = time.time()
    print("######")
    print(ed - st)
    print("######")
    '''

    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for number in PRIMES:
            f = executor.submit(is_prime, number)
            ret = f.result()
            print('%d is prime: %s' % (number, ret))
    st = ed
    ed = time.time()
    print("######")
    print(ed - st)
    print("######")

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    st = ed
    ed = time.time()
    print("######")
    print(ed - st)
    print("######")

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for number in PRIMES:
            f = executor.submit(is_prime, number)
            ret = f.result()
            print('%d is prime: %s' % (number, ret))
    st = ed
    ed = time.time()
    print("######")
    print(ed - st)
    print("######")

if __name__ == '__main__':
    main()