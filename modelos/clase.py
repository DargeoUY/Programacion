from modelos.actividad import Actividad

class Clase(Actividad):
    def __init__(self, id_actividad, id_grupo, fecha, descripcion, estado, tema, modalidad, materiales):
        super().__init__(id_actividad, id_grupo, fecha, descripcion, estado)
        self.tema = tema
        self.modalidad = modalidad
        self.materiales = materiales
