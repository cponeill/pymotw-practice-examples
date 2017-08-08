#!/usr/bin/env python3
# sleep.py

import time

template = '{} - {:02.f} - {:02.f}'

print(template.format(
    time.ctime(), time.time(), time.clock())
)

for i in range(3, 0, -1):
    print('Sleeping', i)
    time.sleep(i)
    print(template.format(
        time.ctime(), time.time(), time.clock())
    )
