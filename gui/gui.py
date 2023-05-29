from tkinter import *
from tkinter import messagebox
import sys

class GUI:
    def __init__(self, robot):
        self.robot = robot
        self.window = Tk()
        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        buttons_frame = Frame(self.window)
        buttons_frame.pack()

        # Primera fila de botones
        row1_frame = Frame(buttons_frame)
        row1_frame.pack(side=TOP)

        def set_category_1():
            
            N = 1
            self.robot.current_category = N

        def set_category_2():
           
            N = 2
            self.robot.current_category = N

        def set_category_3():
            
            N = 3
            self.robot.current_category = N

        def set_category_4():
            
            N = 4
            self.robot.current_category = N

        plastic_bottles_button = Button(row1_frame, text="botellas plasticas", command=set_category_1)
        plastic_bottles_button.pack(side=LEFT)

        cans_button = Button(row1_frame, text="latas", command=set_category_2)
        cans_button.pack(side=LEFT)

        plastic_containers_button = Button(row1_frame, text="contenedores", command=set_category_3)
        plastic_containers_button.pack(side=LEFT)

        paper_cardboard_button = Button(row1_frame, text="papel", command=set_category_4)
        paper_cardboard_button.pack(side=LEFT)
        # Segunda fila de botones
        row2_frame = Frame(buttons_frame)
        row2_frame.pack(side=TOP)

        explore_button = Button(row2_frame, text="Explore", command=self.add_explore_instruction)
        explore_button.pack(side=LEFT)

        follow_button = Button(row2_frame, text="Follow", command=self.add_follow_instruction)
        follow_button.pack(side=LEFT)

        adjust_button = Button(row2_frame, text="Adjust", command=self.add_adjust_instruction)
        adjust_button.pack(side=LEFT)

        grab_button = Button(row2_frame, text="Grab", command=self.add_grab_instruction)
        grab_button.pack(side=LEFT)

        deposit_button = Button(row2_frame, text="Deposit", command=self.add_deposit_instruction)
        deposit_button.pack(side=LEFT)

        move_button = Button(row2_frame, text="Move", command=self.add_move_instruction)
        move_button.pack(side=LEFT)

        check_button = Button(row2_frame, text="Check Events", command=self.process_instruction)
        check_button.pack(side=LEFT)
        
        park_button = Button(row2_frame, text="Park", command=self.add_park_instruction)
        park_button.pack(side=LEFT)
        
        emergency_button = Button(row2_frame, text="Emergency Shutdown", command=self.emergency_shutdown)
        emergency_button.pack(side=LEFT)
        
    def set_category(self, category):
        self.robot.current_category = category
        
    def add_explore_instruction(self):
        self.robot.stop()
        self.robot.explore()
        
    def add_follow_instruction(self):
        self.robot.stop()
        self.robot.follow_trajectory()
        
    def add_adjust_instruction(self):
        self.robot.stop()
        self.robot.adjust_gripper_and_camera()
        
    def add_grab_instruction(self):
        self.robot.stop()
        self.robot.grab_object()
        
    def add_deposit_instruction(self):
        self.robot.stop()
        self.robot.deposit_object()
        
    def add_move_instruction(self):
        self.robot.stop()
        self.robot.move()
        
    def add_park_instruction(self):
        self.robot.stop()
        self.robot.park()
        
    def emergency_shutdown(self):
        self.robot.stop()
        messagebox.showinfo("Emergency Shutdown", "Emergency shutdown. Please restart the program to reset the robot.")
        sys.exit()
        
    def process_instruction(self):
        if not self.robot.should_stop:
            self.robot.should_stop = True
            self.robot.check_events()