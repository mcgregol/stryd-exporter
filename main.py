from exporter import Exporter
from team import Team
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import asyncio, schedule

def new_team():
	init_team_name = ""
	init_incrimentation = 0
	init_save_path = ""

	def create():
		init_team_name = team_name_entry.get()
		init_incrimentation = team_timer_entry.get()

		create_roster = Toplevel(new_popup)
		create_roster.title("Create Roster")
		new_team_listbox = Listbox(create_roster)
		new_team_listbox.pack(side="left", padx=10, pady=10)

		ttk.Label(create_roster, text="Player Name:").pack()
		get_name = ttk.Entry(create_roster)
		get_name.pack(padx=10)

		ttk.Label(create_roster, text="Player email:").pack()
		get_email = ttk.Entry(create_roster)
		get_email.pack(padx=10)

		ttk.Label(create_roster, text="Player password:").pack()
		get_password = ttk.Entry(create_roster)
		get_password.pack(padx=10)

		ttk.Button(create_roster, text="Add Player").pack(padx=10, pady=10)
		ttk.Button(create_roster, text="Save & Close", command=new_popup.destroy).pack(padx=10, pady=10)

	def set_save_path():
		directory = filedialog.askdirectory()
		if directory:
			save_path_label.config(text="Saving to: " + directory)
			init_save_path = directory

	new_popup = Toplevel(root)
	new_popup.geometry("400x300")
	new_popup.title("New Team")
	ttk.Label(new_popup, text="Team name:").pack()
	team_name_entry = ttk.Entry(new_popup)
	team_name_entry.pack()
	save_path_label = ttk.Label(new_popup, text="Saving to: undefined")
	save_path_label.pack(pady=10)
	ttk.Button(new_popup, text="Set save path", command=set_save_path).pack(pady=10)
	ttk.Label(new_popup, text="Timer incrimentation(hrs):").pack()
	team_timer_entry = ttk.Entry(new_popup)
	team_timer_entry.pack()
	ttk.Button(new_popup, text="Create Team & Roster", command=create).pack(pady=50)

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