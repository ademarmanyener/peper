#!/usr/bin/env python3
import discord
from discord.ext import commands
from __token import token # __token.py - token variable
import __user_info as user_info # __user_info.py - any username variable
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

app_id = "peper"
app_title = "Peper the Helper"
prefix = "r->"
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

def print_m_text(message):
  print("\n\t>> " + message + "\n")

class MainApplication:

  ###################
  #   bot command
  ###################
  # !!!!!!!!!!!!!!!!
  # commands're not
  # working properly

  @bot.command()
  async def testlol(cxt): 
    await ctx.send("lol msg")

  ###################
  #   bot event 
  ###################

  @bot.event
  async def on_connect():
    print_b_text(app_title + " is connecting.")

  @bot.event
  async def on_disconnect():
    print_b_text(app_title + " is disconnecting.")

  @bot.event
  async def on_ready():
    print_b_text(app_title + " is ready. Logged in as: " + bot.user.name)

  @bot.event
  async def on_message(message):
    if message.content.startswith(prefix):
      if message.content.endswith("help"): await message.channel.send("later")
      if message.content.endswith("platform"): await message.channel.send(sys.platform)
      else: await message.channel.send("wtf is that command")
    else:
      print_m_text("(msg) [" + str(message.author) + "]: " + str(message.content))

  @bot.event
  async def on_typing(channel, user, when):
    print_m_text("somebody is typing")

  def main(self):
    bot.run(token)

if __name__ == "__main__" and \
  sys.platform == "linux":
    main_app = MainApplication()
    main_app.main()
