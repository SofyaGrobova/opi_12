#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue
from threading import Thread, Lock
import math

eps = .0000001
q = Queue()
lock = Lock()


def sum():
    lock.acquire()
    x = -0.7
    pre = 0
    s = 0
    n = 0
    curr = (n + 1) * math.pow(x, n)
    s += curr
    n += 1
    while abs(curr - pre) > eps:
        pre = curr
        curr = (n + 1) * math.pow(x, n)
        n += 1
        s += curr
    q.put(s)
    lock.release()

def compare(x, y):
    result = x - y
    print(f"Результат {result}")


def func_y(x=-0.7):
    result = 1/(math.pow((1 - x), 2))
    return result


if __name__ == '__main__':
    thread1 = Thread(target=sum).start()
    thread2 = Thread(target=compare(q.get(), func_y())).start()