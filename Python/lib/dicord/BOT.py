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
        sum = var[0]
        for i in var:
            if var.index(i) == 0:
                pass
            else:
                sum += i
        await message.channel.send('{0:.2f}'.format(sum))
    if message.content.startswith("$calculator sub"):
        msg = message.content[15:]
        var = [float(_) for _ in msg.strip().split('-')]
        sum = float(0)
        for i in var:
            sum -= i
        await message.channel.send('{0:.2f}'.format(sum))
    if message.content.startswith("$calculator mul"):
        msg = message.content[15:]
        var = [float(_) for _ in msg.strip().split('x')]
        sum = float(0)
        for i in var:
            sum *= i
        await message.channel.send('{0:.2f}'.format(sum))
    if message.content.startswith("$calculator div"):
        msg = message.content[15:]
        var = [float(_) for _ in msg.strip().split('/')]
        sum = float(0)
        for i in var:
            sum /= i
        await message.channel.send('{0:.2f}'.format(sum))
    if message.content.startswith("$sudo strike hecker."):
        await message.channel.send('Striking hecker.')
    if message.content.startswith(f"$count 1-{int}"):
        n = int(message.content[-1:])
        for i in range(1, n + 1):
            await message.channel.send(f"Number {i}")

with open('token.env', 'r') as file:
    TOKEN = file.read()
    client.run(TOKEN)