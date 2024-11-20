from multiprocessing import Pool
import time
import multiprocessing

import os


def cal_square(n):
    print(n, os.getpid())
    return n * n


result = []
num_list = [1, 2, 3, 4, 5]

p = Pool(processes=2)
result = p.map(cal_square, num_list * 2)
p.close()
p.join()


def sum_val(a, b):
    print(a, b, os.getpid())
    return a + b


result = []
num_list = [(1, 2), (2, 3), (5, 6)]

p = Pool()
result = p.starmap(sum_val, num_list)
p.close()
p.join()
