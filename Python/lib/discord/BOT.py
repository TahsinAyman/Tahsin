import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have Logged In As\n{str(client.user)[:-5]}')
    await client.change_presence(activity=discord.Game('$help'))


@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await message.channel.send("Ok")


client.run('OTM5ODUwNDQ4NDczNTcxMzc4.Yf-18A.nm3zZPPJpKm055SEeXZJhSWMaHQ')
