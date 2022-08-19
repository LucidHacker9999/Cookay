
import random, string;from pystyle import *
def Main2():
    logo = """
▀▀█▀▀ █▀▀█ █░█ █▀▀ █▀▀▄    ▒█▀▀█ █▀▀ █▀▀▄ 
░▒█░░ █░░█ █▀▄ █▀▀ █░░█    ▒█░▄▄ █▀▀ █░░█ 
░▒█░░ ▀▀▀▀ ▀░▀ ▀▀▀ ▀░░▀    ▒█▄▄█ ▀▀▀ ▀░░▀ 
"""
    def gen():
        while True:
            a = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
            b = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(6))
            c = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(38))
            tok = a+"."+b+"."+c
            print(f"{Col.white}[{Col.red}+{Col.white}]{Col.white} GENERATED : {tok} {Col.red}(INVALID)")
    def main():
        print(f"""{Col.orange}
{logo}

{Col.white}[{Col.orange}+{Col.white}] Fastest Discord Token Generator + Checker (With Proxies)
{Col.white}[{Col.orange}+{Col.white}] Press Enter To Start Generating..

    """)
        input()
        gen()
    main()
