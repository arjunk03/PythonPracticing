from os import lockf
import time
import multiprocessing


def deposit_without_mp(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance += amount
    return balance


def withdraw_without_mp(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance -= amount
    return balance


def deposit_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value += amount


def withdraw_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value -= amount


def deposit_with_lock(balance, amount, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += amount
        lock.release()


def withdraw_with_lock(balance, amount, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= amount
        lock.release()


# balance = 600
# balance = deposit_without_mp(balance, 5)
# print("balance :", balance)
# balance = withdraw_without_mp(balance, 5)
# print("balance :", balance)
#
# balance = multiprocessing.Value("i", 600)
# deposit_without_lock(balance, 5)
# print("balance1 :", balance.value)
# withdraw_without_lock(balance, 5)
# print("balance :", balance.value)


# p1 = multiprocessing.Process(target=deposit_without_lock, args=(balance, 5))
# p2 = multiprocessing.Process(target=withdraw_without_lock, args=(balance, 5))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
# print("final balance: ", balance.value)
#
#

balance = multiprocessing.Value("i", 600)
lock = multiprocessing.Lock()
p1 = multiprocessing.Process(target=deposit_with_lock, args=(balance, 5, lock))
p2 = multiprocessing.Process(
    target=withdraw_with_lock, args=(balance, 5, lock))

p1.start()
p2.start()

p1.join()
p2.join()
print("final balance: ", balance.value)
