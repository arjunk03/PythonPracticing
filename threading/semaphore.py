import threading
import time

semaphore = threading.Semaphore()
# semaphore = threading.Semaphore(value=3)


def my_func():
    semaphore.acquire()

    time.sleep(0.1)
    print(threading.current_thread().name, " acquired the semaphore")
    print("Semaphore value is: ", semaphore._value)

    time.sleep(5)

    semaphore.release()

    print("Semaphore valu after relesae : ", semaphore._value)


t1 = threading.Thread(target=my_func)
t2 = threading.Thread(target=my_func)

print("Initial semaphore value : ", semaphore._value)


# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# time_end = time.time()
#
# print("Total time taken : ", time_end - time_start)


semaphore = threading.Semaphore(value=3)


t1 = threading.Thread(target=my_func)
t2 = threading.Thread(target=my_func)
t3 = threading.Thread(target=my_func)
t4 = threading.Thread(target=my_func)
t5 = threading.Thread(target=my_func)
t6 = threading.Thread(target=my_func)
t7 = threading.Thread(target=my_func)
t8 = threading.Thread(target=my_func)

time_start = time.time()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
time_end = time.time()

print("Total time taken : ", time_end - time_start)
