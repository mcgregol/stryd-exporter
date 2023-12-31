from exporter import Exporter
from team import Team
from tkinter import *
from tkinter import ttk, filedialog, PhotoImage, messagebox
from tkcalendar import Calendar
import tkinter as tk
import asyncio, datetime, schedule

#  empty list to store all our teams
teams = []

def new_team():
	today = datetime.date.today()

	init_team_name = ""
	init_start_date = ""
	init_end_date = ""
	init_save_path = ""

	def create():
		if team_name_entry.get() in listbox.get(0, tk.END):
			messagebox.showwarning("Info", "This team name already exists!")
			return
			
		def add_team():
			team = Team(init_team_name,
				init_team_exporter_list,
				init_start_date,
				init_end_date,
				init_save_path)
			teams.append(team)
			listbox.insert(tk.END, init_team_name)
			new_popup.destroy()
			for team in teams:
				print(team.name)

		def add_player():
			#  create exporter objects and add to list and add object name to listbox
			player = Exporter(get_name.get() ,get_email.get(), get_password.get(), init_save_path)
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
		new_team_listbox.pack(side="left",
			padx=10,pady=10)

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
		nonlocal init_save_path
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

def edit_team():
	#  get selected team
	selected_index = listbox.curselection()
	if not selected_index:
		return
	target_team_name = listbox.get(selected_index[0])

	for team in teams:
		if hasattr(team, 'name') and getattr(team, 'name') == target_team_name:
			target_team = team

	today = datetime.date.today()
	
	def apply_edits():
		pass

	def set_save_path():
		pass

	def edit_roster():
		def edit_player():
			pass

		edit_roster_popup = Toplevel(edit_popup)
		edit_roster_popup.title("Edit Roster")
		edit_roster_popup.wm_attributes('-topmost', 1)
		ttk.Label(edit_roster_popup, text=target_team.name).pack(side="left", padx=10)
		existing_teams_listbox = Listbox(edit_roster_popup)
		existing_teams_listbox.pack(side="left",
			padx=10, pady=10)
		ttk.Button(edit_roster_popup, text="Save & Close", command=edit_popup.destroy).pack(side="right", padx=10)
		ttk.Button(edit_roster_popup, text="Edit Player", command=edit_player).pack(side="right", padx=10)
		# add players to listbox from target_team
		for player in target_team.exporter_list:
			existing_teams_listbox.insert(tk.END, player.player_name)

	edit_popup = Toplevel(root)
	edit_popup.geometry("900x500")
	edit_popup.title("Edit Team")
	ttk.Label(edit_popup, text="Team name:").pack(pady=10)
	team_name_entry = ttk.Entry(edit_popup)
	team_name_entry.insert(0, target_team.name)
	team_name_entry.pack()
	save_path_label = ttk.Label(edit_popup, text="Saving to: " + target_team.save_path)
	save_path_label.pack(pady=10)
	ttk.Button(edit_popup, text="Set save path", command=set_save_path).pack()
	#ttk.Label(edit_popup, text="Timer incrimentation(hrs):").pack()
	#team_timer_entry = ttk.Entry(edit_popup)
	ttk.Label(edit_popup, text="Set date range:").pack(pady=20)
	start_cal = Calendar(edit_popup, selectmode='day',
		year=today.year,
		month=today.month,
		day=today.day)
	start_cal.pack(side='left', padx=50)
	end_cal = Calendar(edit_popup, selectmode='day',
		year=today.year,
		month=today.month,
		day=today.day)
	end_cal.pack(side='right', padx=50)
	ttk.Button(edit_popup, text="Save Edits", command=apply_edits).pack(side='bottom', pady=50)
	ttk.Button(edit_popup, text="Edit Roster", command=edit_roster).pack(side='bottom', pady=50)

#  change back to pause_team for v2
def export_team():
	#  get selected team
	selected_index = listbox.curselection()
	if not selected_index:
		return
	target_team_name = listbox.get(selected_index[0])
	for team in teams:
		if hasattr(team, 'name') and getattr(team, 'name') == target_team_name:
			team.export()

def kill_team():
	#  get selected team
	selected_index = listbox.curselection()
	if not selected_index:
		return
	target_team_name = listbox.get(selected_index[0])
	for team in teams:
		if hasattr(team, 'name') and getattr(team, 'name') == target_team_name:
			del team
			listbox.delete(selected_index[0])

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
#ttk.Button(text="Pause", command=pause_team).pack(side="top", padx=50, pady=50)
ttk.Button(text="Export", command=export_team).pack(side="top", padx=50, pady=50)
ttk.Button(text="Kill", command=kill_team).pack(side="top", padx=50,)
ttk.Button(text="Quit", command=quit).pack(side="right", padx=50)

#  add logo
logo = PhotoImage(file='logo.png')
logo_label = ttk.Label(image=logo)
logo_label.pack(side='left', padx=40)

#  start gui
root.mainloop()
