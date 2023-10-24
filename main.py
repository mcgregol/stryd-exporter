from exporter import Exporter
from appJar import gui
import asyncio, time, schedule

#  start gui
app = gui("Stryd Exporter by ACHIEVE", "800x500")
app.setBg("grey")
app.go()








## TODO
##  every instance of exporter runs on async timer
##  create "kill" function
##  create UI