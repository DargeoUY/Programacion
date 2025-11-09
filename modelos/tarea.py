from modelos.actividad import Actividad

class Tarea(Actividad):
    def __init__(self, id_actividad, id_grupo, fecha, descripcion, estado, fecha_entrega, recursos):
        super().__init__(id_actividad, id_grupo, fecha, descripcion, estado)
        self.fecha_entrega = fecha_entrega
        self.recursos = recursos
