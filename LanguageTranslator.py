from tkinter import *
from googletrans import Translator
root = Tk()
translator = Translator()
root.geometry("600x500")
root.title("Khatri's Language Translator")
root.configure(bg="hotpink")
head = Label(root, text="TRANSLATOR", font=('Times',24,'bold'),bg="hotpink",anchor="center",padx=10,pady=30).grid(row=0, column=0)
label = Label(root, text=WORD,bg="hotpink",padx=-10).grid(row=1, column=0)
mn = StringVar()
textEntry=Entry(root, textvariable=mn).grid(row=2, column=0)
l1 = Label(root, text="Enter 1 for hindi",bg="hotpink",padx=-10).grid(row=3, column=0)
l2 = Label(root, text="Enter 2 for punjabi",bg="hotpink",padx=-10).grid(row=4, column=0)
l3 = Label(root, text="Enter 3 for bengali",bg="hotpink",padx=-10).grid(row=5, column=0)
ch = IntVar()
chEntry=Entry(root, textvariable=ch).grid(row=6, column=0)
if(ch.get() == 1):
    out = translator.translate(mn.get(),dest='hi')
if(ch.get() == 2):
    out = translator.translate(mn.get(),dest='pa')
if(ch.get() == 3):
    out = translator.translate(mn.get(),dest='bn')

def output():
    p  = Label(root, text=out.text,bg="hotpink",padx=-10).grid(row=8, column=0)

b = Button(root,text="Result", command = output).grid(row=7,column=0)
root.mainloop()
