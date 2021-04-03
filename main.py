import discord
import os
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$dse'):
        dse_2022 = datetime(2022, 3, 31, 8, 30)
        time_now_hk = datetime.today() - timedelta(hours=16) #16 is the time diff between server and hk
        print(dse_2022 - time_now_hk)
        diff = (dse_2022 - time_now_hk).total_seconds()
        await message.channel.send("Time left from 2022 dse (31/3/2022 8:30am): "+ str(diff // (3600*24))  + " days " + str(diff%(3600*24)//3600) + " Hours " + str(diff%(3600*24)%3600//60) + " Minutes")

client.run(os.getenv('TOKEN'))

