from sys import platform
from os import name
from tkinter import *
import csv
import datetime
import os.path
import time
import pyttsx3
import automationwin
import whatsappautowin
import whatsappautomac
import automationmac

filename = "meeting_records.csv"
converter = pyttsx3.init()

def _check_hrs(row):
    speak = 0
    while True:
        time.sleep(1)
        start_time = datetime.datetime.today()
        print(start_time.hour,":",start_time.minute)
        if row[3] == 0:
            if speak < 1 and f"{start_time.hour}:{start_time.minute}" == f"{row[2]-1}:59":
                converter.say(f"Your {row[1]} lecture is going to start in one minute. Get Ready !")
                converter.runAndWait()
                speak += 1

        else:
            if speak < 1 and f"{start_time.hour}:{start_time.minute}" == f"{row[2]}:{int(row[3])-1}":
                converter.say(f"Your {row[1]} lecture is going to start in one minute. Get Ready !")
                converter.runAndWait()
                speak += 1

        if f"{start_time.hour}:{start_time.minute}" == f"{row[2]}:{row[3]}":
            return True

def readingcsv():
        days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        with open(filename,'r',newline="") as filex:
            my_date = datetime.date.today().weekday()   
            f = csv.reader(filex)

            for row in f:
                if days[my_date] == row[0]:
                    if _check_hrs(row):
                      clicked(platform,rad.get(),row,name.get())
                        
                            

if os.path.isfile(filename):
    home2 = Tk()
    home2.title("Whatsapp and Meet Automation")
    home2.iconbitmap("D:\PYPBL\\viitsymbol.ico")
    home2.geometry("500x200")
    
    rad = IntVar()
    name = StringVar()

    def grpname():
        en = Entry(textvariable=name,width="30")
        en.grid(row=0,column=1)

    def clicked(platform,num,row,group):
        if platform == "win32":
            if num == 1:
                whatsappautowin.run_chrome(row[4],group)
            elif num == 2:
                automationwin.run_chrome(row[4])

        elif platform == "darwin":
            if num == 1:
                whatsappautomac.run_chrome(row[4],group)
            elif num == 2:
                automationmac.run_chrome(row[4])

    Radiobutton(home2,text = "Whatsapp Automation",fg = "green",cursor="hand2",relief=RAISED,variable=rad,value=1,command=grpname).grid(pady=10,padx=10,row=0,column=0)
    Radiobutton(home2,text = "Meet Automation",fg = "blue",cursor="hand2",relief=RAISED,variable=rad,value=2).grid(pady=20,row=1,column=0)
    sub = Button(home2,text="Submit",cursor="hand2",command=home2.destroy,width="19", height="2", bg="grey").grid(pady=10,row=2,column=0)
    mainloop()

    readingcsv()
    

else:

    home = Tk()
    
    home.geometry("1920x1080")
    home.title("Whatsapp and Meet Automation")
    home.iconbitmap("D:\PYPBL\\viitsymbol.ico")
    
    sub_f = [[],[],[],[],[],[],[]]

    hrs_f = [[],[],[],[],[],[],[]]

    mints_f = [[],[],[],[],[],[],[]]

    link_f = [[],[],[],[],[],[],[]]

    def sett():

        #final data is stored in below lists
        for i in range(7):

            if no_lec[i]!=0:

                for j in range(no_lec[i]):

                    sub_f[i].append(sub[i][j].get())

                    hrs_f[i].append(hrs[i][j].get())

                    mints_f[i].append(mints[i][j].get())

                    link_f[i].append(link[i][j].get())

    no_lec =["a","a","a","a","a","a","a"]

    sub = [[],[],[],[],[],[],[]]

    hrs = [[],[],[],[],[],[],[]]

    mints = [[],[],[],[],[],[],[]]

    link = [[],[],[],[],[],[],[]]

    def lectures():

        for i in range(7):

            no_lec[i] = int(lecs[i].get())

            if no_lec[i]!=0:

                for j in range(no_lec[i]):

                    sub[i].append("a")

                    hrs[i].append("a")

                    mints[i].append("a")

                    link[i].append("a")

        t = 15

        for i in range(7):

            if no_lec[i] !=0:

                d = Label(home, text = days[i])

                d.place(x = "215",y = t)

                for j in range(no_lec[i]):

                    sub[i][j] = StringVar()

                    hrs[i][j] = StringVar()

                    mints[i][j] = StringVar()

                    link[i][j] = StringVar()

                    ls = Label(text= "Subject")

                    ls.place(x = "380",y = t)

                    es = Entry(textvariable=sub[i][j],width='10')

                    es.place(x = "450", y = t)

                    lt = Label(text="Hour")

                    lt.place(x = "600", y =t)

                    et = Entry(textvariable=hrs[i][j],width='10')

                    et.place(x = "650", y = t)

                    lx = Label(text="Minutes")

                    lx.place(x = "780", y =t)

                    ex = Entry(textvariable=mints[i][j],width='10')

                    ex.place(x = "850", y = t)

                    ll = Label(text="Link")

                    ll.place(x = "1000", y =t)

                    el = Entry(textvariable=link[i][j],width='10')

                    el.place(x = "1050", y = t)

                    t  += 20

            t+= 10

        button1 = Button(home, text="Submit",cursor="hand2",command=lambda : [sett(),home.destroy()],width="19", height="2", bg="grey")

        button1.place(x = "450", y = t+20)

    a = 0
    g = 15

    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    lecs =["a","a","a","a","a","a","a"]

    for d in days:

        day = Label(text =d)

        day.place(x="10",y = g)

        lecs[a] = StringVar()

        lec = Entry(textvariable=lecs[a],width='10')

        lec.place(x = "100",y = g)

        g += 30

        a += 1

    button = Button(home, text="Submit",cursor="hand2",command=lectures,width="19", height="2", bg="grey")

    button.place(x = "50", y ="500")
    
    rad = IntVar()

    def clicked(platform,num,row,group):
        if platform == "win32":
            if num == 1:
                whatsappautowin.run_chrome(row[4],group)
            elif num == 2:
                automationwin.run_chrome(row[4])

        elif platform == "darwin":
            if num == 1:
                whatsappautomac.run_chrome(row[4],group)
            elif num == 2:
                automationmac.run_chrome(row[4])

    name = StringVar()
    def grpname():
        en = Entry(textvariable=name,width="50")
        en.place(x="50",y="325")

    Radiobutton(home,text = "Whatsapp Automation",fg = "green",cursor="hand2",relief=RAISED,variable=rad,value=1,command=grpname).place(x="50",y="280")
    Radiobutton(home,text = "Meet Automation",fg = "blue",cursor="hand2",relief=RAISED,variable=rad,value=2).place(x="50",y="370")

    mainloop()

    with open(filename,"w",newline="") as filex:
            f = csv.writer(filex)
            for i in range(7):
                for j in range(no_lec[i]):
                    f.writerow([days[i],sub_f[i][j],hrs_f[i][j],mints_f[i][j],link_f[i][j]])

    readingcsv()