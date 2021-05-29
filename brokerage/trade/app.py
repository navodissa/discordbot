#!/usr/bin/env python

# WS client example

import asyncio
import websockets


async def hello():
    #uri = "wss://m-sl-trade-universal.directfn.com/smbws"
    uri = "wss://lkcentralprice.directfn.com/price"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        while True:
            name = input("Input: ")

            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
