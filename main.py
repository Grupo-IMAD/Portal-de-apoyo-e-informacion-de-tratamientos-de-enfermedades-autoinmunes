#importacion de modulos 
import DiccionariosEnfermedades as Diccionario 
import DiccionariosCentrosMedicos as Centros 
#as es para llamar de otra forma a los módulos
#las letras antepuestas en las variables indican el tipo de dato
#creacion de variables globales 
        #\n —> salto de linea  

bInicioPrograma = True

sLinea = ("-"*43)

sMensajeEntrada = (" "*7)+"Portal de apoyo e información\nde tratamientos de enfermedades autoinmunes\n"+sLinea+"\n"+(" "*13)+"Ingrese la opción\n"+sLinea+"\n(a) Buscar centros medicos\n(b) Informacion de enfermedades autoinmunes\n(c) Salir\n" 

sMensajeEnfermedad = "Ingrese una enfermedad o un termino:\n" 

sMensajeLugar = "Ingrese un lugar o término:\n" 

sNingunTermino = sLinea+"\n  No se encontraron terminos relacionados\n"+sLinea 

#bucle de entrada de programa
while bInicioPrograma: #mientras se cumpla la condición (bInicioPrograma=True) el bucle seguirá mostrando el programa ///cambio de condición al final///

    try: # try sirve como precaución, ya que es un excepción. En caso no funcione alguna parte de nuestro código, el try omite el error para que el programa continúe. ///en caso de error, salta a la línea 156 ///

        sOpcion = str(input(sMensajeEntrada))

        #cuando la opcion es "a"
        if (sOpcion.lower() == "a"):

            #ingreso de palabra clave
            sEnfermedadIngresada = str(input(sMensajeLugar))
            sEnfermedadIngresada = sEnfermedadIngresada.upper() #convierte las minusculas del input en mayusculas

            #almacenamiento de claves del diccionario
            lNombres = Centros.dCentrosMedicos.keys()

            #busqueda de termino de claves
            lParecidos = []
            
            #recorre todo el diccionario
            for sValor in lNombres:

                #verifica si el termino de busqueda se relaciona con los diccionarios
                if (sValor.find(sEnfermedadIngresada)>= 0): #el término ingresado busca en la clave, en caso no lo encuentre bota -1

                    #agrega a la lista de valores relacionados de las llaves del diccionario dCentrosMedicos
                    lParecidos.append(sValor)
                    
                    #almacenamiento de claves, sDatos adquiere las llaves del subdiccionario del diccionario dCentrosMedicos dependiendo de lo que valga sValor
                    sDatos = (Centros.dCentrosMedicos[sValor].keys())
            
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

                        print(sClave)
                        print(Diccionario.dEnfermedades[lParecidos[iOpcion]][sClave])
                        print(sLinea)                       

            #muestra mensaje que no existe termino relacionado
            else:
                print(sNingunTermino)

        #cuando la opcion es "c"
        if (sOpcion.lower() == "c"):
            bInicioPrograma = False #cuando es falso, el programa termina. Esto es para cuando el usuario quiera dejar de usarlo.
            break
            
    #captura los errores de los programas
    except:
        print("Error")





