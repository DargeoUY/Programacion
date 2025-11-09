from modelos.actividad import Actividad

class Prueba(Actividad):
    def __init__(self, id_actividad, id_grupo, fecha, descripcion, estado, tipo, puntaje_maximo=100):
        super().__init__(id_actividad, id_grupo, fecha, descripcion, estado)
        self.tipo = tipo
        self.puntaje_maximo = puntaje_maximo
