#!/usr/bin/env python3
import discord
from discord.ext import commands
import __token # you need to have __token.token variable
import sys

'''
peper the helper
================
it's a discord bot written in discord
(as you can see). the main purpese of
that bot is seein' the codes of bot
and understand the way how the bots
work in better way.
github: anilademyener/peper

used discord lib(s)
https://github.com/Rapptz/discord.py

other libs are os, sys etc.

file specifies
__*.py -> files we shouldn't commit to git
	  because we write important things
	  in that files (such as token) 
_*.py -> files we shouldn't use for maintain
	  because it might be beta version,
	  spaghetti code, broken code etc.
*.py -> they're usually normal py code and
	there is no any wrong with using them
'''

prefix = "r->" 

bot = commands.Bot(command_prefix=prefix)

@bot.command()
async def commands(ctx):
  await ctx.send("prefix = r->[command]\n \
		  ping\n \
		  os\n \
		  token\n")

@bot.command()
async def ping(ctx):
  await ctx.send("pong")

@bot.command()
async def os(ctx):
  await ctx.send("server os: " + sys.platform)

@bot.command()
async def token(ctx):
  await ctx.send("your token is: " + __token.token)

bot.run(__token.token)
