#! /usr/bin/env python3
# signal.py

import signal
import os
import time


def receive_signal(signum, stack):
    print('Received:', signum)


signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# Print the process ID so it can be used with 'kill'
# to send this program signals.
print('My PID is:', os.getpid())


while True:
    print('Waiting... ')
    time.sleep(3)
