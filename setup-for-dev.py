#!/usr/bin/env python3
import os, sys

'''
setup-for-dev.py
============
it's a script for make developers
ready to play with peper the helper
discord bot.
'''
install_discordpy = "pip install discord.py"

class DevBuild:
  def main(self):
    check = input("did you create a virtualenv? ")
    if check.lower() == "y" or \
      check.lower() == "yes":
      os.system(install_discordpy)
    else:
      check = input("do you want me to create a virtualenv? ")
      if check.lower == "y" or check.lower == "yes":
        os.system("virtualenv venv")
        os.system("source ./venv/bin/activate")
        os.system(install_discordpy)
      else:
        print("maybe it's better for you to create a virtualenv first")

if __name__ == "__main__" and \
  sys.platform == "linux":
    dev_build = DevBuild()
    dev_build.main()
