# -*- coding:utf-8 -*-
#!/usr/bin/python3
import datetime


def getday(y=2018, m=10, d=7, n=100):
    the_date = datetime.datetime(y, m, d)
    result_date = the_date + datetime.timedelta()
    d = result_date.strftime('%Y-%m-%d')
    return d


print(getday())
