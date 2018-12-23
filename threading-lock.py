#!/usr/bin/env python3
# coding: utf-8
# Date: 2018-12-26 20:07:51
# Author: zheng_oh
# email: 894389673@qq.com
import threading
sum = 0
loopsum = 1000000
lock = threading.Lock()


def myAdd():
    global sum, loopsum
    for x in range(1, loopsum):
        lock.acquire()
        sum += 1
        lock.release()


def myMinu():
    global sum, loopsum
    for x in range(1, loopsum):
        lock.acquire()
        sum -= 1
        lock.release()


if __name__ == '__main__':
    print("String...{0}".format(sum))
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done...{0}".format(sum))
