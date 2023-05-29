from transitions import Machine
import random
import sys

global N
v = 0
botellas = 0
latas = 0
papel = 0
recipientes = 0

class Robot:
    def __init__(self, window):
        
        states = [
            "home",
            "exploring",
            "approaching",
            "grabbing",
            "depositing",
            "moving",
            "check",
            "park"
        ]

        transitions = [
            {"trigger": "explore", "source": "home", "dest": "exploring"},
            {"trigger": "follow_trajectory", "source": "exploring", "dest": "approaching"},
            {"trigger": "adjust_gripper_and_camera", "source": "approaching", "dest": "grabbing"},
            {"trigger": "grab_object", "source": "grabbing", "dest": "depositing"},
            {"trigger": "deposit_object", "source": "depositing", "dest": "moving"},
            {"trigger": "move", "source": "moving", "dest": "check"},
            {"trigger": "check_events", "source": "check", "dest": "park"},
            {"trigger": "park", "source": "*", "dest": "home"}
        ]

        self.machine = Machine(model=self, states=states, transitions=transitions, initial="home")
        self.window = window
        self.after_id = None
        self.should_stop = False
        self.current_category = None

    def start(self):
        self.explore()

    def explore(self):
        print("Exploring...")
        global v 
        v = random.randint(0, 7)
        if v == 0:
            print("Se encontraron", v, "objetos. Volviendo a home.")
            self.stop()
            self.park()
            return
        elif v > 0:
            print("Se encontraron", v, "objetos.")

        self.after_id = self.after(1000, self.follow_trajectory)

    def follow_trajectory(self):
        print("Following trajectory...")
        self.after_id = self.after(1000, self.adjust_gripper_and_camera)

    def adjust_gripper_and_camera(self):
        print("Adjusting gripper and camera...")
        self.after_id = self.after(1000, self.grab_object)

    def grab_object(self):
        print("Grabbing object...")
        self.after_id = self.after(1000, self.deposit_object)

    def deposit_object(self):
        print("Depositing object...")
        self.after_id = self.after(1000, self.move)

    def move(self):
        print("Moving...")
        if not self.should_stop:
            self.after_id = self.after(1000, self.check_events)

    def park(self):
        print("Parking...")

  
    
    def check_events(self):
        if N == 1:
            global botellas
            botellas += v
            print("La cantidad de botellas ahora es:", botellas, "botellas.")
        elif N == 2:
            global latas
            latas += v
            print("La cantidad de latas ahora es:", latas, "latas.")
        elif N == 3:
            global recipientes
            recipientes += v
            print("La cantidad de recipientes ahora es:", recipientes, "recipientes.")
        elif N == 4:
            global papel
            papel += v
            print("La cantidad de papel ahora es:", papel, "papel.")
        elif N is None:
            self.park()
        self.after_id = self.after(1000, self.park)

    def after(self, ms, func):
        return self.window.after(ms, func)
        
    def stop(self):
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None
            self.should_stop = False
