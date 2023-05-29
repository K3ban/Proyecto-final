from states.robot import Robot
from gui.gui import GUI
from tkinter import Tk

window = Tk()
robot = Robot(window)
gui = GUI(robot)
window.mainloop()

v = 0
botellas = 0
latas = 0
papel = 0
recipientes = 0