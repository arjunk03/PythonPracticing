import time
import threading


def greet1():
    for i in range(6):
        print("hello")
        time.sleep(1)


def greet2():
    for i in range(6):
        print("hello 2")
        time.sleep(1)


start = time.time()
greet1()
greet2()
end = time.time()
print("total time: ", end - start)


start = time.time()
t1 = threading.Thread(target=greet1)
t2 = threading.Thread(target=greet2)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print("total time thread: ", end - start)
