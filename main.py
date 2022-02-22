#-------import-------
import xml.etree.ElementTree as ET


#----------------------
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
        print(r.attrib['nombre'],nombre)
        print("--Matriz-----")
        for sub in r:
            R = ''
            C = ''
            F = ''
            S = ''
            tag = sub.tag 
            if tag =='R': 
                tag = tag.replace('\ ','')
                R = sub.text
                print("R = ",R)
            elif tag =='C': 
                tag = tag.replace('\ ','')
                C = sub.text
                print("C = ",C)
            elif tag =='F': 
                tag = tag.replace('\ ','')
                F = sub.text
                print("F = ",F)
            elif tag =='S': 
                tag = tag.replace('\ ','')
                S = sub.text
                print("S = ",S)
            for p in sub :
                
                Codigo = p.text.replace('\n', '')
                nombreCodigo = p.attrib['codigo']
                
               




                print('\t','\t Nombre de Codigo ',nombreCodigo,'\n', '\t\tCodigo --->',Codigo)
if __name__ == "__main__":
    print(xpath)
    elementTree(xpath)