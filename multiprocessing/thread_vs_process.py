import time
import threading
import multiprocessing


def square(numbers):
    for val in numbers:
        print("the square of num %d is %d" % (val, val * val))


def cube(numbers):
    for val in numbers:
        print("the cube of num %d is %d" % (val, val * val * val))


num_list = [1, 2, 3, 4]
p1 = multiprocessing.Process(target=square, args=(num_list,))
p2 = multiprocessing.Process(target=cube, args=(num_list,))

p1.start()
p2.start()

p1.join()
p2.join()

print("proocess completed")


square_list = []


def square_new(numbers):
    global square_list

    for val in numbers:
        print("the square of num %d is %d" % (val, val * val))
        square_list.append(val * val)
        print("square inside :", square_list)


num_list = [1, 2, 3, 4]
p1 = multiprocessing.Process(target=square_new, args=(num_list,))
# p2 = multiprocessing.Process(target=cube, args=(num_list,))

p1.start()
# p2.start()

p1.join()
# p2.join()
print(" square lit i:s", square_list)
print("proocess completed")


square_list = []


def square_new(numbers):
    global square_list

    for val in numbers:
        print("the square of num %d is %d" % (val, val * val))
        square_list.append(val * val)
        print("square inside :", square_list)


num_list = [1, 2, 3, 4]
p1 = threading.Thread(target=square_new, args=(num_list,))
# p2 = multiprocessing.Process(target=cube, args=(num_list,))

p1.start()
# p2.start()

p1.join()
# p2.join()
print(" square lit i:s", square_list)
print("proocess completed")
