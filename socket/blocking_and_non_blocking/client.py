import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 4571))
    s.setblocking(False)

    data = bytes("Hello server \n", "utf-8") * 1024 * 1024 * 10
    print("size of data sent : %i bytes" % len(data))

    assert s.send(data)
