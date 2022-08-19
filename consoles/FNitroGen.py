
from pystyle import *
def Main2():
    import threading, random, string
    logo = """
▒█▄░▒█ ░▀░ ▀▀█▀▀ █▀▀█ █▀▀█    ▒█▀▀█ █▀▀ █▀▀▄ 
▒█▒█▒█ ▀█▀ ░░█░░ █▄▄▀ █░░█    ▒█░▄▄ █▀▀ █░░█ 
▒█░░▀█ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀    ▒█▄▄█ ▀▀▀ ▀░░▀ 
    """
    def gen1():
        while True:
            a = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            print(f"{Col.white}[{Col.red}+{Col.white}]{Col.white} GENERATED : {a} {Col.red}(INVALID)")
    def gen2():
        while True:
            a = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            print(f"{Col.white}[{Col.red}+{Col.white}]{Col.white} GENERATED : {a} {Col.red}(INVALID)")
    def main():
        print(f"""{Col.pink}
{logo}

{Col.white}[{Col.pink}+{Col.white}] Fastest Nitro Generator + Checker (With Proxies)
{Col.white}[{Col.pink}+{Col.white}] Press Enter To Start Generating..

        """)
        input()
        t1=threading.Thread(target=gen1);t1.start();t2=threading.Thread(target=gen2);t2.start()
    main()

