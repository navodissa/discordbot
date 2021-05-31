
import app
import asyncio


async def main():
    inp = input('Input')
    apl = app.Application()
    apl.setRequest(inp)
    await apl.hello()
    while True:
        inp = input('Input')
        apl.setRequest(inp)


main()
