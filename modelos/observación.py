from modelos.actividad import Actividad

class Observacion(Actividad):
    def __init__(self, id_actividad, id_grupo, fecha, descripcion, estado, notas, seguimiento, reflexion):
        super().__init__(id_actividad, id_grupo, fecha, descripcion, estado)
        self.notas = notas
        self.seguimiento = seguimiento
        self.reflexion = reflexion
