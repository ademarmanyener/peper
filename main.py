#!/usr/bin/env python3
import discord
from discord.ext import commands
from __custom import * # __custom.py - CustomApplication() classname
from __token import token # __token.py - token variable
from __user_info import user_info # __user_info.py - user_info dictionary
import sys, os

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

class BaseApplication:
  app_id = "peper"
  app_title = "Peper the Helper"
  prefix = "." + "PPR" + " RUNX _> "
  bot = commands.Bot(command_prefix=prefix)

  def print_b_text(message):
    print("\n\t", end="")
    for letter in str(message):
      print("#", end="")
    print("\n", end="")
    print("\t" + message)
    print("\t", end="")
    for letter in str(message):
      print("#", end="")
    print("\n")
    return

  def print_m_text(message):
    print("\n\t>> " + message + "\n")
    return

class MainApplication(BaseApplication):

  ###################
  #   bot command
  ###################

  @BaseApplication.bot.command()
  async def PUT(ctx, msg:str="<Null>"):
    await ctx.channel.purge(limit=2)
    await ctx.channel.send(msg)

  @BaseApplication.bot.command()
  async def WHO(ctx):
    await ctx.channel.send("not ready yet")
    return

  @BaseApplication.bot.command()
  async def MAN(ctx, special:str=None):
    if special == None:
      await ctx.channel.send("DEFAULT MAN PAGE")
      await ctx.channel.send("================")
      await ctx.channel.send("L> CLR S ALL OR CLR D [NUMBER]")
      await ctx.channel.send("L> INF LIST OR INF [USER]")
    else:
      await ctx.channel.send("not empty")
    return

  @BaseApplication.bot.command()
  async def CLR(ctx, r_type, amount):
    try:
      if r_type.lower() == "d":
        await ctx.channel.purge(limit=int(amount) + 1)
      if r_type.lower() == "s":
        if str(amount).lower() == "all":
          await ctx.channel.purge(limit=99999999)
      if r_type.lower() == "x":
        return
    except:
      await ctx.channel.send("exception")
    return

  @BaseApplication.bot.command()
  async def PNG(ctx):
    await ctx.send("pong")
    return

  @BaseApplication.bot.command()
  async def INF(ctx, user):
    if user.lower() == "list":
      for user in user_info:
        await ctx.send(user)
    else:
      if user.lower() in user_info:
        await ctx.send(user.lower() + " ==> " + user_info[user.lower()])
      else:
        await ctx.send("who tf is this?")
    return

  @BaseApplication.bot.command()
  async def PLF(ctx): 
    await ctx.send("platform: " + sys.platform)
    return

  ###################
  #   bot event 
  ###################

  @BaseApplication.bot.event
  async def on_connect():
    BaseApplication.print_b_text(BaseApplication.app_title + " is connecting.")
    return

  @BaseApplication.bot.event
  async def on_disconnect():
    BaseApplication.print_b_text(BaseApplication.app_title + " is disconnecting.")
    return

  @BaseApplication.bot.event
  async def on_ready():
    BaseApplication.print_b_text(BaseApplication.app_title + " is ready. Logged in as: " + BaseApplication.bot.user.name)
    return

  @BaseApplication.bot.event
  async def on_error(self, ctx, *args, **kwargs):
    await ctx.channel.send("hey yo! wtf is that command nigger")

  def main(self):
    BaseApplication.bot.run(token)
    return

'''
if you want to default functions
use MainApplication() class

but if you want to use a custom
version and use functions you
wrote then use CustomApplication()
class and write your functions
(events or commands) in __custom.py
and of course don't forget to
from __custom import *
and using CustomApplication() classname
'''

if __name__ == "__main__" and \
  sys.platform == "linux":
    main_app = MainApplication()
    main_app.main()
