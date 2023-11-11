from exporter import Exporter
from team import Team
from tkinter import *
from tkinter import ttk, filedialog, PhotoImage, messagebox
from tkcalendar import Calendar
import tkinter as tk
import asyncio, datetime, schedule

def new_team():
	today = datetime.date.today()

	init_team_name = ""
	init_incrimentation = 0
	init_save_path = ""

	def create():
		if team_name_entry.get() in listbox.get(0, tk.END):
			messagebox.showwarning("Info", "This team name already exists!")
			return
			
		def add_team():
			listbox.insert(tk.END, init_team_name)
			new_popup.destroy()

		def add_player():
			#  create exporter objects and add to list and add object name to listbox
			player = Exporter(get_name.get() ,get_email.get(), get_password.get())
			init_team_exporter_list.append(player)
			new_team_listbox.insert(tk.END, player.player_name)
			get_name.delete(0, 'end')
			get_email.delete(0, 'end')
			get_password.delete(0, 'end')

		init_team_exporter_list = []
		init_team_name = team_name_entry.get()
		#init_incrimentation = team_timer_entry.get()

		create_roster = Toplevel(new_popup)
		create_roster.title("Create Roster")
		create_roster.wm_attributes('-topmost', 1)
		ttk.Label(create_roster, text=init_team_name).pack(side="left", padx=10)
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

		ttk.Button(create_roster, text="Add Player", command=add_player).pack(padx=10, pady=10)
		ttk.Button(create_roster, text="Save & Close", command=add_team).pack(padx=10, pady=10)

	def set_save_path():
		directory = filedialog.askdirectory()
		if directory:
			save_path_label.config(text="Saving to: " + directory)
			init_save_path = directory
			new_popup.wm_attributes('-topmost', 1)

	new_popup = Toplevel(root)
	new_popup.geometry("900x500")
	new_popup.title("New Team")
	ttk.Label(new_popup, text="Team name:").pack(pady=10)
	team_name_entry = ttk.Entry(new_popup)
	team_name_entry.pack()
	save_path_label = ttk.Label(new_popup, text="Saving to: undefined")
	save_path_label.pack(pady=10)
	ttk.Button(new_popup, text="Set save path", command=set_save_path).pack()
	#ttk.Label(new_popup, text="Timer incrimentation(hrs):").pack()
	#team_timer_entry = ttk.Entry(new_popup)
	ttk.Label(new_popup, text="Set date range:").pack(pady=20)
	start_cal = Calendar(new_popup, selectmode='day',
		year=today.year,
		month=today.month,
		day=today.day)
	start_cal.pack(side='left', padx=50)
	end_cal = Calendar(new_popup, selectmode='day',
		year=today.year,
		month=today.month,
		day=today.day)
	end_cal.pack(side='right', padx=50)
	ttk.Button(new_popup, text="Create Team & Roster", command=create).pack(side='bottom', pady=50)

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

#  add logo
logo = PhotoImage(file='logo.png')
logo_label = ttk.Label(image=logo)
logo_label.pack(side='left', padx=40)

#  start gui
root.mainloop()
