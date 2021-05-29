#!/usr/bin/env python

import asyncio
import websockets
import authentication as auth
import userRequests as usrreq


async def run():
    uri = "wss://m-sl-trade-universal.directfn.com/smbws"
    # Start running the websocket
    async with websockets.connect(uri, ping_interval=None) as websocket:
        # call the authentication and cast it to String to be
        client = auth.UserAuth()
        req = str(client.authenticate())
        await websocket.send(req)
        response = await websocket.recv()
        print(f"< {response}")
        client.setAuthValues(response)
        custDetailsReq = str(usrreq.getCustomerDetails(client))
        print(f"< {custDetailsReq}")
        await websocket.send(custDetailsReq)
        response = await websocket.recv()
        print(f"< {response}")

        # while True:
        #     req = input("Input:")

        #     await websocket.send(req)
        #     print(f"> {req}")

        #     greeting = await websocket.recv()
        #     print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(run())
