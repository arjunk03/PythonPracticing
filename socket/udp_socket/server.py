import time
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(0.2)
    s.bind((socket.gethostname(), 4571))

    i = 1
    while True:
        message = bytes("Message #" + str(i), "utf-8")
        s.sendto(message, ("localhost", 37020))
        print("message sent")

        time.sleep(2)

        i += 1
