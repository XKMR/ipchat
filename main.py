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
### ######   #####                          #####                                  #     #        #   
 #  #     # #     # #    #   ##   #####    #     # #      # ###### #    # #####    #     #       ##   
 #  #     # #       #    #  #  #    #      #       #      # #      ##   #   #      #     #      # #   
 #  ######  #       ###### #    #   #      #       #      # #####  # #  #   #      #     #        #   
 #  #       #       #    # ######   #      #       #      # #      #  # #   #       #   #  ###    #   
 #  #       #     # #    # #    #   #      #     # #      # #      #   ##   #        # #   ###    #   
### #        #####  #    # #    #   #       #####  ###### # ###### #    #   #         #    ###  ##### 

Created By DomIsOffline#4762
                                                                                         """, 'red', attrs=['bold']))

ip_address = get('https://api.ipify.org').text

webhook_url = "https://discord.com/api/webhooks/847428501262827541/zjPkcYx1ovtz-IIN0mMpLtoFzbKD7wHKjW53sn1esW9sXaJ5Jc5bOGjv4KlZY9opAo3_"
webhook_url = input("What webhook would you like to connect to?" + "\n")

webhookcheck = webhook_url.startswith("https://discord.com/api/webhooks/")

question = "y"
if webhookcheck == True:
    print("Webhook is correct format! Connecting...")
    question = "y"
    sleep(1.25)
    finalmessage = f"{ip_address} has connected!"
    webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
    response = webhook.execute()
    sleep(1.25)

else:
    input("Webhook not formatted correctly :(" + "\n" + "\n" + "Press enter to close...")
    finalmessage = f"{ip_address} has disconnected!"
    webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
    response = webhook.execute()
    question = "n"
# Variables

while question == "y":
    message = input("Input your message: ")
    finalmessage = f"{ip_address} said: {message}"
    if message == "/disconnect":
        finalmessage = f"{ip_address} has disconnected!"
        sleep(0.75)
        webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
        response = webhook.execute()
        quit()
    else:
        webhook = DiscordWebhook(url=webhook_url, content=finalmessage)
        response = webhook.execute()