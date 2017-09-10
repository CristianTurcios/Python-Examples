class Students:
    """Test for Students."""
    def __init__(self, nombre, apellido, universidad):
        self.nombre = nombre
        self.apellido = apellido
        self.universidad = universidad

    def getAllDataOfStudent(self):
        return ('Nombre: %s , Apellido: %s , Universidad: %s'
                %(self.nombre, self.apellido, self.universidad))
