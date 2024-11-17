import time
import os
from multiprocessing import Process, current_process


def square(num):
    time.sleep(1)
    res = num * num
    print(" the square of the number %d is %d" % (num, res))


numbers = [1, 2, 3, 4]
start = time.time()

for num in numbers:
    square(num)

end = time.time()
print("total time : ", end - start)


def new_square(num):
    time.sleep(1)
    res = num * num

    process_id = os.getpid()
    print(" proess id: ", process_id)
    print(" the square of the number %d is %d" % (num, res))


numbers = [1, 2, 3, 4]
start = time.time()

for i, num in enumerate(numbers):
    process = Process(target=new_square, args=(num,))
    process.start()


process.join()

end = time.time()
print("total time : ", end - start)


def new_square_2(num):
    time.sleep(1)
    res = num * num

    process_id = current_process().pid
    process_name = current_process().name
    print(" proess id: ", process_id)
    print(" proess name: ", process_name)
    print(" the square of the number %d is %d" % (num, res))


numbers = [1, 2, 3, 4]
start = time.time()

for i, num in enumerate(numbers):
    process = Process(target=new_square_2, args=(num,))
    process.start()


process.join()

end = time.time()
print("total time : ", end - start)
