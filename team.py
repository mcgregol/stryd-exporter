from exporter import Exporter
import datetime

class Team:
    def __init__(self, name, exporter_list, start_date, end_date, save_path):
        self.name = name
        self.exporter_list = exporter_list
        self.start_date = start_date
        self.end_date = end_date
        self.save_path = save_path

    def export(self):
        for player in self.exporter_list:
            player.export()
            print(player.get_player_name() + " has been exported!")

    def change_name(self, new_name):
        self.name = new_name

    def change_dates(self, new_start_date, new_end_date):
        self.start_date = new_start_date
        self.end_date = new_end_date

    def change_save_path(self, new_save_path):
        self.save_path = new_save_path