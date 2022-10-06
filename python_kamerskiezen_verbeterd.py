import tkinter as tk
from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import date

today = date.today()

#define on button and check which room is chosen

def on_button():
    for i in l.curselection():
        if OPTIONS[i] == "Kamer 1":
            print("gekozen voor kamer 1")
            root.destroy()
            datepick()
        elif OPTIONS[i] == "Kamer 2":
            print("gekozen voor kamer 2")
            root.destroy()
            datepick()
        elif OPTIONS[i] == "Kamer 3":
            print("gekozen voor kamer 3")
            root.destroy()
            datepick()
    print()

def datepick():
    def datechoice():
        print(cal.get_date())
    win = tk.Tk()
    #Set the Geometry
    win.geometry("250x250")
    win.title("Date Picker")
    #Create a Label
    Label(win, text= "Kies een datum", foreground="white", bg='#2da3b3').pack(padx=20,pady=20)
    #Create a Calendar using DateEntry
    cal = DateEntry(win, width= 16, background="magenta3", foreground="white", bd=2, mindate=today)
    cal.pack(pady=20)
    b = tk.Button(win, text='OK', command=datechoice)
    b.pack(fill='x')
    win.mainloop()


# --- tkinter list and menu ---

OPTIONS = ["Kamer 1", "Kamer 2", "Kamer 3"]

root = tk.Tk()
root.geometry("500x200")
root.title("kamerkiezer")

# --- Listbox ---

tk.Label(root, text='Kamers', bg='#2da3b3').pack(fill='x')

l = tk.Listbox(root, selectmode='single', bg='#2da3b3')
l.pack()
l.insert('end', *OPTIONS)

# --- ok button and call function ---

b = tk.Button(root, text='OK', command=on_button)
b.pack(fill='x')

root.mainloop()