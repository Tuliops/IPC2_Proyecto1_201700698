#-------import-------


import xml.etree.ElementTree as ET



from ListaPisos import *


from ListaPatrones import ListaPatrones

from ListaColumnas import ListaColumnas
from LF import LF

#----------------------
nColumna = ListaColumnas()
nFila = LF()



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
           CargarArchivo()



        elif opcionMenu=="2":


            print("---->¨Pisos y Patrones ")


            choose()


        elif opcionMenu=="3":


            print("----- Cambiar de un Patron a otro ...")
            CambioPatrones()
           


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


    print ("\t2 - Mostrar  piso y patrón específico")


    print ("\t3 - Cambiar de un Patron a otro ")



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


            print("--------salir a menu Principal Precione E -------")


            print("-----------NOMBRES DE LOS PISOS-------------")
            


            print("Esctiba el nombre")


            pisos.mostrarNombres()
            name = input()      


            pisos.mostrarPatronesPorNombre(name)


            matrizdelospisos(name)
           


            if name == 'E':


                break


def matrizdelospisos(name):
    


    while True :


        print("-----------salir a menu Principal PISOS E ------------")


        print("----------PATRONES DEL PISO ----------")


        print("Esctiba el codigo del patron")
        c=''
        c = input()


        
        if c !='':
            print(c)
            if c == 'E':

                 break
                
            else:
                cod = pisos.cadenapatrones(c , name)


                columnas = pisos.retornarnoColumnas(name)

      
                filas = pisos.retornarnoFilas(name)
                Graficar(cod, columnas, filas)
                

        print("codigo para la matriz -> ")
        if c == 'E':


            break



#Graficar


import graphviz




def Graficar(cod,columans,filas):
    
    contfilas = 1
    print("Matris de ")
    print(columans, "  Columnas")
    print( filas, "  Filas ")
    fila =''
    cont = 0
    cn=1
    contenidoTabla = '''<TR>'''
    g = graphviz.Digraph(filename='structs_revisited.gv')
    
    for c in cod:
        if c == 'B':
            g.attr('node',shape='record', style='filled', color='black')
            g.node(str(cn) ,label= c)
            contenidoTabla += '<TD  COLOR = "WHITE" BGCOLOR="BLACK">     </TD>'
            
            cn += 1
            cont += 1
            fila += c
        elif c=='W':
            g.attr('node',shape='record', style='filled',color="lightgrey",bgcolor='black')
            g.node(str(cn) ,label= c)
            contenidoTabla += '<TD   COLOR = "BLACK" BGCOLOR="WHITE">     </TD>'
            cn += 1
            cont += 1
            
            fila += c

       
        if cont >= int(columans):
            print(fila)
            fila = ''
            cont = 0
            
            
            contenidoTabla +='</TR>'
            if contfilas != int(filas):

                contenidoTabla +='<TR>'
                contfilas += 1
            else:
                break
        

   
    g.node('structx', '''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="3" CELLPADDING="3">
        '''
        +contenidoTabla+
        '''
        </TABLE>>''')     
            
    g.view()
    
def CambioPatrones():
    pisos.mostrarNombres()
    print("ingrese al Piso a elegir")
    nombre = input()
    pisos.mostrarPatronesPorNombre(nombre)
    filas = pisos.retornarnoFilas(nombre)
    columnas = pisos.retornarnoColumnas(nombre)
    while True:
        print("Ingrese Codigo de Piso  ")
        piso1  = input()
        piso1 = pisos.cadenapatrones(piso1, nombre)
        print(piso1)
        if piso1 == None:
            print("Error Codigo de Piso 1  ")
                
        else:
            break

    while True:
            
        print("Ingrese Codigo de Piso 2")
        piso2 =  input()
        piso2 = pisos.cadenapatrones(piso2, nombre)
        print(piso2)
        if piso2 == None:
            print("Error en Codigo de Piso")
            
        else:
            break
                

    print("Todo Correcto ")
    print("piso1 -> ", piso1)
    print("piso2 ->", piso2)
    Cambio(piso1, piso2,filas,columnas)
    


def Cambio(piso1,piso2,filas,columans):
    print("Entra al Cambio")
    lex1=''
    lex2=''
    cont = 0
    
    for c in range(len(piso1)):
        
        
        lex1 += piso1[c]
        lex2 += piso2[c]
        cont += 1
        
        if cont == int(columans):
            F = nFila.addFila()
            for l1 in lex1:
                F.columnas.InsertElementoAColumna(l1)

            lex1 = ''
            lex2 = ''
            cont = 0
    
    tmpF = nFila.primero
    contaP2 = 0
    c = columans
    c = int(c)
    c = c-1
    controladorColumnas = 0
    lexColumnas = ''
    Graficar(piso1, columans, filas)
    for i in range(nFila.size):
        print("Filas : ", i)
        t =  nFila.primero.columnas.primero
        x = t.siguiente
        print()
        for j in range(nFila.primero.columnas.size):

            #Demtrp de la las Filas y Columnas
            print("Columna " ,j, " : ")

            x = nFila.primero.columnas.primero.siguiente
        
            
            print()
            #print("columna j +1 " , j+1, " : ", x)
            
            
            if x is None:
                pass
            else :
                print("BUSQUEDA DE ERRORES  ")
                if t.getDatoColuman() == piso2[contaP2]:
                   print("DATO EN FILA : ",i, "Y COLUMNA :" ,j)
                   print("ES IGUAl No HAY CAMBIOS")
                else:
                    print("--------------------------------------------")
                    print("DATO EN FILA : ",i, "Y COLUMNA :" ,j)
                    print("!NO! SON IGUALES ")
                    
                    
                    if (t.getDatoColuman() == x.getDatoColuman() ):
                        
                        print("SE DEBE  DAR VUELTA AL AZULEJO")
                        if t.getDatoColuman() == 'W':
                            t.setDatoColuman('B')
                            print("CAMBIO DE 'W' A 'B " )
                            print()
                            print("-------------------------")
                        elif t.getDatoColuman() =='B':
                            t.setDatoColuman('W')
                            print("CAMBIO DE 'B' A 'W " )
                            print()
                            print("-------------------------")
                        
                    elif controladorColumnas == c:
                         print("SE DA VUELTA ")
                         if t.getDatoColuman() == 'W':
                            t.setDatoColuman('B')
                            print("CAMBIO DE 'W' A 'B " )
                            print()
                            print("-------------------------")

                         elif t.getDatoColuman() =='B':
                            t.setDatoColuman('W')
                            print("CAMBIO DE 'B' A 'W " )
                            print()
                            print("-------------------------")
                        

                         
                         controladorColumnas = 0
                         


                    else:
                        
                        print("SE  MUEVE A LA IZQUIERDA ")
                        if t.getDatoColuman() =='W':
                            print("SE CAMBIA DE 'W' A 'B' ")
                            t.siguiente.setDatoColuman('W')
                            t.setDatoColuman('B')
                            print()
                            print("-------------------------")
                            
                        elif t.getDatoColuman() =='B':
                            print("SE CAMBIA DE 'B' A 'W' ")
                            
                            t.siguiente.setDatoColuman('B')
                            t.setDatoColuman('W')
                            print()
                            print("-------------------------")
                            
                        
                print("LA FILA PRESENTA LOS CAMBIOS  ", lexColumnas)
            #PARA GRAFICAR LOS MOVIMIENTOS CREADOS 
            p = ''
            z = nFila.primero.columnas.primero
            for w in range(nFila.primero.columnas.size):
                p +=  z.getDatoColuman()
                z = z.getSiguienteColumna()
              
            Graficar(p, columans, 1)
        
            lexColumnas += t.getDatoColuman()     
            contaP2 += 1
            controladorColumnas +=1
            t = t.siguiente
            x = x.siguiente
            grafColum = ''
      
       
    
        tmpF = nFila.siguiente 
    print("GRAFICA MOVIMIENTO FINAL ")
    Graficar(lexColumnas, columans, filas)

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import io
from io import * 

def CargarArchivo():
        print("Boton Cargar Archivo")
        root=Tk()
        #Abre Ventana para Buscar el archivo .lfp 
        archivo =  filedialog.askopenfilename(initialdir = "/") 
            #Abre el achivo 
        
        root.destroy()
        elementTree(archivo)


if __name__ == "__main__":

    
    """print(xpath)


    elementTree(xpath)"""

    
    MenuPrincipal()