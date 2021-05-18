from discord.ext import commands
import os
import traceback
import numpy as np

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

'''
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'test':
        await message.channel.send('テストだよ')
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
'''
    
@bot.command()
async def neko(ctx):
    a = np.randam.randint(1, 4)
    if a == 1:
        await ctx.send('にゃごにゃご')
    elif a == 2:
        await ctx.send('にゃーん')
    elif a == 3:
        await ctx.send('ふしゃー！')
    else:
        await ctx.send('ごろにゃん')
    
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

@bot.command()
async def dancing(ctx):
    await ctx.send('（ツ）ｺﾛﾝｺﾛﾝ')

@bot.command()
async def yes(ctx):
    await ctx.send('(ツ)<ｿｳ!')

@bot.command()
async def rice(ctx):
    await ctx.send('コメ・バルゴ')
    
@bot.command()
async def morning(ctx):
    await ctx.send('アサ・バルゴ')
    
@bot.command()
async def noon(ctx):
    await ctx.send('ヒル・バルゴ')
    
@bot.command()
async def night(ctx):
    await ctx.send('ヨル・バルゴ')

   
bot.run(token)
