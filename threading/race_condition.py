import threading
import time


amount = 0


def deposit(dep_amt, dep_lock):
    global amount

    for i in range(dep_amt):
        dep_lock.acquire()
        # dep_lock.acquire(timeout=3)
        amount += 1
        dep_lock.release()


def two_deposit_threads(dep_amount):
    lock = threading.Lock()
    # lock = threading.RLock()
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


lck = threading.Lock()
print("first lock :", lck.acquire())
print("second lock :", lck.acquire(timeout=3))

# This Mdule, RLock will allow the same thread to acquire multiple times
# without releasing the previous lock the same thread has.
lck = threading.RLock()
print("first lock :", lck.acquire())
print("second lock :", lck.acquire(timeout=3))
