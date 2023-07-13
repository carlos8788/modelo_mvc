class EstudianteControlador:
    def __init__(self, modelo):
        self.modelo = modelo

    def agregar_estudiante(self, nombre):
        self.modelo.agregar_estudiante(nombre)

    def obtener_estudiantes(self):
        return self.modelo.obtener_estudiantes()
