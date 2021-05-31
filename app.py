import discord as discord
import random
import time
import asyncio
import os
#import brokerage.trade.app as trade

TOKEN = ''

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'time!':
        response = time.time()
        await message.channel.send(response)
    elif message.content == 'balance!':
        #loop = asyncio.get_event_loop()
        # response = loop.run_until_complete(await trade.run())
        # response = await trade.run()
        await message.channel.send('Wait to be amazed')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# client.run('')
client.run(os.getenv('TOKEN'))
