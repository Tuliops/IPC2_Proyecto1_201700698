from Piso import Piso
class ListaPisos:

    def __init__(self):
        self.primero = None
        self.siguiente = None 
        self.size = 0
    #Insertar
    def insertarPiso(self, nombre, R, C, F, S):
        nuevoPiso = Piso(nombre, R, C, F, S)
        self.size += 1
        if self.primero is None:
            self.primero = nuevoPiso
            self.ultimo = nuevoPiso
        else:
            self.ultimo.setSiguientePiso(nuevoPiso)
            self.ultimo = nuevoPiso

        #nuevoPiso.patrones.insertar(codigo, cadena)
        return nuevoPiso
    # Mostrar
    def mostrarPisos(self):
        print('----------------Lista-----------')
        tmp = self.primero
        for i in range(self.size):
            print('-----------------Piso',i+1,'---------------------')
            print('Nombre Piso :', tmp.getNombre())
            print('filas :', tmp.getR())
            print('columnas :', tmp.getC())
            print('Costo de dar Vuelta: ', tmp.getF())
            print('Costo de deslizar : ',tmp.getS())
            tmp.patrones.mostrarPatrones()
            tmp = tmp.getSiguientePiso()
            print('-----------------end---------------------')
    
    def mostrarNombres(self):
        print('Nombre de Pisos')
        tmp = self.primero
        for i in range(self.size):
            print(i+1,': ',tmp.getNombre())
            tmp = tmp.getSiguientePiso()
  
    
    def mostrarPatronesPorNombre(self,nombre):
        tmp = self.primero
        for i in range(self.size):
            if str(tmp.getNombre()) == str(nombre):
                tmp.patrones.mostrarPatrones()
                break
            else:
                tmp = tmp.getSiguientePiso()