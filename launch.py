import os
import threading


def infiniteloop1():
    print("launching the server")
    os.system("python app.py &")

def infiniteloop2():
    print("launching the chungus")
    os.system("python birdnest.py &")

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()