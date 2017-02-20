#! /usr/bin/env python3
# signal_alarm.py

import signal
import time


def receive_alarm(signum, stack):
    print('Alarm: ', time.ctime())

# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Before: ', time.ctime())
time.sleep(4)
print('After: ', time.ctime())
