import threading


sem = threading.Semaphore(3)
# thi creaetes problem in restricting te number of concurrent thread if release semaphore before acquire
# This will be suitable when we are waiting for a producer to produce data and then relese the sewmaphore
# and in the consmer, we will acquire the semaphore after reading it.
print(sem._value)
sem.release()
print(sem._value)
sem.release()
sem.release()
print(sem._value)


sem2 = threading.BoundedSemaphore(1)
print(sem2._value)
print("before acquire")
sem2.release()
print(sem2._value)
sem2.acquire()

print(sem2._value)

sem2.release()

print(sem2._value)
sem2.release()
