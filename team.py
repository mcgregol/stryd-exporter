import datetime

class Team:
	def __init__(self, exporter_list, timer, save_path):
		self.exporter_list = [exporter_list]
		self.timer = timer
		self.save_path = save_path
		self.start_date = datetime.date.today()