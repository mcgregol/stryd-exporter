import datetime

class Team:
	def __init__(self, name, exporter_list, start_date, end_date, save_path):
		self.name = name
		self.exporter_list = [exporter_list]
		self.start_date = start_date
		self.end_date = end_date
		self.save_path = save_path