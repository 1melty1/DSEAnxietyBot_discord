import discord
import os, random, time
from datetime import datetime, timedelta
from refresh import keep_alive
from PIL import Image, ImageFont, ImageDraw, ImageFilter

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name=f"in {len(client.guilds)} servers| $dse")) #set status




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$dse'):
        #time
        dse_2022 = datetime(2022, 3, 31, 8, 30)
        time_now_hk = datetime.today() - timedelta(hours=16) #16 is the time diff between server and hk
        print("Ping time: ", datetime.today())
        print(dse_2022 - time_now_hk)
        diff = (dse_2022 - time_now_hk).total_seconds()
        line1 = "2022 DSE Time left"
        line2 = str(int(diff // (3600*24)))  + " days "
        line3 = str(int(diff%(3600*24)//3600)) + " Hours "
        line4 = str(int(diff%(3600*24)%3600//60)) + " Minutes"
        #2022 dse: 31/3/2022 8:30am

        loading_message = await message.channel.send('Appending text into Image... plz wait') #send loading message

        img_path = random.choice(os.listdir("resources/")) #choose randome background
        print(img_path)
        img = Image.open("resources/" + img_path)
        width, height = img.size
        if "c" in message.content:
          final_img = img
        else:
          final_img = img.filter(ImageFilter.GaussianBlur(radius = 20))
        font = ImageFont.truetype('futura.ttf', width//10)
        draw = ImageDraw.Draw(final_img)
        draw.text((20, height//5), line1, (255,255,255),font=font) #put text with alignment
        draw.text((20, height//5*2), line2, (255,255,255),font=font)
        draw.text((20, height//5*3), line3, (255,255,255),font=font)
        draw.text((20, height//5*4), line4, (255,255,255),font=font)

        output_path = 'output.png'
        final_img.save(output_path)
        
        await loading_message.delete() #delete the message before sending image
        
        if os.path.exists(output_path): #check if output file is generated and send correct message
          await message.channel.send(file=discord.File(output_path))
        else:
          await message.channel.send("Failed to export :(")

        #await message.channel.send(text)
        
        os.remove(output_path)



keep_alive()
client.run(os.getenv('TOKEN'))
