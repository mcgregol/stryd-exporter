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

#  create window/frame
root = Tk()
root.title("Stryd Exporter")
root.geometry("800x500")

#  title
ttk.Label(text="Teams:").place(x=90, y=50)

#  create listbox for teams
listbox = Listbox()
listbox.place(x=40, y=80)

#  button to create team
ttk.Button(text="New", command=new_team).pack(side="right", padx=300)

#  start gui
root.mainloop()




## TODO
##  every instance of exporter runs on async timer
##  create "kill" function
##  create UI