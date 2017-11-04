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
    await client.send_file(client.get_channel('chan_id'), 'filepath')
@client.command()
async def smug():
    await client.send_file(client.get_channel('chan_id'), 'filepath')
@client.command()
async def facepalm():
    await client.send_file(client.get_channel('chan_id'), 'filepath')
@client.command()
async def pet():
    await client.send_file(client.get_channel('chan_id'), 'filepath')
@client.command()
async def lewd():
    await client.send_file(client.get_channel('chan_id'), 'filepath')
@client.command()
async def mfw():
    await client.send_file(client.get_channel('chan_id'), 'filepath')
@client.command()
async def keikaku():
    await client.send_file(client.get_channel('chan_id'), 'filepath')
@client.command()
async def bait():
    await client.send_file(client.get_channel('chan_id'), 'filepath')


client.run("bot_token")
