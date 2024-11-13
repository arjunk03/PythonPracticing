import threading
import time


semaphore = threading.Semaphore(0)

order_num = 0

# semaphore is acquired in one thread and it gets released in another thread.
# First it will release the semaphore then it will acquire that.
# Semaphore can be used to restrict the degree of concurrency.
# Means how many tread can execute at any point of time


def place_order():
    print("order placed")
    semaphore.acquire()
    print("customer order nmber : ", order_num)


def prepare_order():
    global order_num

    time.sleep(3)
    order_num += 1
    print("preparing order : ", order_num)
    semaphore.release()


for i in range(0, 6):
    t1 = threading.Thread(target=place_order)
    t2 = threading.Thread(target=prepare_order)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

print("program terminated")
