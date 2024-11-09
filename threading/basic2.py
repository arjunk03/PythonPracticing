import threading
import time


def calc_square(n):
    result = n * n
    print(f" the square for {n} is {result}")


square_list = []
num_list = [2, 3, 4, 5]

for num in num_list:
    thread = threading.Thread(target=calc_square, args=(num,))
    square_list.append(thread)

    thread.start()
    thread.join()


class DerThread(threading.Thread):
    def run(self):
        time.sleep(2)
        print("hello from thread class, : ", threading.current_thread().name)


obj = DerThread()
obj.start()
obj.join()
print("contrl returned o main")


class Regular:
    def print_list(self):
        print("from the function inside class")


obj = Regular()

thread = threading.Thread(target=obj.print_list)
thread.start()
thread.join()
