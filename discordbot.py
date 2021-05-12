from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


'''
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
'''
    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
@bot.command()
async def inu(ctx):
    await ctx.send('わんわん')
    
@bot.command()
async def hato(ctx):
    await ctx.send('くるっぽー')
    
@bot.command()
async def buta(ctx):
    await ctx.send('ぶひぶひ')

@bot.command()
async def marimo(ctx):
    await ctx.send('(ツ)<ﾓﾛﾍｲﾔｯ')
    
@bot.command()
async def niwatori(ctx):
    await ctx.send('こけこっこー')
    
@bot.command()
async def maguro(ctx):
    await ctx.send('ノア・バルゴ')

@bot.command()
async def kurumi(ctx):
    await ctx.send(':tophat:<ｲｵｽ......')


bot.run(token)
