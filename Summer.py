import discord
from discord.ext.commands import Bot
from discord.ext import commands
client = commands.Bot(command_prefix='s!', description='summer project discord bot')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)


# beginning of commands for summerbot
@client.command()
async def oh():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/oh.png')
@client.command()
async def smug():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/smug hikari.jpg')
@client.command()
async def facepalm():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/handtoface.jpg')
@client.command()
async def pet():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/headpat.gif')
@client.command()
async def lewd():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/hentie.png')
@client.command()
async def mfw():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/myface.jpg')
@client.command()
async def keikaku():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/calculated.png')
@client.command()
async def bait():
    await client.send_file(client.get_channel('324229388629573633'), 'C:/Users/Ian/Pictures/Fanart/Anime/BKWMkRP.png')


client.run("MzQ0MjYyNDMyMzUwNTM1Njgw.DGqK8g.u9tcG0ImcTXk-0SxjKD89ZqOC64")
