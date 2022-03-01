
from Patron import Patron

class ListaPatrones:
    def __init__(self) :
        self.primero = None 
        self.ultimo = None
        self.size = 0
    
    #Metodo Insertar
    
    def insertar(self, codigo, cadena):
        nuevoPatron = Patron(codigo, cadena)
        self.size +=1

        if self.primero is None:
            self.primero = nuevoPatron
            self.ultimo = nuevoPatron
        else :
            self.ultimo.setSiguiente(nuevoPatron)
            self.ultimo = nuevoPatron


       
    def mostrarPatrones(self):
        print('Lista Patrones ')
        tmp = self.primero
        
        for i in range(self.size):
            print('--------------')
            print(i,'Codigo :', tmp.getCodigo())
            print('Cadena ', tmp.getCadena())
            tmp = tmp.getSiguiente()
            print('------------')
    