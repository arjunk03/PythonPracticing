import threading
import time


meeting = threading.Event()


def hold_meeting():
    meeting.set()
    print("meeting started")

    time.sleep(3)

    print("meeting complete. clearing te room")
    meeting.clear()


def enter_meeting_room():
    time.sleep(1)
    meeting.wait()

    while meeting.is_set():
        print("watiting for the meeting to end")
        time.sleep(0.5)

    print("meeting complteed. entering the room")


t1 = threading.Thread(target=hold_meeting)
t2 = threading.Thread(target=enter_meeting_room)

t1.start()
t2.start()

t1.join()
t2.join()
