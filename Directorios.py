import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")

# Directorios principales
create_directory("RobotReciclador")

# Subdirectorios dentro de la carpeta principal
create_directory("RobotReciclador/robot")
create_directory("RobotReciclador/gui")
create_directory("RobotReciclador/recursos")
create_directory("RobotReciclador/imagenes")



def create_file(directory, filename):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        file.write("Contenido del archivo.")
    print(f"File '{filename}' created in directory '{directory}'.")

# Archivos dentro de la carpeta 'robot'
create_file("RobotReciclador/robot", "__init__.py")
create_file("RobotReciclador/robot", "control_movimiento.py")
create_file("RobotReciclador/robot", "procesamiento_imagenes.py")
create_file("RobotReciclador/robot", "control_garra.py")
create_file("RobotReciclador/robot", "maquina_estados.py")

# Archivos dentro de la carpeta 'gui'
create_file("RobotReciclador/gui", "__init__.py")
create_file("RobotReciclador/gui", "Ventana_principal.py")
create_file("RobotReciclador/gui", "Botones.py")
create_file("RobotReciclador/gui", "Labels.py")

# Archivos dentro de la carpeta 'resources'
create_file("RobotReciclador/recursos", "PROYECTO.MD")
create_file("RobotReciclador/recursos", "requierments.txt")

# Archivos dentro de la carpeta 'images'
#create_file("RobotReciclador/imagenes", "image1.jpg")
#create_file("RobotReciclador/imagenes", "image2.jpg")



