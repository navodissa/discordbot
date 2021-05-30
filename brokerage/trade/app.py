#!/usr/bin/env python

import asyncio
#from discord_bot.discordbot.brokerage.trade.externalValues import setterBalance
import websockets
from brokerage.trade import authentication as auth
from brokerage.trade import userRequests as usrreq
# import authentication as auth
# import userRequests as usrreq
import json


def getterBalance(self):
    return self.balance


def setterBalance(self, balance):
    self.balance = balance


async def run():
    uri = "wss://m-sl-trade-universal.directfn.com/smbws"
    # Start running the websocket
    balance = ""
    # with create_connection(uri) as websocket:
    # call the authentication and cast it to String to be
    async with websockets.connect(uri, ping_interval=None) as websocket:
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
        cus_res = json.loads(response)
        balance = cus_res['DAT']['cshAccLst'][0]['balance']
        print(balance)
        return balance

# if __name__ == '__main__':
#     run()

    # while True:
    #     req = input("Input:")

    #     await websocket.send(req)
    #     print(f"> {req}")

    #     greeting = await websocket.recv()
    #     print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(run())
