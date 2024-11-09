import threading
import time


amount = 0


def deposit(dep_amt, dep_lock):
    global amount

    for i in range(dep_amt):
        dep_lock.acquire()
        amount += 1
        dep_lock.release()


def two_deposit_threads(dep_amount):
    lock = threading.Lock()
    t1 = threading.Thread(target=deposit, args=(dep_amount, lock))
    t2 = threading.Thread(target=deposit, args=(dep_amount, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


two_deposit_threads(10)
print("Balance amount is :", amount)


amount = 0
two_deposit_threads(1000)
print("Balance amount is :", amount)

amount = 0
two_deposit_threads(10000)
print("Balance amount is :", amount)

amount = 0
two_deposit_threads(100000)
print("Balance amount is :", amount)

amount = 0
two_deposit_threads(1000000)
print("Balance amount is :", amount)


# amount = 0
# two_deposit_threads(1000000)
# print("Balance amount is :", amount)
# amount = 0
# two_deposit_threads(10000000)
# print("Balance amount is :", amount)
# amount = 0
# two_deposit_threads(100000000)
# print("Balance amount is :", amount)
# amount = 0
# two_deposit_threads(1000000000)
# print("Balance amount is :", amount)
# amount = 0
# two_deposit_threads(10000000000)
# print("Balance amount is :", amount)
# amount = 0
# two_deposit_threads(100000000000)
# print("Balance amount is :", amount)
# amount = 0
# two_deposit_threads(1000000000000)
# print("Balance amount is :", amount)
