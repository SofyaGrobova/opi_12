#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import time
import random
from queue import Queue
import math

queue = Queue()


class Shooter():
    def __init__(self, p, name):
        self.p = p
        self.i = 1
        self.name = name

    def prb(self):
        p = math.pow(self.p, self.i)
        self.i += 1
        return p


class ProducerThread(Thread):
    def run(self):
        count_shoots = 0
        while count_shoots < 20:
            i = random.randint(0, 5)
            queue.put(shoot[i])
            print(f"Стреляет {shoot[i].name}  -  {shoot[i].i} раз \n")
            time.sleep(0.1)
            count_shoots += 1


class ConsumerThread(Thread):
    def run(self):
        shoot_consumed = 0
        while shoot_consumed < 20:
            num = queue.get()
            queue.task_done()
            print (f"Вероятность попадания {num.i} выстрелов подряд -  {num.prb()} \n")
            time.sleep(0.1)
            shoot_consumed += 1


if __name__ == '__main__':
    str_1 = Shooter(0.5, "Иван ")
    str_2 = Shooter(0.79, "Сергей ")
    str_3 = Shooter(0.57, "Дима ")
    shoot = [str_1, str_2, str_3]
    ProducerThread().start()
    ConsumerThread().start()