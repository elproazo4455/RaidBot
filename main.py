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
    sys.exit(0)
else:
    print(Style.RESET_ALL)
    sys.exit(0)

import json
import discord

with open("config.json", "r") as d:
    data = d.read()
