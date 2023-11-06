from exporter import Exporter
from tkinter import *
from tkinter import ttk
import asyncio, time, schedule

def new_team():
	pass

def kill_team():
	pass

def edit_team():
	pass

def pause_team():
	pass

def quit():
	root.destroy()

#  create window/frame
root = Tk()
root.title("Stryd Exporter")
root.geometry("600x400")

#  title
ttk.Label(text="Teams:").place(x=90, y=50)

#  create listbox for teams
listbox = Listbox()
listbox.place(x=40, y=80)

#  add buttons
ttk.Button(text="New", command=new_team).pack(side="top", padx=50, pady=50)
ttk.Button(text="Edit", command=edit_team).pack(side="top", padx=50)
ttk.Button(text="Pause", command=pause_team).pack(side="top", padx=50, pady=50)
ttk.Button(text="Kill", command=kill_team).pack(side="top", padx=50,)
ttk.Button(text="Quit", command=quit).pack(side="right", padx=50)

#  start gui
root.mainloop()




## TODO
##  every instance of exporter runs on async timer
##  create "kill" function
##  create UI