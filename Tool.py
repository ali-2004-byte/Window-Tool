from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import random
import tkinter as tk
from tkinter import filedialog
import platform
import psutil
#brightness
import screen_brightness_control as pct
#audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
#clock
from time import strftime
#calender
from tkcalendar import *
#open google
import pyautogui
import subprocess
import webbrowser as wb
import random

#Main window
root = Tk()
root.title("Software Tool for Windows")
root.geometry('850x500+300+170')
root.configure(bg='#000000')
root.resizable(True, True)

def weather():
    APP1=Toplevel()
    APP1.title("Weather")
    APP1.geometry('850x500+300+170')
    APP1.configure(bg='#f4f5f5')
    APP1.resizable(True,True)

    APP1_icon = PhotoImage(file='App1.png')
    APP1.iconphoto(False,APP1_icon)

    def getWeather():
        try:
            city=textfield.get()
            geolocator=Nominatim(user_agent="geoapiExercises")
            location=geolocator.geocode(city)
            obj=TimezoneFinder()
            result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
            home=pytz.timezone(result)
            localtime=datetime.now(home)
            currenttime=localtime.strftime("%I: %M %p")
            clock.config(text=currenttime)
            name.config(text="CURRENT WEATHER")
            api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
            json_data=requests.get(api).json()
            condition=json_data['weather'][0]['main']
            description=json_data['weather'][0]['description']
            temp=int(json_data['main']['temp']-273.15)
            pressure=json_data['main']['pressure']
            humidity=json_data['main']['humidity']
            wind=json_data['wind']['speed']
            t.config(text=(temp,"°"))
            c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)

        except Exception as e:
            print(e)
            messagebox.showerror("Weather App","Invalid Entry")


    search_image=PhotoImage(file='search.png')
    myimage=Label(APP1, image=search_image,bg='#f4f5f5')
    myimage.place(x=20,y=20)

    textfield=tk.Entry(APP1,justify='center', width=17,font=('Baskerville',25,'bold'),bg='#404040',border=0, fg='white')
    textfield.place(x=50,y=40)
    textfield.focus()

    search_icon=PhotoImage(file='search_icon.png')
    myimage_icon=Button(APP1, image=search_icon, borderwidth=0, cursor='hand2', bg='#404040',command=getWeather)
    myimage_icon.place(x=400,y=34)

    logo_image=PhotoImage(file='logo.png')
    logo=Label(APP1,image=logo_image,bg='#f4f5f5')
    logo.place(x=150,y=100)

    Frame_image=PhotoImage(file='box.png')
    frame_myimage=Label(APP1, image=Frame_image,bg='#f4f5f5')
    frame_myimage.pack(padx=5,pady=5, side=BOTTOM)

    name=Label(APP1,font=("Baskerville",15,'bold'),bg='#f4f5f5')
    name.place(x=30,y=100)
    clock=Label(APP1, font=("Baskerville",20),bg='#f4f5f5')
    clock.place(x=30,y=130)

    label1 = Label(APP1, text='WIND', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    label1.place(x=120,y=400)
    label2 = Label(APP1, text='Humidity', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    label2.place(x=250,y=400)
    label3 = Label(APP1, text='Description', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    label3.place(x=430,y=400)
    label4 = Label(APP1, text='Pressure', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    label4.place(x=650,y=400)

    t=Label(APP1,font=("Baskerville",70,"bold"),fg="#ee666d",bg="#f4f5f5")
    t.place(x=400,y=150)
    c=Label(APP1,font=("Baskerville",20,"bold"),bg="#f4f5f5")
    c.place(x=400,y=250)


    w = Label(APP1, text='...', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    w.place(x=120,y=430)
    h = Label(APP1, text='...', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    h.place(x=250,y=430)
    d = Label(APP1, text='...', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    d.place(x=430,y=430)
    p = Label(APP1, text='...', font=("Baskerville", 15, 'bold'), fg='white', bg='#1ab5ef')
    p.place(x=650,y=430)


    APP1.mainloop()

def clock():
    APP2=Toplevel()
    APP2.title("Clock")
    APP2.geometry("800x110+300+10")
    APP2.configure(bg="#38b6ff")
    APP2.resizable(True,True)

    image_icon=PhotoImage(file='App2.png')
    APP2.iconphoto(False,image_icon)
    def clock():
        text=strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000,clock)
    lbl=Label(APP2,font=("digital-7",50,"bold"),width=20,bg='#f4f5f5',fg='#38b6ff')
    lbl.pack(anchor='center',pady=20)
    clock()
    

    APP2.mainloop()

def calendar():
    APP3=Toplevel()
    APP3.title("Calendar")
    APP3.geometry("300x300+10+10")
    APP3.configure(bg="#292e2e")
    APP3.resizable(True,True)

    image_icon=PhotoImage(file="App3.png")
    APP3.iconphoto(False,image_icon)

    mycal=Calendar(APP3, setmode='day',date_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)

    APP3.mainloop()

def game():
    APP5=Toplevel()
    APP5.geometry("300x500+1170+170")
    APP5.title("Ludo")
    APP5.configure(bg="#dee2e5")
    APP5.resizable(True,True)
    image_icon=PhotoImage(file="App5.png")
    APP5.iconphoto(False,image_icon)

    ludo_image=PhotoImage(file="ludo back.png")
    Label(APP5,image=ludo_image).pack()

    label=Label(APP5,text=' ',font=("times",150))
    def roll():
        dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
        label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
        label.pack()

    btn_image=PhotoImage(file="ludo button.png")
    btn=Button(APP5,image=btn_image,bg="#dee2e5",command=roll)
    btn.pack(padx=10,pady=10)

    APP5.mainloop()

def screenshot():
    root.iconify()
    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

def file():
    subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
def chrome():
    wb.register('chrome',None)
    wb.open('https://www.google.com/')

def git():
    wb.register('github',None)
    wb.open('https://github.com/ali-2004-byte')
def closewindow():
    root.destroy()
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)
body = Frame(root, width=810, height= 460, bg="#38b6ff")
body.place(x=20,y=20)
#------------------------------------------------------------------------------------------------
lhs=Frame(body, width=310, height=440, bg="#ffffff")
lhs.place(x=10,y=10)
logo=PhotoImage(file="laptop.png")
Logo=Label(lhs,image=logo,background="#ffffff")
Logo.place(x=2,y=20)
title_tool=Label(lhs, text="NeuralLink Solutions", fg="#000000",bg="#ffffff",font=("Baskerville",20,'bold'))
title_tool.place(x=15,y=210)
my_system=platform.uname()
l1=Label(lhs,text=f"System:{my_system.system}",fg="#000000",bg="#ffffff",font=("Baskerville",10,"bold"))
l1.place(x=15,y=270)
l2=Label(lhs,text=f"Version:{my_system.version}",fg="#000000",bg="#ffffff",font=("Baskerville",10,"bold"))
l2.place(x=15,y=295)
l3=Label(lhs,text=f"Machine:{my_system.machine}",fg="#000000",bg="#ffffff",font=("Baskerville",10,"bold"))
l3.place(x=15,y=320)
l4=Label(lhs,text=f"Processor:{my_system.processor}",fg="#000000",bg="#ffffff",font=("Baskerville",7,"bold"))
l4.place(x=15,y=345)
l5=Label(lhs,text=f"Release:{my_system.release}",fg="#000000",bg="#ffffff",font=("Baskerville",10,"bold"))
l5.place(x=15,y=370)
l6=Label(lhs,text=f"Total RAM installed:{round(psutil.virtual_memory().total/1000000000,2)} GB",fg="#000000",bg="#ffffff",font=("Baskerville",10,"bold"))
l6.place(x=15,y=395)

##################MODE#####################
button_mode=True
def mode():
    global button_mode
    if button_mode:
        lhs.config(bg="#292e2e")
        Logo.config(bg="#292e2e")
        l1.config(bg="#292e2e",fg="#d6d6d6")
        l2.config(bg="#292e2e",fg="#d6d6d6")
        l3.config(bg="#292e2e",fg="#d6d6d6")
        l4.config(bg="#292e2e",fg="#d6d6d6")
        l5.config(bg="#292e2e",fg="#d6d6d6")
        l6.config(bg="#292e2e",fg="#d6d6d6")

        rdo.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        Apps.config(bg="#292e2e",fg="#d6d6d6")
        button_mode=False

    else:
        lhs.config(bg="#ffffff")
        Logo.config(bg="#ffffff")
        l1.config(bg="#ffffff",fg="#000000")
        l2.config(bg="#ffffff",fg="#000000")
        l3.config(bg="#ffffff",fg="#000000")
        l4.config(bg="#ffffff",fg="#000000")
        l5.config(bg="#ffffff",fg="#000000")
        l6.config(bg="#ffffff",fg="#000000")
        rdo.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        app1.config(bg="#ffffff")
        Apps.config(bg="#ffffff",fg="#000000")
        button_mode=True

   


#------------------------------------------------------------------------------------------------
rup=Frame(body, width= 470, height=220, bg="#ffffff")
rup.place(x=330,y=10)
system=Label(rup,text="System",fg="#000000",bg="#ffffff",font=("Baskerville",20,'bold'))
system.place(x=10,y=10)
####Battery####
def none():
    global battery_png
    global battery_label
    battery=psutil.sensors_battery()
    percent = battery.percent
    
    lbl.config(text=f"{percent}%")
    lbl_plug.config(text=f"Plug in: {str(battery.power_plugged)}")

    battery_label=Label(rup,bg="#ffffff")
    battery_label.place(x=15,y=50)

    lbl.after(1000,none)
    if battery.power_plugged == False:
        battery_png=PhotoImage(file="battery.png")
        battery_label.config(image=battery_png)
        lbl_plug.config(text=f"Plug in: NO!")

    else:
        battery_png=PhotoImage(file="charging.png")
        battery_label.config(image=battery_png)
        lbl_plug.config(text=f"Plug in: YES!")


lbl=Label(rup,font=("Baskerville",40,"bold"),bg="#ffffff")
lbl.place(x=200,y=40)
lbl_plug=Label(rup,font=("Baskerville",10),bg="#ffffff")
lbl_plug.place(x=20,y=100)

none()

####Speaker####

def current_volume():
    return '{: .2f}'.format(volume_value.get())
def volume_changed(event):
    device=AudioUtilities.GetSpeakers()
    interface=device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume=cast(interface,POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-float(current_volume()),None)

style=ttk.Style()
style.configure("TScale",bg="#ffffff")
lbl_speaker=Label(rup,text="Speaker: ", bg="#ffffff", font=("Baskerville",10,"bold"))
lbl_speaker.place(x=10,y=150)
volume_value=tk.DoubleVar()
volume=ttk.Scale(rup,from_=60,to=0,orient='horizontal',command=volume_changed,variable=volume_value)
volume.place(x=90,y=150)
volume.set(0)

####Brightness####
def current_brightness():
    return '{: .2f}'.format(brightness_value.get())
def brightness_changed(event):
    pct.set_brightness(current_brightness())
lbl_bright=Label(rup,text="Brightness: ",bg="#ffffff",font=("Baskerville",10,"bold"))
lbl_bright.place(x=10,y=190)
brightness_value=tk.DoubleVar()
brightiness=ttk.Scale(rup,from_=0,to=100, orient='horizontal',command=brightness_changed,variable=brightness_value)
brightiness.place(x=90,y=190)
brightiness.set(100)
#------------------------------------------------------------------------------------------------
rdo=Frame(body, width=470,height=210, bg="#ffffff")
rdo.place(x=330,y=240)
Apps=Label(rdo,text="Apps",fg="#000000",bg="#ffffff",font=("Baskerville",20,'bold'))
Apps.place(x=10,y=10)
app1_image=PhotoImage(file="App1.png")
app1=Button(rdo,image=app1_image,bd=0,command=weather)
app1.place(x=15,y=50)

app2_image=PhotoImage(file="App2.png")
app2=Button(rdo,image=app2_image,bd=0,command=clock)
app2.place(x=110,y=50)

app3_image=PhotoImage(file="App3.png")
app3=Button(rdo,image=app3_image,bd=0, command=calendar)
app3.place(x=205,y=50)

app4_image=PhotoImage(file="App4.png")
app4=Button(rdo,image=app4_image,bd=0,command=mode)
app4.place(x=300,y=50)

app5_image=PhotoImage(file="App5.png")
app5=Button(rdo,image=app5_image,bd=0,command=game)
app5.place(x=395,y=50)

app6_image=PhotoImage(file="App6.png")
app6=Button(rdo,image=app6_image,bd=0,command=screenshot)
app6.place(x=15,y=150)

app7_image=PhotoImage(file="App7.png")
app7=Button(rdo,image=app7_image,bd=0,command=file)
app7.place(x=110,y=150)

app8_image=PhotoImage(file="App8.png")
app8=Button(rdo,image=app8_image,bd=0,command=chrome)
app8.place(x=205,y=150)

app9_image=PhotoImage(file="App^9.png")
app9=Button(rdo,image=app9_image,bd=0,command=git)
app9.place(x=300,y=150)

app10_image=PhotoImage(file="App10.png")
app10=Button(rdo,image=app10_image,bd=0,command=closewindow)
app10.place(x=395,y=150)
root.mainloop()


