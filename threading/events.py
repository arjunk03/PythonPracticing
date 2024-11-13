import threading
import time


evnt = threading.Event()

evnt.set()
print(evnt.is_set())

evnt.wait()
print(evnt.is_set())

evnt.clear()
print(evnt.is_set())

print("reordered the statemetnt")
evnt.set()
print(evnt.is_set())

evnt.clear()
print(evnt.is_set())

evnt.wait()
print(evnt.is_set())
