import discord
import os
from random import randrange
from datetime import datetime, timedelta
from refresh import keep_alive
from PIL import Image, ImageFont, ImageDraw 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$dse'):
        #time
        dse_2022 = datetime(2022, 3, 31, 8, 30)
        time_now_hk = datetime.today() - timedelta(hours=16) #16 is the time diff between server and hk
        print(dse_2022 - time_now_hk)
        diff = (dse_2022 - time_now_hk).total_seconds()
        line1 = "Time left 2022 dse"
        line2 = str(int(diff // (3600*24)))  + " days "
        line3 = str(int(diff%(3600*24)//3600)) + " Hours "
        line4 = str(int(diff%(3600*24)%3600//60)) + " Minutes"
        #2022 dse: 31/3/2022 8:30am

        #image processing
        img_path = "background" + str(randrange(1)) + ".jpg"
        print(img_path)
        img = Image.open(img_path)
        width, height = img.size
        font = ImageFont.truetype('futura.ttf', width//10)
        draw = ImageDraw.Draw(img)
        draw.text((20, height//5), line1, (255,255,255),font=font)
        draw.text((20, height//5*2), line2, (255,255,255),font=font)
        draw.text((20, height//5*3), line3, (255,255,255),font=font)
        draw.text((20, height//5*4), line4, (255,255,255),font=font)
        img.save('output.jpg')

        #await message.channel.send(text)

        await message.channel.send(file=discord.File('output.jpg'))
        os.remove("output.jpg")

keep_alive()
client.run(os.getenv('TOKEN'))
