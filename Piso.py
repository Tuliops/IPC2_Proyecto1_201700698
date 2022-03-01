
#Nodo Piso 
from ListaPatrones import ListaPatrones
class Piso:
    #Contructor 

    def __init__(self, nombre, r, c, f, s):
        #Atributos 
        self.nombre = nombre
        self.filas = r
        self.columnas = c
        self.vuelta_Cost = f
        self.deslizar_Cost = s
        self.siguiente = None
        self.patrones = ListaPatrones()
    
 
  
    #Sigueinte
    def setSiguientePiso(self,piso ):
        self.siguiente = piso
    def getSiguientePiso(self):
        return self. siguiente
    #Get´s
    def getNombre(self):
        return self.nombre
    def getR(self):
        return self.filas
    def getC(self):
        return self.columnas
    def getF(self):
        return self.vuelta_Cost
    def getS(self):
        return self.deslizar_Cost
    #Set´s
    def setNombre(self, nombre):
        self.nombre = nombre
    def setR(self , r):
        self.filas = r 
    def setC(self, c):
        self.columnas = c
    def setF(self,f):
        self.vuelta_Cost = s
    def setS(self, s):
        self.deslizar_Cost = s