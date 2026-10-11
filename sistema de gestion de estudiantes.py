
# Sistema de Gestión de Estudiantes
# Proyecto de programación orientada a objetos (POO)


# Definimos la clase Estudiante.
class Estudiante:

    # Constructor: inicializa los atributos de cada estudiante.
    def __init__(self, nombre, matricula, calificacion1, calificacion2):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2

    # Método para calcular el promedio de las calificaciones.
    def calcular_promedio(self):
        promedio = (self.calificacion1 + self.calificacion2) / 2
        return promedio

    # Método para determinar si el estudiante aprobó.
    def obtener_estado(self):
        if self.calcular_promedio() >= 70:
            return "Aprobado"
        else:
            return "Reprobado"

    # Método para mostrar los datos del estudiante.
    def mostrar_informacion(self):
        print("------------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Calificación 1: {self.calificacion1}")
        print(f"Calificación 2: {self.calificacion2}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        print(f"Estado: {self.obtener_estado()}")
        print("------------------------------")


# Programa principal: creamos tres objetos de la clase Estudiante.
estudiante1 = Estudiante("Carlos", "A001", 85, 90)
estudiante2 = Estudiante("María", "A002", 55,58)
estudiante3 = Estudiante("Luis", "A003", 60, 65)

# Ejecutamos los métodos de cada objeto.
estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()
estudiante3.mostrar_informacion()
