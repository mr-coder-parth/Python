import tkinter as tk
import wikipedia as database_server_Py
import pyttsx3 as tt
import fitz
import tkdocviewer
from tkinter import ttk
import pygame as p
from tkinter import filedialog
from pygame import *
import PIL
from PIL import ImageTk,Image
from pdf2image import convert_from_path
import image
from pygame import mixer
from tkinter import Frame
from tkinter import Menu
from google_images_download import google_images_download as d
from tkinter import messagebox
import music_data
import datetime
import time
import socket
import clock
from string import *
from tkinter import*
import sys
import threading
from threading import *
import os
import webbrowser as WB
def full_Jarvis_Program():
    path=('C:\\Users\\Monal\\Desktop\\kickstart\\')
    path1=('C:\\Users\\Monal\\Desktop\\kickstart\\Images')
    png=(".png")
    def music_PARTY():
        mixer.init()
        mixer.music.load('C:\\Users\\Monal\\Desktop\\kickstart\\mashup.mp3')
        mixer.music.set_volume(5)
        mixer.music.play(-1)
    def music_pause():
        mixer.init()
        mixer.music.pause()
    def music_resume():
        mixer.init()
        mixer.music.unpause()
    ivory='ivory'
    black='black'
    white='white'
    red='red'
    orange='orange'
    yellow='yellow'
    blue='blue'
    lightblue='light blue'
    navyblue='navy blue'
    deepskyblue2='deepskyblue2'
    app=tk.Toplevel()
    app.state('zoomed')
    app.title('JARVIS WORLD!-BY PARTH SANTOSH KARBA')
    app.iconbitmap(path+'images.ico')
    app.config(width=950,height=600)
    app.configure(bg=black)
    img=tk.PhotoImage(file=path+'c.png', width=900, height=1000)
    l_img=tk.Label(app, image=img, border=0)
    l_img.place(x=500)
    sanchit=tk.PhotoImage(file=path+'Presentation1.png', width=800)
    label=tk.Label(app, image=sanchit, border=0)
    label.pack(side=tk.LEFT)
    user=tk.Entry(app, width=53, bg=ivory, border=0, font=(
    'Agency FB',20))
    user.place(x=800,y=630) 
    mobile= tk.PhotoImage(file=path+'TABLET.png')
    mobile_label=tk.Label(app, image=mobile, border=0 ,bg=None, width=400,height=550)
    mobile_label.place(x=890,y=50)
    Image_Open_Path=('C:\\Users\\Monal\\Desktop\\kickstart\\Jarvis Work\\Images'+(user.get())+(user.get()))
    def music_screen():
        win=tk.Toplevel()
        speak('Sir i am playing songs, if you want to pause song press middle button, or if you want to resume press right hand button and if you press left hand button songs will start from the beginning')
        music_PARTY()
        win.iconbitmap(path+'music.ico')
        win.config(width=700, height=850)
        win.state('zoomed')
        bg1=tk.PhotoImage(file='C:\\Users\\Monal\\Desktop\\kickstart\\c.png')
        label3= tk.Label(win, image=bg1, border=0, bg=None)
        label3.place(x=600)
        b1g=tk.PhotoImage(file='C:\\Users\\Monal\\Desktop\\kickstart\\c.png')
        label2= tk.Label(win, image=b1g, border=0, bg=None)
        label2.place(x=0)
        bg=tk.PhotoImage(file='C:\\Users\\Monal\\Desktop\\kickstart\\dj.png')
        label1= tk.Label(win,image=bg, border=0, bg=None)
        label1.pack()
        win.configure(bg='orange')
        win.title('Music Settings')
        play_song= tk.PhotoImage(file=path+'play.png')
        gautam= tk.Button(win, width=100, height=100,bd=0,image=play_song,command=music_PARTY,border=0)
        gautam.place(x=400)
        pause_song= tk.PhotoImage(file=path+'pause2.png')
        shital= tk.Button(win,image=pause_song, width=95, height=100, command=music_pause, border=0)
        shital.place(x=600)
        stop_song= tk.PhotoImage(file=path+'stop2.png')
        santosh= tk.Button(win,image=stop_song, width=95, height=95, command=music_resume, border=0)
        santosh.place(x=800)
        win.mainloop() 
    def speak(str):
        engine=tts.init()
        engine.say(str)
        engine.runAndWait()
    btn1=tk.Button(app, width=10,bg='red', height=1,cursor='star', border=0, text='Play Songs!',command=music_screen,font=(
    'Arial',10))
    btn1.place(x=1290) 
    img1x=tk.PhotoImage(file='C:\\Users\\Monal\\Desktop\\kickstart\\parthkabra.png')
    label= tk.Label(app, image=img1x,border=0,width=500).place(x=0)
    def is_connected():
        try:
            socket.create_connection(("1.1.1.1", 53))
            messagebox.showinfo('"Hello" from Internet World!', 'Successfully connected to the virtual world! Press OK and start, we cannot wait for our star to connect with us!!')
        except OSError:
            run=True
            while run:
                messagebox.showwarning('Virtual connection lost!','Sir your virtual connection is lost. Please do check internet, otherwise you will not be able to enjoy the functions of Jarvis!')
                pass
    is_connected()
    def time_TIME():
        hr=(datetime.datetime.now().hour)
        morning=('good morning parth i am jarvis, how may i help u?')
        if hr==1:
            speak(morning)
        elif hr==2:
            speak(morning)
        elif hr==3:
            speak(morning)
        elif hr==4:
            speak(morning)
        elif hr==5:
            speak(morning)
        elif hr==6:
            speak(morning)
        elif hr==7:
            speak(morning)
        elif hr==8:
            speak(morning)
        elif hr==9:
            speak(morning)
        elif hr==10:
            speak(morning)
        elif hr==11:
            speak(morning)
        afternoon=('good afternoon parth i am jarvis, how may i help u?')
        if hr==12:
            speak(afternoon)
        elif hr==13:
            speak(afternoon)
        elif hr==14:
            speak(afternoon)
        elif hr==15:
            speak(afternoon)
        elif hr==16:
            speak(afternoon)
        elif hr==17:
            speak(afternoon)
        evening=('good evening parth i am jarvis, how may i help u?')
        if hr==18:
            speak(evening)
        elif hr==19:
            speak(evening)
        elif hr==20:
            speak(evening)
        elif hr==21:
            speak(evening)
        elif hr==22:
            speak(evening)
        elif hr==23:
            speak(evening)
        elif hr==24:
            speak(morning)
    def exit_():
        sys.exit()
    def search():
        hr=(datetime.datetime.now().hour)
        music_pause()
        def get():
            dir_img = ('C:\\Users\\Monal\\Desktop\\kickstart\\Jarvis Work\\Images\\')
            response = d.googleimagesdownload()
            arguments = {
            "keywords": str(user.get()),
            "limit": int(1),
            "print_urls": True,
            "output_directory": dir_img
            }
            try:
                path = response.download(arguments)
                messagebox.showinfo("Download Status!.","Your image image is downloaded, to find your image go to "+path1+".You may find a folder name of your file. Click on it and view your image!  THANKS")
                print(path)
            except Exception as e:
                messagebox.showerror("Download Status!", "Oops! Something went wrong. Please do check your WIFI connection and try again. THANKS")
        def install():

            thread = Thread(target=get)
            thread.start()
        install()
        day=('okk, hope we had a marvellous time together')
        if (user.get()=='bye jarvis'):
            speak(day)
            exit_()
        elif (user.get()=='bye'):
            speak(day)
            exit_()
        elif(user.get()=='what can you do'):
            speak('i can give information on a large scale. This is my original work')
        elif(user.get()=='who made you'):
            speak('my master, parth santosh kabra made me, and his father mister, santosh kabra named me as Jarvis')
        ans=('hello master')
        if(user.get()=='hi'):
            speak(ans)
        elif(user.get()=='hello'):
            speak(ans)
        elif(user.get()=='hey there'):
            speak(ans)
        elif(user.get()=='hey'):
            speak(ans)
        elif (user.get()=='how are you'):
            speak('i am fine')
        result=(database_server_Py.summary((user.get()),sentences=1))
        if(result==None):
            speak('sorry sir. i could not help u in this case. i dont have any result for this. is there anything else i can help u with?')
        speak(result)
        def Folder_Open():
            WB.open(Image_Open_Path)
            speak('sir select folder which is named by your search and open it. You will be able to see a image of your search.')
        Folder_Open()
    time_TIME()
    b=tk.Button(app, width=53,height=1, text='Ask Jarvis!',cursor='star',border=0,bg=yellow,command=search,font=(
    'Arial',15))
    b.place(x=800, y=663)
    app.mainloop()
win=tk.Tk()
def CONNECTION():
    def is_connected():
        try:
            socket.create_connection(("1.1.1.1", 53))
            messagebox.showinfo('"Hello" from Internet World!','Connected to the virtual world successfully! Please stay connected to wifi to excperiece better')
        except OSError:
            run=True
            while run:
                messagebox.showwarning('Virtual connection lost!','Sir your virtual connection is lost. Please do check internet, otherwise you will not be able to enjoy the functions of Jarvis and EduBot!!')
                pass
    is_connected()
CONNECTION()
pathx=('C:\\Users\\Monal\\Desktop\\')
pathy=('C:\\Users\\Monal\\Desktop\\kickstart\\')
win.configure(bg='light blue')
win.config(width=950, height=600)
win.title('Hey Parth!- My personal eduBot')
win.state('zoomed')
board=tk.PhotoImage(file=pathy+'gautam.png')
board1=tk.Label(win, image=board, border=0).place(x=0,y=14)
board2=tk.PhotoImage(file=pathy+'bo9.png')
board21=tk.Label(win, image=board2, border=0).place(x=900,y=14)
que=StringVar()
que.set("Enter your subject name and grade only in lower cast. Eg: hindi 7")
user_ask=tk.Entry(win,textvariable=que, width=100, bg='yellow',font=('Comic Sans MS',15),border=0).place(x=0)


def e_book_open():
    notebook_open_TXT= filedialog.askopenfile()
def notepad_book():
    os.system(r'%windir%\system32\notepad.exe')
def EXIT():
    sys.exit()
def python_book():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\beyond school syllabus\\py.pdf')
def java_book():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\beyond school syllabus\\java.pdf')
def js_book():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\beyond school syllabus\\js.pdf')
def c_book():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\beyond school syllabus\\c.pdf')
def go_book():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\beyond school syllabus\\go.pdf')
def html_css_book():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\beyond school syllabus\\html css.pdf')
menubar = Menu(win)
win.config(menu=menubar)
filemenu = Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open eNoteBook',command=e_book_open)
filemenu.add_command(label='Create a eNoteBook',command=notepad_book)
filemenu.add_separator()
filemenu.add_command(label='Have a doubt? Ask Jarvis for help!',command=full_Jarvis_Program)
filemenu.add_separator()
filemenu.add_command(label='Exit!',command=EXIT)
filemenu2 = Menu(menubar)
menubar.add_cascade(label='Beyond School Syllabus', menu=filemenu2)
filemenu2.add_command(label='''
Python Pogramming''',command=python_book)
filemenu2.add_command(label='''
Java Pogramming''',command=java_book)
filemenu2.add_command(label='''
Javascript Pogramming''',command=js_book)
filemenu2.add_command(label='''
HTML & CSS Pogramming''',command=html_css_book)
filemenu2.add_command(label='''
C Pogramming''',command=c_book)
filemenu2.add_command(label='''
GO Pogramming''',command=go_book)
def paper_craft():
    WB.open('The Complete Photo Guide to Paper Crafts_ _All You Need to Know to Craft with Paper _ The Essential Reference for Novice and Expert Paper Crafters _ ... Instructions for More Than 60 Projects ( PDFDrive ).pdf')
def origami():
    WB.open('Origami Ikebana_ Create Lifelike Paper Flower Arrangements_ Includes Origami Book with 38 Projects and Instructional DVD ( PDFDrive ).pdf')
filemenu3 = Menu(menubar)
menubar.add_cascade(label='Art & Craft!', menu=filemenu3)
filemenu3.add_command(label='''
Paper Craft''',command=paper_craft)
filemenu3.add_command(label='''
Origami''',command=origami)
def MG():
    WB.open('mg.pdf')
def SM():
    WB.open('sm.pdf')
def AK():
    WB.open('ak.pdf')
def BS():
    WB.open('bs.pdf')
def RLB():
    WB.open('rlb.pdf')
def SM1():
    WB.open('sm1.pdf')
def IN():
    WB.open('in.pdf')
filemenu4 = Menu(menubar)
menubar.add_cascade(label='AutoBiography', menu=filemenu4)
filemenu4.add_command(label='Mahatma Gandhi',command=MG)
filemenu4.add_command(label='Shivaji Maharaj',command=SM)
filemenu4.add_command(label='Dr.A.P.J Abdul Kalam',command=AK)
filemenu4.add_command(label='Sir Issac Newton',command=IN)
filemenu4.add_command(label='Bhagat Singh',command=BS)
filemenu4.add_command(label='Rani LaxmiBai',command=RLB)
filemenu4.add_command(label='Sambhaji Maharaj',command=SM1)
def BGH():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\Bhagavad Gita Hind.pdf')
def BGHM():
    WB.open('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\bhagavad gita meanings.pdf')
filemenu3 = Menu(menubar)
menubar.add_cascade(label='Holy Books', menu=filemenu3)
filemenu3.add_command(label='''
Bhagvat Geeta- Hindi''',command=BGH)
filemenu3.add_command(label='''
Bhagvat Geeta- Manings of some words in English''',command=BGHM)
import pyttsx3 as tts
def speak(str):
    engine=tts.init()
    engine.say(str)
    engine.runAndWait()
def grade():
    OB=('opening book')
    if (que.get()=='hindi 7'):
        speak(OB)
    if (que.get()=='marathi 7'):
        speak(OB)
    if (que.get()=='maths 7'):
        speak(OB)
    if (que.get()=='history 7'):
        speak(OB)
    if (que.get()=='civics 7'):
        speak(OB)
    if (que.get()=='geography 7'):
        speak(OB)
    if (que.get()=='ss 7'):
        speak(OB)
    if (que.get()=='value education 7'):
        speak(OB)
    if (que.get()=='science 7'):
        speak(OB)
    if (que.get()=='story book'):
        speak(OB)
    else:
        messagebox.showerror('ERROR', 'No such book available. Do check your spelling or do check the instruction!')
btn_class=tk.Button(win, width=26,height=1,bg='cyan', border=0,text='Search for book!',command=grade,font=('Comic Sans MS',10)).place(x=1200)



var=IntVar()
def class_1_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var)  
    menubutton.menu.add_checkbutton(label = 'Story Book-1', variable = var)  
    menubutton.menu.add_checkbutton(label = 'Story Book-2', variable = var)  
    menubutton.menu.add_checkbutton(label = "Picture Book", variable = var)  
    menubutton.place(x=0,y=170)

path2=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 2\\')
storybook=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\Story Book\\')
picbook=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\Picture Book\\')
def english2():
    WB.open(r'file:///C:/Users/Monal/Desktop/Pdf%20Viewer/Class%202/english.html')
def marathi2():
    WB.open(path2+'marathi.pdf')
def maths2():
    WB.open(path+'maths.pdf')
def story2():
    WB.open(storybook+'little-women.pdf')
def story_2():
    WB.open(storybook+'height.pdf')
def pic2():
    WB.open(picbook+'hide and seek.pdf')
def class_2_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english2)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi2)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var,command=maths2)  
    menubutton.menu.add_checkbutton(label = 'Story Book-1', variable = var,command=story2)  
    menubutton.menu.add_checkbutton(label = 'Story Book-2', variable = var,command=story_2)  
    menubutton.menu.add_checkbutton(label = "Picture Book", variable = var,command=pic2)  
    menubutton.place(x=0,y=302)

path3=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 3\\')
def evs3():
    WB.open(path3+'evs.pdf')
def english3():
    WB.open(path3+'english.pdf')
def marathi3():
    WB.open(path3+'marathi.pdf')
def maths3():
    WB.open(path3+'maths.pdf')
def story3():
    WB.open(storybook+'gullivers-travel.pdf')
def story_3():
    WB.open(storybook+'room with a view.pdf')
def pic3():
    WB.open(picbook+'tooth fairy.pdf')
def class_3_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english3)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "E.V.S", variable = var,command=evs3)  
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi3)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var,command=maths3)  
    menubutton.menu.add_checkbutton(label = 'Story Book-1', variable = var,command=story3)  
    menubutton.menu.add_checkbutton(label = 'Story Book-2', variable = var,command=story_3)  
    menubutton.menu.add_checkbutton(label = "Picture Book", variable = var,command=pic3)  
    menubutton.place(x=0,y=435)

path4=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 4\\')
def evs4():
    WB.open(path4+'evs.pdf')
def english4():
    WB.open(path4+'english.pdf')
def marathi4():
    WB.open(path4+'marathi.pdf')
def history4():
    WB.open(path4+'history.pdf')
def maths4():
    WB.open(path4+'maths.pdf')
def story4():
    WB.open(storybook+'art of war.pdf')
def story_4():
    WB.open(storybook+'the sea wolf.pdf')
def pic4():
    WB.open(picbook+'missing smile.pdf')
def class_4_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english4)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "E.V.S", variable = var,command=evs4)  
    menubutton.menu.add_checkbutton(label = "History", variable = var,command=history4) 
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi4)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var,command=maths4)  
    menubutton.menu.add_checkbutton(label = 'Story Book-1', variable = var,command=story4)  
    menubutton.menu.add_checkbutton(label = 'Story Book-2', variable = var,command=story_4)  
    menubutton.menu.add_checkbutton(label = "Picture Book", variable = var,command=pic4)  
    menubutton.place(x=0,y=569)

path5=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 5\\')
def hindi():
    WB.open(path5+'hindi.pdf')
def evs5():
    WB.open(path5+'evs.pdf')
def english5():
    WB.open(path5+'english.pdf')
def history5():
    WB.open(path5+'history.pdf')
def marathi5():
    WB.open(path5+'marathi.pdf')
def maths5():
    WB.open(path5+'maths.pdf')
def story5():
    WB.open(storybook+'sherlock homes.pdf')
def story_5():
    WB.open(storybook+'Time Machine.pdf')
def pic5():
    WB.open(picbook+'woodland school.pdf')
def class_5_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english5)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "Geography", variable = var)  
    menubutton.menu.add_checkbutton(label = "E.V.S", variable = var,command=evs5)  
    menubutton.menu.add_checkbutton(label = "History", variable = var,command=history5) 
    menubutton.menu.add_checkbutton(label = "Hindi", variable = var,command=hindi) 
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi5)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var,command=maths5)  
    menubutton.menu.add_checkbutton(label = 'Story Book-1', variable = var,command=story5)  
    menubutton.menu.add_checkbutton(label = 'Story Book-2', variable = var,command=story_5)  
    menubutton.menu.add_checkbutton(label = "Picture Book", variable = var,command=pic5)  
    menubutton.place(x=350,y=170)

path6=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 6\\')
def english6():
    WB.open(path6+'english.pdf')
def geo6():
    WB.open(path6+'geography.pdf')
def hindi6():
    WB.open(path6+'hindi.pdf')
def HS6():
    WB.open(path6+'history civics.pdf')
def marathi6():
    WB.open(path6+'marathi.pdf')
def maths6():
    WB.open(path6+'maths.pdf')
def science6():
    WB.open(path6+'science.pdf')
def story6():
    WB.open(stoorybook+'secret socity.pdf')
def story_6():
    WB.open(storybook+'tale of 2 cities')
def pic6():
    WB.open(picbook+'the dog service.pdf')
def class_6_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english6)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "Geography", variable = var,command=geo6)  
    menubutton.menu.add_checkbutton(label = "Science", variable = var,command=science6)  
    menubutton.menu.add_checkbutton(label = "History & Civics", variable = var,command=HS6) 
    menubutton.menu.add_checkbutton(label = "Hindi", variable = var,command=hindi6) 
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi6)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var,command=maths6)  
    menubutton.menu.add_checkbutton(label = 'Story Book-1', variable = var,command=story6)  
    menubutton.menu.add_checkbutton(label = 'Story Book-2', variable = var,command=story_6)  
    menubutton.menu.add_checkbutton(label = "Picture Book", variable = var,command=pic6)  
    menubutton.place(x=350,y=302)

path7=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 7\\')
def english7():
    WB.open(path7+'english.pdf')
def geo7():
    WB.open(path7+'geography.pdf')
def HC7():
    WB.open(path7+'history civics.pdf')
def marathi7():
    WB.open(path7+'marathi.pdf')
def maths7():
    WB.open(path7+'maths.pdf')
def science7():
    WB.open(path7+'science.pdf')
def story7():
    WB.open(storybook+'the wonderful wizard of oz.pdf')
def story_7():
    WB.open(storybook+'huckleberry finn.pdf')
def pic7():
    WB.open(picbook+'ginger and giraffe.pdf')
def class_7_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english7)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "Geography", variable = var,command=geo7)  
    menubutton.menu.add_checkbutton(label = "Science", variable = var,command=science7)  
    menubutton.menu.add_checkbutton(label = "History & Civics", variable = var,command=HC7) 
    menubutton.menu.add_checkbutton(label = "Hindi", variable = var) 
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi7)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var,command=maths7)  
    menubutton.menu.add_checkbutton(label = 'Story Book-1', variable = var,command=story7)  
    menubutton.menu.add_checkbutton(label = 'Story Book-2', variable = var,command=story_7)  
    menubutton.menu.add_checkbutton(label = "Picture Book", variable = var,command=pic7)  
    menubutton.place(x=350,y=435)

path8=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 8\\')
def english8():
    WB.open(path8+'english.pdf')
def geo8():
    WB.open(path8+'geography.pdf')
def hindi8():
    WB.open(path8+'hindi.pdf')
def HC8():
    WB.open(path8+'history civics.pdf')
def marathi8():
    WB.open(path8+'marathi.pdf')
def maths8():
    WB.open(path8+'maths.pdf')
def SANSKRIT():
    WB.open(path8+'sanskrit.pdf')
def science8():
    WB.open(path8+'science.pdf')
def class_8_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english8)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "Geography", variable = var,command=geo8)  
    menubutton.menu.add_checkbutton(label = "Science", variable = var,command=science8)  
    menubutton.menu.add_checkbutton(label = "Sanskrit", variable = var,command=SANSKRIT)  
    menubutton.menu.add_checkbutton(label = "History & Civics", variable = var,command=HC8) 
    menubutton.menu.add_checkbutton(label = "Hindi", variable = var,command=hindi8) 
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi8)  
    menubutton.menu.add_checkbutton(label = "Maths", variable = var,command=maths8)  
    menubutton.place(x=350,y=569)

path9=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 9\\')
def defence():
    WB.open(path9+'defence studies.pdf')
def english9():
    WB.open(path9+'english.pdf')
def hindi9():
    WB.open(path9+'Hindi.pdf')
def HPS():
    WB.open(path9+'history and political science.pdf')
def marathi9():
    WB.open(path9+'marathi.pdf')
def maths19():
    WB.open(path9+'maths 1.pdf')
def maths29():
    WB.open(path9+'maths 2.pdf')
def science_tech():
    WB.open(path9+'science and technology.pdf')
def class_9_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english9)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "Geography", variable = var)  
    menubutton.menu.add_checkbutton(label = "Science & Technology", variable = var,command=science_tech)  
    menubutton.menu.add_checkbutton(label = "Defence Studies", variable = var,command=defence)  
    menubutton.menu.add_checkbutton(label = "History & Political Science", variable = var,command=HPS) 
    menubutton.menu.add_checkbutton(label = "Hindi", variable = var,command=hindi9) 
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi9)  
    menubutton.menu.add_checkbutton(label = "Maths Part-1", variable = var,command=maths19)  
    menubutton.menu.add_checkbutton(label = "Maths Part-2", variable = var,command=maths29)  
    menubutton.place(x=687,y=170)

path10=('C:\\Users\\Monal\\Desktop\\kickstart\\.PDF\\class 10\\')
def english10():
    WB.open(path10+'english.pdf')
def hindi10():
    WB.open(path10+'hindi.pdf')
def HPS1():
    WB.open(path10+'history and political science.pdf')
def marathi10():
    WB.open(path10+'marathi.pdf')
def maths10():
    WB.open(path10+'maths 1.pdf')
def maths101():
    WB.open(path10+'maths 2.pdf')
def science_tech1():
    WB.open(path10+'science and technology part 1.pdf')
def science_tech2():
    WB.open(path10+'science and technology part 2.pdf')
def class_10_provision():
    menubutton = Menubutton(win, text = "Choose Book!",border=2,width=30,bg='white')  
    menubutton.place()
    menubutton.menu = Menu(menubutton)  
    menubutton["menu"]=menubutton.menu  
    menubutton.menu.add_checkbutton(label = 'English                                     ', variable=var,command=english10)  
    menubutton.menu.add_checkbutton(label = "Grammar", variable = var)  
    menubutton.menu.add_checkbutton(label = "Geography", variable = var)  
    menubutton.menu.add_checkbutton(label = "Science & Technology Part-1", variable = var,command=science_tech1)  
    menubutton.menu.add_checkbutton(label = "Science & Technology Part-2", variable = var,command=science_tech2)  
    menubutton.menu.add_checkbutton(label = "History & Political Science", variable = var,command=HPS1) 
    menubutton.menu.add_checkbutton(label = "Hindi", variable = var,command=hindi10) 
    menubutton.menu.add_checkbutton(label = 'Marathi', variable = var,command=marathi10)  
    menubutton.menu.add_checkbutton(label = "Maths Part-1", variable = var,command=maths10)  
    menubutton.menu.add_checkbutton(label = "Maths Part-2", variable = var,command=maths101)  
    menubutton.place(x=687,y=302)
def ViEw_It():
    class_1_provision()
    class_2_provision()
    class_3_provision()
    class_4_provision()
    class_5_provision()
    class_6_provision()
    class_7_provision()
    class_8_provision()
    class_9_provision()
    class_10_provision()
ViEw_It()
win.mainloop()