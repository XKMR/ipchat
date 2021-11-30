from typing import final
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
import random
from requests import get
import requests
from colorama import init
from termcolor import colored, cprint

init()

print(colored("""                                                                                                                                       
### ######   #####                          #####                                  #     #        #       #####
 #  #     # #     # #    #   ##   #####    #     # #      # ###### #    # #####    #     #       ##            #
 #  #     # #       #    #  #  #    #      #       #      # #      ##   #   #      #     #      # #            #
 #  ######  #       ###### #    #   #      #       #      # #####  # #  #   #      #     #        #          #
 #  #       #       #    # ######   #      #       #      # #      #  # #   #       #   #  ###    #   ###  #
 #  #       #     # #    # #    #   #      #     # #      # #      #   ##   #        # #   ###    #   ### #
### #        #####  #    # #    #   #       #####  ###### # ###### #    #   #         #    ###  ##### ### #######

Created By DomIsOffline#4762
Upgraded to V1.2 by darkHares#0001                                                                                         """, 'red', attrs=['bold']))

usrnmin = input("chose a username for yourself: ")

webhook_url = input("What webhook would you like to connect to?" + "\n")

webhookcheck = webhook_url.startswith("https://discord.com/api/webhooks/")

question = "y"
if webhookcheck == True:
    print("Webhook is correct format! Connecting...")
    question = "y"
    sleep(1.25)
    finalmessage = f"{usrnmin} has connected!\n\nGitHub project: `https://github.com/53z/ipchat`\nCreated By `DomIsOffline#4762`  -  `https://github.com/53z`\nUpgraded to `V1.2` by `darkHares#0001`  -  `https://github.com/XKMR`"
    webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
    response = webhook.execute()
    sleep(1.25)

else:
    input("Webhook not formatted correctly :(" + "\n" + "\n" + "Press enter to close...")
    finalmessage = f"{usrnmin} has disconnected!"
    webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
    response = webhook.execute()
    question = "n"
# Variables

while question == "y":
    message = input("Input your message: ")
    finalmessage = f"{usrnmin} said: {message}"
    if message == "/disconnect":
        finalmessage = f"{ip_address} has disconnected!"
        sleep(0.75)
        webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
        response = webhook.execute()
        quit()
    else:
        webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
        response = webhook.execute()
