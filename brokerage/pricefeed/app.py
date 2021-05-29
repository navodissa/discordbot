#!/usr/bin/env python

import asyncio
import websockets
import time


async def hello():
    #uri = "wss://m-sl-trade-universal.directfn.com/smbws"
    uri = "wss://lkcentralprice.directfn.com/price"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        auth_req = '115{"AUTHVER":"10","LOGINIP":"","CLVER":"1.0.0","PDM":"56","LAN":"EN","METAVER":"0","SSOTOK":"DEMO1UNI","SSOTYPE":"2"}'
        await websocket.send(auth_req)
        response = await websocket.recv()
        print(f"< {response}")

        init_req = ['22{"40":"7","E":"LKCSE"}',
                    '33{"80":"17","E":"LKCSE","S":"ASI"}',
                    '51{"40":"64","E":"LKCSE","TT":"1","MKT":"N","L":"EN"}',
                    '51{"40":"64","E":"LKCSE","TT":"3","MKT":"N","L":"EN"}',
                    '51{"40":"64","E":"LKCSE","TT":"4","MKT":"N","L":"EN"}',
                    '32{"81":"17","E":"LKCSE","S":"ASI"}',
                    '33{"80":"17","E":"LKCSE","S":"ASI"}',
                    '23{"40":"32","E":"LKCSE"}',
                    '32{"81":"7","E":"LKCSE","S":"ASI"}',
                    '40{"80":"0","E":"LKCSE","S":"AAF.N0000`N"}',
                    '40{"80":"0","E":"LKCSE","S":"AAF.R0000`N"}',
                    '41{"80":"0","E":"LKCSE","S":"AAIC.N0000`N"}',
                    '41{"80":"0","E":"LKCSE","S":"AAIC.R0000`N"}',
                    '41{"80":"0","E":"LKCSE","S":"ABAN.N0000`N"}',
                    '41{"80":"0","E":"LKCSE","S":"TKYO.N0000`N"}']

        for req in range(0, len(init_req)):
            await websocket.send(init_req[req])
            response = await websocket.recv()
            print(f"< {response}")
            time.sleep(0.5)

        while True:
            new_req = input("Input:")

            await websocket.send(new_req)
            print(f"> {new_req}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
