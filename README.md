# Proyecto-final

# Robot-Reciclador-prog-III

# Descripción

Este repositorio contiene un programa de simulación de un robot que realiza tareas de exploración y recolección de objetos. El programa está escrito en Python y utiliza la biblioteca Tkinter para la interfaz gráfica y la biblioteca Transitions para implementar la lógica de la máquina de estados.

El código simula el comportamiento del robot mientras explora un entorno, sigue una trayectoria, ajusta su agarre y cámara, recoge y deposita objetos, se mueve y verifica eventos. Además, se proporciona una interfaz gráfica para interactuar con el robot y enviar instrucciones.

# Instrucciones de Uso

## Requisitos previos

- Python 3.x instalado en tu sistema.

## Instalación

1. Clona o descarga este repositorio.

2. Navega hasta el directorio del repositorio en tu sistema.

3. (Opcional) Crea y activa un entorno virtual para el proyecto.

   ```shell
   python3 -m venv myenv
   source myenv/bin/activate
   
4. instala las dependencias necesarias

-pip install -r requirements.txt

## Ejecución

1. Ejecuta el programa.
   - main.py
2. Se abrirá una ventana de interfaz gráfica donde podrás interactuar con el robot.

3. Haz clic en los diferentes botones para enviar instrucciones al robot y observar su comportamiento en la consola.

## Contribución

Si deseas contribuir a este proyecto, puedes seguir los pasos a continuación:

   1. Realiza un fork de este repositorio.

   2. Crea una rama con la nueva funcionalidad o corrección de errores.

   3. Realiza los cambios y commitea tus modificaciones.

   4. Envía un pull request para que revisemos tus cambios.
  
## Licencia

Este proyecto se encuentra bajo la Licencia MIT.

# Explicacion del Codigo 

Estado inicial: "home"

## Estados:

- "home": El estado inicial del robot.
- "exploring": El robot está en el proceso de exploración.
- "approaching": El robot se está acercando a un objeto.
- "grabbing": El robot está agarrando un objeto.
- "depositing": El robot está depositando un objeto.
- "moving": El robot se está moviendo a una nueva ubicación.
- "check": El robot está verificando los eventos o condiciones.
- "park": El robot está en el estado de estacionamiento.

## Transiciones:

- "explore": Transición del estado "home" al estado "exploring".
- "follow_trajectory": Transición del estado "exploring" al estado "approaching".
- "adjust_gripper_and_camera": Transición del estado "approaching" al estado "grabbing".
- "grab_object": Transición del estado "grabbing" al estado "depositing".
- "deposit_object": Transición del estado "depositing" al estado "moving".
- "move": Transición del estado "moving" al estado "check".
- "check_events": Transición del estado "check" al estado "park".
- "park": Transición desde cualquier estado al estado "home".

# main.py

from tkinter import *
from tkinter import messagebox
import sys
import random

from transitions import Machine

# Variables globales
v = 0
botellas = 0
latas = 0
papel = 0
recipientes = 0

class Robot:
    def _init_(self, window):
        """
        Clase que representa al robot.

        Args:
            window (Tk): Instancia de la ventana principal de Tkinter.

        Attributes:
            machine (Machine): Instancia de la máquina de estados.
            window (Tk): Instancia de la ventana principal de Tkinter.
            after_id (int): ID del temporizador para programar tareas.
            should_stop (bool): Bandera para detener la ejecución de tareas.
            current_category: Categoría actual del robot.
        """
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
        """
        # Inicia la exploración del robot.
        """
        self.explore()

    def explore(self):
        """
        # Realiza la exploración del entorno.
        """
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
        """
        # Sigue una trayectoria predefinida.
        """
        print("Following trajectory...")
        self.after_id = self.after(1000, self.adjust_gripper_and_camera)

    def adjust_gripper_and_camera(self):
        """
        # Ajusta la pinza y la cámara.
        """
        print("Adjusting gripper and camera...")
        self.after_id = self.after(1000, self.grab_object)

    def grab_object(self):
        """
        # Recoge un objeto.
        """
        print("Grabbing object...")
        self.after_id = self.after(1000, self.deposit_object)

    def deposit_object(self):
        """
        # Deposita un objeto.
        """
        print("Depositing object...")
        self.after_id = self.after(1000, self.move)

    def move(self):
        """
        # Mueve el robot.
        """
        print("Moving...")
        if not self.should_stop:
            self.after_id = self.after(1000, self.check_events)

    def park(self):
        """
        # Estaciona el robot.
        """
        print("Parking...")

    def check_events(self):
        """
        # Verifica los eventos y realiza las acciones correspondientes.
        """
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
        """
        # Programa una tarea para ejecutarse después de un tiempo determinado.

        Args:
            ms (int): Tiempo en milisegundos.
            func (function): Función a ejecutar.

        Returns:
            int: ID del temporizador para cancelar la tarea.
        """
        return self.window.after(ms, func)
        
    def stop(self):
        """
        # Detiene la ejecución de las tareas actuales.
        """
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None
            self.should_stop = False

class GUI:
    def _init_(self, robot):
        """
        #Clase que representa la interfaz gráfica del programa.

        Args:
            robot (Robot): Objeto Robot para interactuar con él.
        """
        self.robot = robot
        self.window = Tk()
        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        """
        # Crea los botones en la interfaz gráfica.
        """
        buttons_frame = Frame(self.window)
        buttons_frame.pack()

        # Primera fila de botones
        row1_frame = Frame(buttons_frame)
        row1_frame.pack(side=TOP)

        def set_category_1():
            global N
            N = 1
            self.robot.current_category = N

        def set_category_2():
            global N
            N = 2
            self.robot.current_category = N

        def set_category_3():
            global N
            N = 3
            self.robot.current_category = N

        def set_category_4():
            global N
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
        """
        # Establece la categoría actual del robot.

        Args:
            category (int): Categoría del objeto.
        """
        self.robot.current_category = category
        
    def add_explore_instruction(self):
        """
        # Añade la instrucción de exploración al robot.
        """
        self.robot.stop()
        self.robot.explore()
        
    def add_follow_instruction(self):
        """
        # Añade la instrucción de seguir trayectoria al robot.
        """
        self.robot.stop()
        self.robot.follow_trajectory()
        
    def add_adjust_instruction(self):
        """
        # Añade la instrucción de ajustar la pinza y la cámara al robot.
        """
        self.robot.stop()
        self.robot.adjust_gripper_and_camera()
        
    def add_grab_instruction(self):
        """
        # Añade la instrucción de recoger un objeto al robot.
        """
        self.robot.stop()
        self.robot.grab_object()
        
    def add_deposit_instruction(self):
        """
        # Añade la instrucción de depositar un objeto al robot.
        """
        self.robot.stop()
        self.robot.deposit_object()
        
    def add_move_instruction(self):
        """
        # Añade la instrucción de mover al robot.
        """
        self.robot.stop()
        self.robot.move()
        
    def add_park_instruction(self):
        """
        # Añade la instrucción de estacionar el robot.
        """
        self.robot.stop()
        self.robot.park()
        
    def emergency_shutdown(self):
        """
        # Realiza un apagado de emergencia del robot y muestra un mensaje de advertencia.
        """
        self.robot.stop()
        messagebox.showinfo("Emergency Shutdown", "Emergency shutdown. Please restart the program to reset the robot.")
        sys.exit()
        
    def process_instruction(self):
        """
        # Procesa la instrucción de verificación de eventos del robot.
        """
        if not self.robot.should_stop:
            self.robot.should_stop = True
            self.robot.check_events()
            
# Creación de la ventana principal de Tkinter
window = Tk()
robot = Robot(window)
gui = GUI(robot)
