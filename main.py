#-------import-------
import xml.etree.ElementTree as ET

from ListaPisos import *
from ListaPatrones import ListaPatrones
#----------------------
pisos = ListaPisos()
patrones = ListaPatrones()
#---------------------
def MenuPrincipal(): 
    while True:
        # Mostramos el menu
        menu1()
    
        # solicituamos una opción al usuario
        opcionMenu = input("Seleccione una opcion >> ")
    
        if opcionMenu=="1":
           print("---->XML")
           

        elif opcionMenu=="2":
            print("---->¨Pisos y Patrones ")
            choose()
        elif opcionMenu=="3":
            print(" Mostrar Grafica ...")
           
        elif opcionMenu =="4":
            print("Seleccionar Nuevo ")
        elif opcionMenu=="5":
                    break
        else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\n pulsa una tecla para continuar")
def menu1():
    """
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
    #os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    
    print ("Selecciona una opción")
    print ("\t1 -  Cargar Archivo XML  ")
    print ("\t2 - Seleccionar un piso y patrón específico")
    print ("\t3 - Mostrar Graficamente el Patron")
    print ("\t4 - Seleccionar un nuevo código de patrón")
    print ("\t5  - salir")
        #Menu Principal del Programaa
xpath = ('./2.xml')

def elementTree(ruta):
    tree = ET.parse(ruta)
    raiz = tree.getroot()


    """print('Atributos')
    for element in raiz:
        for subelement in element:
            print(subelement.attrib)
            print(subelement.text)
        
    print('Valores')
    for element in raiz:
        for subelement in element:
            print(subelement.tag)
            print(subelement.text)"""
            



    #Leer los Nombres de los Pisos 
    for r in raiz:
        nombre = r.text.replace('\n','')
        
       
        nombre = r.attrib['nombre']
        nombre = str(nombre)
        
        R = ''
        C = ''
        F = ''
        
        S = ''
        for sub in r:
           
            tag = sub.tag 
            if tag =='R': 
                tag = tag.replace('\ ','')
                R = sub.text
                R = str(R)
                
            elif tag =='C': 
                tag = tag.replace('\ ','')
                C = sub.text
                C = str(C)
             
            elif tag =='F': 
                tag = tag.replace('\ ','')
                F = sub.text
                F = str(F)
              
            elif tag =='S': 
                tag = tag.replace('\ ','')
                S = sub.text
                S = str(S)
        piso = pisos.insertarPiso(nombre, R, C, F, S)
        for p in sub :
                
            Codigo = p.text.replace('\n', '')
            nombreCodigo = p.attrib['codigo']
            nombreCodigo = str(nombreCodigo)
            piso.patrones.insertar(nombreCodigo, Codigo)
        

def choose():
        while True:
            
            pisos.mostrarNombres()
            print("Esctiba el nombre")
            name = input()      
            pisos.mostrarPatronesPorNombre(name)
            print("salir a menu Principal Precione E")
            if name == 'E':
                break
            
          
if __name__ == "__main__":
    print(xpath)
    elementTree(xpath)
    MenuPrincipal()