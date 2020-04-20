import concurrent.futures
import time
import logging
import threading
from time import sleep

def func1():
    while(True):
        print("func 1")
        sleep(5)


def func2():
    while(True):
        print("func 2")
        sleep(5)

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.submit(func1)
        executor.submit(func2)


    '''

    executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)

    with executor:
        fs = []
        # 提交任务
        fs.append(executor.submit(func1))
        fs.append(executor.submit(func2))

        while True:
            time.sleep(1)
            logging.info(threading.enumerate())

            flag = True
            for f in fs:
                logging.info(f.done())
                flag = flag and f.done()
    '''
main()
