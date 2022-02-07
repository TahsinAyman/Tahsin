import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$calculator add"):
        msg = message.content[15:]
        var = [float(_) for _ in msg.strip().split('+')]
        sum = float(0)
        for i in var:
            sum += i
        await message.channel.send('{0:.2f}'.format(sum))


TOKEN = open('token.env', 'r').read()
client.run(TOKEN)
