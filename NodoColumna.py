class NodoColumna:
    def  __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        

    def getDatoColuman(self):
        return self.dato

    def setDatoColuman(self, dato):
        self.dato = dato
    
    def getSiguienteColumna(self):
        return self.siguiente
    
    def setSiguenteColumna(self,dato):
        self.siguiente = dato
        
