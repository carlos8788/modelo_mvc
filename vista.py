class EstudianteVista:
    def __init__(self, controlador):
        self.controlador = controlador

    def agregar_estudiante(self):
        nombre = input("Introduce el nombre del estudiante: ")
        self.controlador.agregar_estudiante(nombre)

    def mostrar_estudiantes(self):
        for estudiante in self.controlador.obtener_estudiantes():
            print(f'Estudiante: {estudiante}')
