#!/usr/bin/env python3
import os, sys

'''
dev-build.py
============
it's a script for make developers
ready to play with peper the helper
discord bot.
'''

class DevBuild:
  def main(self):
    check = input("did you create a virtualenv? ")
    if check.lower() == "y" or \
      check.lower() == "yes":
      os.system("pip install discord.py")
    else:
      print("maybe it's better for you to create a virtualenv first")

if __name__ == "__main__" and \
  sys.platform == "linux":
    dev_build = DevBuild()
    dev_build.main()
