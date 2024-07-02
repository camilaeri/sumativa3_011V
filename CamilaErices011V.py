import random
import csv
import os
clean="cls"
#INICIAMOS LISTAS
registros_csv=[]
ZONAS=["san bernardo", "calera de tango", "buin"]
pedidos=[["Nro. PEDIDO", "CLIENTE", "DIRECCIÒN", "SECTOR", "SACO 5KG", "SACO 10KG", "SACO 20KG"]]
#definimos una funcion para registrar pedidos
def registrar_pedido ():
    numero_pedido=random.randint(1,1000)
    while True:
        numero_pedido+=1
        nombre=input("Ingrese nombre y apellido de cliente: ")
        comuna=input("Ingrese direcciòn: ")
        
        while True:
            try:
                sector=input("Ingrese sector (San bernardo/Calera de tango/Buin): ").lower()
                if sector in ZONAS:
                    break
                else:
                    print("Sector invalido ingrese (San bernardo/Calera de tango/Buin)")
            except ValueError:
                print("Sector invalido ingrese (San bernardo/Calera de tango/Buin)")



        sacos_cinco=int(input("Ingrese cantidad de sacos de 5 kg: "))
        sacos_diez=int(input("Ingrese cantidad de sacos de 10 kg: "))
        sacos_veinte=int(input("Ingrese cantidad de sacos de 20 kg: "))
        
       


        nuevo_pedido=[numero_pedido, nombre, comuna, sector, sacos_cinco, sacos_diez, sacos_veinte]
        pedidos.append(nuevo_pedido)
        #creamos un diccionario para contenerlo en una lista para ser guardada en un archivo csv
        diccionario={
      
            "N pedido": numero_pedido,
            "Cliente": nombre,
            "Direccion": comuna,
            "Sector": sector,
            "Saco 5kg": sacos_cinco,
            "Saco 10kg": sacos_diez,
            "Saco 20kg": sacos_veinte
            
         }

        otro_pedido=int(input("Desea registrar otro pedido? 1=si 2=no \nOpcion: "))
        registros_csv.append(diccionario)
        if otro_pedido==2:
            break
        
      
#definimos una funcion para listar los pedidos
def listar_pedidos():
    for fila in pedidos:
        print(f"{fila[0]:>18}{fila[1]:>18}{fila[2]:>18}{fila[3]:>18}{fila[4]:>18}{fila[5]:>18}{fila[6]:>18}\n")   
#definimos una funcion para imprimir ruta segun sector 
def imprimir_ruta():
    print("Para imprimir ruta ingrese el sector a imprimir ")
    while True:      
        try:
                        
             sector_imprimir=input("San bernardo - Calera de Tango - Buin \nSector: ").lower()
             #definimos el nombre del archivo segun ruta elegida
             if sector_imprimir in ZONAS:
                if sector_imprimir=="san bernardo":
                    nombre_archivo="ruta_sanbernardo.txt"
                elif sector_imprimir=="buin":
                    nombre_archivo="ruta_buin.txt"
                elif sector_imprimir=="calera de tango":
                    nombre_archivo="ruta_calera.txt"
                #filtramos las filas correspondientes a la ruta elegida
                                 
                for fila in pedidos:
                    fila[3]==sector_imprimir
                    
                    archivo_imprimir=(f"{fila[0]:>15}{fila[1]:>15}{fila[2]:>15}{fila[3]:>15}{fila[4]:>15}{fila[5]:>15}{fila[6]:>15}")
                #creamos el archivo txt
                with open(nombre_archivo, "w") as archivo_txt:
                    archivo_txt.write(archivo_imprimir)
                print(f"Ruta guardada con exito, en archivo con el nombre: {nombre_archivo}")
                break
                
             else: 
                print("Sector ingresado no corresponde, intente otra vez")
        except ValueError:
            print("Sector ingresado no corresponde, intente otra vez")

#definimos el menu principal
otra_accion=1
while otra_accion==1:
                   
        
        while True:
            print("Bienvenido a CatPremium")
            print("1. Registrar pedidos")
            print("2. Listar todos los pedidos")
            print("3. Imprimir hoja de ruta")
            print("4. Salir del programa")
                
            try:
                opcion=int(input("Seleccione su opcion 1-4: "))

                os.system(clean)
                if opcion==1:
                    registrar_pedido()
                elif opcion==2:
                    listar_pedidos()
                elif opcion==3:
                    imprimir_ruta()
                elif opcion==4:
                    print("Has salido del programa, los pedidos registrados han sido guardados en el siguiente archivo: ")
                    with open("registros_pedidos.csv", "w", newline="") as archivo_csv:
                        escritor_csv=csv.writer(archivo_csv)
                        escritor_csv.writerow(registros_csv)

                    print("Nombre archivo: registros_pedidos.csv")

                
                    break
                else:
                    print("Opcion invalida, intente otra vez")
            except ValueError:
                print("Opcion invalida, intente otra vez") 

            otra_accion=int(input("Desea realizar otra accion? 1=si 2=no \nOpcion:  "))
            otra_accion=1
            os.system(clean)
            
        
    



