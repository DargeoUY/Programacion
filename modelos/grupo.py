class Grupo:
    def __init__(self, id_grupo, nombre, asignatura, turno, horario):
        self.id_grupo = id_grupo
        self.nombre = nombre
        self.asignatura = asignatura
        self.turno = turno
        self.horario = horario
        self.actividades = []

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)

    def __str__(self):
        return f"{self.nombre} - {self.asignatura} ({self.turno})"
