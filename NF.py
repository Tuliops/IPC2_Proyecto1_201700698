from ListaColumnas import ListaColumnas
class NF:
    def __init__(self):
        self.columnas = ListaColumnas()
        self.siguiente = None

    def getSigueinteFila(self):
        return self.siguiente

    def setSiguienteFila(self,columna):
        self.siguiente = columna
        