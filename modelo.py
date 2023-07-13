class EstudianteModelo:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre):
        self.estudiantes.append(nombre)

    def obtener_estudiantes(self):
        return self.estudiantes
