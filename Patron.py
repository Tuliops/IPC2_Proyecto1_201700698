class Patron:   #clase nodo 
    def __init__(self, codigo, cadena ):
        self.codigo = codigo
        self.cadena = cadena
        self.siguiente = None
    
    def setSiguiente(self, patron):
        self.siguiente = patron
    #Gets
    def getCodigo(self):
        return self.codigo

    def getCadena(self):
        return self.cadena
    #sets 
    def setCodigo(self,codgo):
        self.codigo = codigo
    def setCodigo(self , Codigo):
        self.cadena = cadena 

## Para siguiente 
  
    def getSiguiente(self):
        return self.siguiente
 

