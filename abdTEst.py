from ppadb.client import Client
import threading
import random

adb = Client(host="127.0.0.1", port=5037)
devices = adb.devices()

if len(devices) == 0:
    quit()

device = devices[0]
threads = []


def tread_func(x, y):
    while True:
        device.shell(f'input tap {x} {y}')


for i in range(10):
    t = threading.Thread(target=tread_func, args=(random.randint(300, 600), random.randint(600, 800)))
    t.daemon = True
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()
