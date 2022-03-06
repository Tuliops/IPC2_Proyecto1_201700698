from NodoColumna import NodoColumna
class ListaColumnas:
    def __init__(self):
        self.primero = None
        self.siguiente = None
        self.size = 0

    def InsertElementoAColumna (self,dato):
        nuevo = NodoColumna(dato)
        self.size += 1
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else :
            self.ultimo.setSiguenteColumna(nuevo)
            self.ultimo = nuevo
        return nuevo
        

    def MostrarColumnas(self):
        tem = self.primero

        for i in range(self.size):
            print("Columnas")
            print(i," :" , tem.getDatoColuman())
            tem = tem.getSiguienteColumna()
    
    def RetornarColumna(self):
        tmp = self.primero
        for i in range(self.size):

            return tmp
            tmp = tmp.getSiguienteColumna()