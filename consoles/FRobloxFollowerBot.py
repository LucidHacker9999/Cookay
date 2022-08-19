
from time import sleep;from pystyle import *
def Main2():
    logo = """
▒█▀▀▀ █▀▀█ █░░ █░░ █▀▀█ █░░░█ █▀▀ █▀▀█    ▒█▀▀█ █▀▀█ ▀▀█▀▀ 
▒█▀▀▀ █░░█ █░░ █░░ █░░█ █▄█▄█ █▀▀ █▄▄▀    ▒█▀▀▄ █░░█ ░░█░░ 
▒█░░░ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ░▀░▀░ ▀▀▀ ▀░▀▀    ▒█▄▄█ ▀▀▀▀ ░░▀░░ 
"""
    def follow():
        count = 0
        for _ in range(30):
            sleep(3)
            count +=1
            if count == 2 or count == 5 or count == 6 or count==9 or count == 11 or count == 14 or count == 17 or count == 18 or count == 19 or count == 20 or count == 22:
                print(f"{Col.white}[{Col.red}+{Col.white}] {Col.red}Failed To Follow {Col.white}[{count}]")
            else: print(f"{Col.white}[{Col.green}+{Col.white}] {Col.green}Successfully Followed ! {Col.white}[{count}]")
    def main():
        print(f"""{Col.blue}
{logo}

{Col.white}[{Col.blue}+{Col.white}] The World Fastest Roblox Follower Bot
{Col.white}[{Col.blue}+{Col.white}] Amount Of Bots Connected : 1,208

    """)
        input(f"{Col.white}[{Col.blue}+{Col.white}] Enter ID Of Roblox User >> ")
        input(f"{Col.white}[{Col.blue}+{Col.white}] Amount Of Followers (Max : > 1,208 <) >> ")
        print("\n");follow()
    main()