import discord
from discord.ext.commands import Bot
from discord.ext import commands
client = commands.Bot(command_prefix='!', description='summer project discord bot')
chan_id = '*****'
token = '************'
botname = '****'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('You are now using a simple bot that posts images based on what was said in the text channel')
    print('Thisis a list of all the words the bot responds to:')
    print('fine, OMG, omg, ow, feel, bad, rip, oic, smug, facepalm, pet, rude, triggered, gdi, hentai, my face, keikaku, bait, lewd, rofl')
    

# beginning of commands for summerbot
@client.command
async def halp():
    global chan_id
    prt1 = 'This is a list of all the words'
    prt2 = 'will respond to:'
    await client.send_message(client.get_channel(chan_id), prt1 + botname + prt2)

@client.event
async def on_message(message):
    if message.content.startswith('fine'):
        await client.send_file(message.channel, 'OS Path/memebase/thisisfine.png')
    if message.content.startswith('OMG'):
        await client.send_file(message.channel, 'OS Path/memebase/OMG.jpg')
    if message.content.startswith('omg'):
        await client.send_file(message.channel, 'OS Path/memebase/omg.gif')
    if message.content.startswith('ow'):
        await client.send_file(message.channel, 'OS Path/memebase/ow')
    if message.content.startswith('feel') | message.content.startswith('bad') | message.content.startswith('rip'):
        await client.send_file(message.channel, 'OS Path/memebase/pepe.jpg')
    if message.content.startswith('oic') | message.content.startswith('i see'):
        await client.send_file(message.channel, 'OS Path/memebase/oh.png')
    if message.content.startswith('smug'):
        await client.send_file(message.channel, 'OS Path/memebase/smug hikari.jpg')
    if message.content.startswith('facepalm'):
        await client.send_file(message.channel, 'OS Path/memebase/handtoface.jpg')
    if message.content.startswith('pet'):
        await client.send_file(message.channel, 'OS Path/memebase/headpat.gif')
    if message.content.startswith('rude'):
        await client.send_file(message.channel, 'OS Path/memebase/j0fzd2d.png')
    if message.content.startswith('triggered'):
        await client.send_file(message.channel, 'OS Path/memebase/image.png')
    if message.content.startswith('gdi') | message.content.startswith('fuck') | message.content.startswith('damn'):
        await client.send_file(message.channel, 'OS Path/memebase/HPxW4sQ.gif')
    if message.content.startswith('hentai'):
        await client.send_file(message.channel, 'OS Path/memebase/hentie.png')
    if message.content.startswith('my face'):
        await client.send_file(message.channel, 'OS Path/memebase/myface.jpg')
    if message.content.startswith('keikaku'):
        await client.send_file(message.channel, 'OS Path/memebase/calculated.png')
    if message.content.startswith('bait'):
        await client.send_file(message.channel, 'OS Path/memebase/BKWMkRP.png')
    if message.content.startswith('lewd'):
        await client.send_file(message.channel, 'OS Path/memebase/lewd.png')
    if message.content.startswith('rofl'):
        await client.send_file(message.channel, 'OS Path/memebase/rofl.gif')

client.run(token)
