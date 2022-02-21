
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








if __name__ == "__main__":
   MenuPrincipal()