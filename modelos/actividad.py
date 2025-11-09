class Actividad:
    def __init__(self, id_actividad, id_grupo, fecha, descripcion, estado):
        self.id_actividad = id_actividad
        self.id_grupo = id_grupo
        self.fecha = fecha
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"{self.descripcion} ({self.estado})"
