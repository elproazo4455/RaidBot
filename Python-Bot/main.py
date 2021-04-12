import sys
from colorama import Fore, Style

print(Fore.BLUE + "This project is only for education.")
print(Fore.BLUE + "I am not the responsible person of")
print(Fore.BLUE + "the bad use of this bot\n")

print(Fore.GREEN + "Do you want to turn on the bot?")

i = input(Fore.YELLOW + "(Y/N): ").lower()
if i == "y":
    print("Starting Bot...")
elif i == "n":
    print(Style.RESET_ALL)
    print(Fore.WHITE + "I'm not turning on :(")
    sys.exit(0)
else:
    print(Style.RESET_ALL)
    sys.exit(0)

import json
import discord

with open("config.json", "r") as d:
    data = d.read()

data = json.loads(data)
token = data["TOKEN"]
invite = data["INVITE"]
banMsg = data["banMSG"]
trigger = data["triggerCMD"]

client = discord.Client()
print("\n")

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.streaming , name = trigger + " For help")
    await client.change_presence(status=discord.Status.do_not_disturb , activity=activity)
    print(Fore.GREEN + "[BOT]" + " " + Fore.YELLOW + f"LOGGED IN: {client.user}")
    print(Fore.GREEN + "[BOT]" + " " + Fore.CYAN + "I'm Ready!\n")

print(Style.RESET_ALL)
print(Fore.GREEN + f"[BOT] INVITE: {invite}\n")
print(Fore.GREEN + "[BOT]" + " " + Fore.YELLOW + f"BAN_MSG: {banMsg}")
print(Fore.GREEN + "[BOT]" + " " + Fore.YELLOW + f"TRIGGER: {trigger}")

@client.event
async def on_message(message):
  if message.author == client.user:
        return
  
  if(message.content == trigger):
    print(Fore.GREEN + "[BOT]" + " " + Fore.BLUE + f"{message.author}" +  " " + Fore.YELLOW + "HAS STARTED A RAID")

client.run(token)