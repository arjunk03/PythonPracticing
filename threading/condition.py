import random
import time
import threading

cond = threading.Condition()

container = []
counter = 1
more_to_come = True


def produce():
    global container
    global counter
    global more_to_come

    for i in range(5):
        time.sleep(random.randrange(2, 5))
        cond.acquire()

        item = "News item #" + str(counter)

        container.append(item)
        counter += 1

        print("produced : ", item)
        cond.notify_all()

        cond.release()
    more_to_come = False


def consume():
    global more_to_come

    while more_to_come:
        cond.acquire()
        cond.wait()

        time.sleep(random.random())
        print(threading.current_thread().name, " acquired ", container[-1])
        cond.release()


prod = threading.Thread(target=produce)
cons1 = threading.Thread(target=consume, name="cons1")
cons2 = threading.Thread(target=consume, name="cons2")
cons3 = threading.Thread(target=consume, name="cons3")

threads = [prod, cons1, cons2, cons3]

for th in threads:
    th.start()

for th in threads:
    th.join()

time.sleep(1)
print("all done")
