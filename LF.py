from NF import NF
class LF:
    def __init__(self):
        self.primero = None
        self.siguiente = None
        self.size = 0
    
    def addFila(self):
        nuevaFila = NF()
        self.size += 1
        if self.primero == None :
            self.primero = nuevaFila
            self.ultimo = nuevaFila
        else:
            self.ultimo.setSiguienteFila(nuevaFila)
            self.ultimo = nuevaFila
        return nuevaFila

    def mostrarLF(self):
        print("----Datos en Fila---- ")
        tmp = self.primero
        for i in range(self.size):
            print("Fila : " , i)
            tmp.columnas.MostrarColumnas()
            tmp = tmp.getSigueinteFila()
        