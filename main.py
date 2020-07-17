#importacion de modulos 
import DiccionariosEnfermedades as Diccionario 
import DiccionariosCentrosMedicos as Centros 
#as es para llamar de otra forma a los módulos
#las letras antepuestas en las variables indican el tipo de dato
#creacion de variables globales 
        # \n —> salto de linea  

bInicioPrograma = True
sLinea = ("-"*43) 
sEspacio1 =  (" "*13) 
sEspacio2 =  (" "*7)  

sMensajeEntrada = sEspacio2+"Portal de apoyo e información\nde tratamientos de enfermedades autoinmunes\n"+sLinea+"\n"+sEspacio1+"Ingrese la opción\n"+sLinea+"\n(a) Buscar centros medicos\n(b) Informacion de enfermedades autoinmunes\n(c) Salir\n" 

sMensajeEnfermedad = "Ingrese una enfermedad o un termino:\n" 

sMensajeLugar = "Ingrese un lugar o término:\n" 

sNingunTermino = sLinea+"\n  No se encontraron terminos relacionados\n"+sLinea 

#bucle de entrada de programa


while bInicioPrograma: #mientras se cumpla la condición (bInicioPrograma=True) el bucle seguirá mostrando el programa ///cambio de condición al final///
    
    try: #try sirve como precaución, ya que es un excepción algorítmica. En caso no funcione alguna parte de nuestro código, el try omita el error para que el programa continúe. ///en caso de error, salta a la línea 172 ///

        sOpcion = str(input(sMensajeEntrada))

        #cuando la opcion es "a"
        if (sOpcion.lower() == "a"):

            #ingreso de palabra clave
            sEnfermedadIngresada = str(input(sMensajeLugar))
            sEnfermedadIngresada = sEnfermedadIngresada.upper()

            #almacenamiento de claves del diccionario
            lNombres = Centros.dCentrosMedicos.keys()

            #busqueda de termino de claves
            lParecidos = []
            
            #recorre todo el diccionario
            for sValor in lNombres:

                #verifica si el termino de busqueda se relaciona con los diccionarios
                if (sValor.find(sEnfermedadIngresada)>= 0): #el término ingresado busca en la clave, en caso no lo encuentre bota -1

                    #agrega a la lista de valores relacionados
                    lParecidos.append(sValor)
                    
                    #almacenamiento de claves
                    sDatos = (Centros.dCentrosMedicos[sValor].keys())
            #termina for

            #busqueda de posicion para busqueda de diccionario
            iPosicion = 0

            #verifica la existencia de resultados parecidos
            if (len(lParecidos)>0):

                #muestra mensaje de lugares
                print(sLinea)
                print((9*" ")+"Lugares relacionados")
                print(sLinea)

                #recorre todos los elementos del diccionario
                for sNombre in lParecidos:
                    print("("+str(iPosicion)+") "+sNombre+" - "+Centros.dCentrosMedicos[sNombre]["DISTRITO"])
                    iPosicion+=1

                #mensaje para ingreso de opcion de centro medico
                print(sLinea)
                iOpcion = int(input("Seleccione un centro medico por indice:\n"))

                #almacenamiento de datos de diccionario

                sDatos =(Centros.dCentrosMedicos[lParecidos[iOpcion]].keys())
                print(sLinea)
                print(lParecidos[iOpcion])
                print(sLinea)

                #recorremos diccionario en la clave seleccionada
                for sClave in sDatos: #sClave toma el valor de las claves (llaves) del subdiccionario de dCentrosMedicos 
                    print(sClave) #imprime el valor de las claves (llaves) del subdiccionario de dCentrosMedicos
                    print(Centros.dCentrosMedicos[lParecidos[iOpcion]][sClave]) #imprime los valores de las claves del subdiccionario dCentrosMedicos
                    print(sLinea)
                    
            #el termino de busqueda no tiene ninguna relacion con los diccionarios
            else:
                print(sNingunTermino)

        #cuando la opcion es "b"
        if (sOpcion.lower() == "b"):

            #ingreso de termino clave para busqueda
            sEnfermedadIngresada = str(input(sMensajeEnfermedad))
            sEnfermedadIngresada = sEnfermedadIngresada.upper()

            #devuelve las claves del diccionario de enfermedades
            lNombres = Diccionario.dEnfermedades.keys()

            #variable flat para verificar existencia
            lParecidos = []

            #recorre los elementos del diccionario
            for sValor in lNombres:

                #verifica si el termino de busqueda se relaciona con los diccionarios
                if (sValor.find(sEnfermedadIngresada)>= 0):

                    #agrega a la lista de valores relacionados
                    lParecidos.append(sValor)

                    #recolecta las claves del diccionario
                    sDatos =(Diccionario.dEnfermedades[sValor].keys())

            #verifica si existen resultados relacionados
            if (len(lParecidos)>0):

                #muestra de mensaje de enfermedades relacionadas
                iPosicion = 0
                print(sLinea)
                print((9*" ")+"Enfermedades relacionadas")
                print(sLinea)

                #imprime el indice de los valores relacionados
                for sNombre in lParecidos:
                    print("("+str(iPosicion)+") "+sNombre)
                    iPosicion+=1

                #muestra ls enfermedades
                print(sLinea)
                iOpcion = int(input("Seleccione la enfermedad por indice:\n"))

                #recolecta las claves del termino relacionado
                sDatos =(Diccionario.dEnfermedades[lParecidos[iOpcion]].keys())
                print(sLinea)
                print(lParecidos[iOpcion])
                print(sLinea)

                #recorrido del diccionario con la clave especifica
                for sClave in sDatos:

                  
                    #verifica si es la clave sintomas para enumerar los sintomas (línea - 148)
                    if(sClave == "SINTOMAS"):
                        print(sClave)
                        print("- ",end="")
                        
                        #reemplaza las ',' con salto de linea para enumerarlas
                        print(Diccionario.dEnfermedades[lParecidos[iOpcion]][sClave].replace(",","\n-"))
                        print(sLinea)
                    #termina el if enumerando los síntomas (línea - 156), si no estuviera; los síntomas aparecen como texto corrido                    

                    #muestra normalmente los elementos, no como los síntomas
                    else:
                        print(sClave)
                        print(Diccionario.dEnfermedades[lParecidos[iOpcion]][sClave])
                        print(sLinea)                       

            #muestra mensaje que no existe termino relacionado
            else:
                print(sNingunTermino)

        #cuando la opcion es "c"
        if (sOpcion.lower() == "c"):
            bInicioPrograma = False #deja de ejecutarse el programa
            break
            

    #captura los errores de los programas
    except:
        print("Error") #imprimirá "error" cuando ocurra un error durante la ejecución del programa y permitirá que continúe el bucle  





