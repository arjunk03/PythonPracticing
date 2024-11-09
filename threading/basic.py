import threading
import time
from pprint import pp, pprint


def new_func():
    pprint(threading.active_count())
    print()
    pprint(threading.enumerate())
    print()
    pprint(threading.current_thread())


def func():
    print("printing from function func")


# new_func()


# x = threading.Thread(target=func)
# x.start()
#
def sleep_func():
    time.sleep(2)
    print("hello from sleeping func")
    pprint(threading.current_thread().getName())


x = threading.Thread(target=sleep_func, name="sleeep")
x.start()
x.join()
pprint(threading.active_count())

pprint(threading.enumerate())

pprint(threading.current_thread())
pprint(threading.current_thread().getName())
