#!/usr/bin/env python3
import discord
from discord.ext import commands
import __token

bot = commands.Bot(command_prefix=">")

class MyClient(discord.Client):
  async def on_ready(self):
    print("logged as: " + self.user)

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content == "ping":
      await message.channel.send("pong")

client = MyClient()
client.run(__token.token)
