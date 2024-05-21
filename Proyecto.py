class proyecto:
    def __init__(self, codigo=None, descripcion=None, tematica=None, academia=None, prioridad=None, fecha_inicio=None, fecha_fin=None):
        self.codigo = codigo
        self.descripcion = descripcion
        self.tematica = tematica
        self.academia = academia
        self.prioridad = prioridad
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin




    def __str__(self):
        return (f'Id: {self.codigo}, Descripcion: {self.descripcion}, tematica: {self.tematica},
                academia: {self.academia},prioridad: {self.prioridad}, fecha_inicio: {self.fecha_inicio}, fecha_fin: {self.fecha_fin}')
                