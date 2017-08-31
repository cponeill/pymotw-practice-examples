#!/usr/bin/env python3
# coroutinue.py

import asyncio

async def coroutine():
    print('in coroutine')

event_loop = asyncio.get_event_loop()
try:
    print("starting coroutinue")
    coro = coroutine()
    print("entering event loop")
    event_loop.run_until_complete(coro)
finally:
    print("closing loop")
    event_loop.close()
