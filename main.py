# Package
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

# Font 
fnt = ('traditional arabic', 18)

# dif button
def su1():
  messagebox.showinfo('Surah selection',"سورتی الفاتحە")
  os.systam("quran1.mp3")

def su2():
  messagebox.showinfo('Surah selection',"سورتی البقر")
  os.systam("quran2.mp3")

def su3():
  messagebox.showinfo('Surah selection',"سورتی ال عمران")
  os.systam("quran3.mp3")

def su4():
  messagebox.showinfo('Surah selection',"سورتی النسا ")
  os.systam("quran4.mp3")

def su5():
  messagebox.showinfo('Surah selection',"سورتی المائد ")
  os.systam("quran5.mp3")

def su6():
  messagebox.showinfo('Surah selection',"سورتی العام ")
  os.systam("quran6.mp3")

def su7():
  messagebox.showinfo('Surah selection',"سورتی الاعراف ")
  os.systam("qura7.mp3")

def su8():
  messagebox.showinfo('Surah selection',"سورتی النفال ")
  os.systam("qura8.mp3")

def su9():
  messagebox.showinfo('Surah selection',"سورتی التوبە ")
  os.systam("qura9.mp3")

def su9():
  messagebox.showinfo('Surah selection',"سورتی یونس ")
  os.systam("qura10.mp3")

def su10():
  messagebox.showinfo('Surah selection',"سورتی یونس ")
  os.systam("qura10.mp3")

# Form
root=Tk()
root.geometry('1280x720')
root.title('Quran app')

# Buttons

lblTitle = Label(root, text=' Quran app by lion of kurdistan', font=('andalus',25))
lblTitle.pack()

fatehah = Button(root, text='سورتی الفا تحە',font=fnt, command= su1)
fatehah.pack()

baqarah = Button(root, text='سورتی البقرە',font=fnt,command= su2)
baqarah.pack()

amran = Button(root, text='سورتی ال عمران',font=fnt, command=su3)
amran.pack()

nesaa = Button(root, text='سورتی النسا',font= fnt, command=su4)
nesaa.pack()

maedah = Button(root,text='سورتی المائد', font=fnt, command=su5)
maedah.pack()

anaam = Button(root, text='سورتی العام', font = fnt, command=su6)
anaam.pack()

aaraf = Button(root, text='سورتی الاعراف', font=fnt,command=su7)
aaraf.pack()

anfal = Button(root,text='سورتی النفال', font = fnt, command=su8)
anfal.pack()

tawbah = Button(root, text='سورتی التوبە', font=fnt, command=su9)
tawbah.pack()

yunus = Button(root, text='سورتی یونس', font=fnt, command=su10)
yunus.pack()

root.mainloop()
