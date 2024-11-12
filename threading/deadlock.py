import threading
import time

data_one = 3
data_two = 5


def my_process(lock1, lock2):
    global data_one
    global data_two

    lock1.acquire()
    print("incrementing data one :", threading.current_thread().name)
    data_one += 1
    time.sleep(1)

    lock2.acquire()
    print("incrementing data two :", threading.current_thread().name)
    data_two += 1
    time.sleep(1)

    lock1.release()
    lock2.release()


# This will remove the chance of dead lock . release the lock one it is not needed

#     global data_one
#     global data_two
#
#     lock1.acquire()
#     print("incrementing data one :", threading.current_thread().name)
#     data_one += 1
#     time.sleep(1)
#
#     lock1.release()
#
#     lock2.acquire()
#     print("incrementing data two :", threading.current_thread().name)
#     data_two += 1
#     time.sleep(1)
#
#     lock2.release()


lock1 = threading.Lock()
lock2 = threading.Lock()

t1 = threading.Thread(target=my_process, args=(lock1, lock2))
t2 = threading.Thread(target=my_process, args=(lock2, lock1))

# To avoid deadlock, change the args order
# t1 = threading.Thread(target=my_process, args=(lock1, lock2))
# t2 = threading.Thread(target=my_process, args=(lock1, lock2))


t1.start()
t2.start()

t1.join()
t2.join()
