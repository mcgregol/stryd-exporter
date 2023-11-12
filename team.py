from exporter import Exporter
import datetime

class Team:
	def __init__(self, name, exporter_list, start_date, end_date, save_path):
		self.name = name
		self.exporter_list = [exporter_list]
		self.start_date = start_date
		self.end_date = end_date
		self.save_path = save_path

	def export(self):
		print("YASSSSS")

	def change_name(self, new_name):
		name = new_name

	def change_dates(self, new_start_date, new_end_date):
		start_date = new_start_date
		end_date = new_end_date

	def change_save_path(self, new_save_path):
		save_path = new_save_path