from multiprocessing import Pool
import os
import multiprocessing
import time


def cal_square(n):
    print(n, os.getpid())
    return n * n


result = []
num_list = [1, 2, 3, 4, 5]
for num in num_list:
    result.append(cal_square(num))


print(os.cpu_count())


result = []

p = Pool()
result = p.map(cal_square, num_list * 2)
p.close()

print(result)
