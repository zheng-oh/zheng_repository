#!/usr/bin/env python3
# coding: utf-8
# Date: 2018-12-26 20:26:47
# Author: zheng_oh
# email: 894389673@qq.com
import queue
import time
import threading


class Producer(threading.Thread):
    """docstring for Producer"""

    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for x in range(100):
                    count = count + 1
                    msg = '生成产品' + str(count)
                    # put往queue里面放一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    """docstring for Producer"""

    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for x in range(3):
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = queue.Queue()
    for x in range(500):
        queue.put('初始产品', str(x))
    for x in range(2):
        p = Producer()
        p.start()
    for x in range(5):
        c = Consumer()
        c.start()
