from gestion_Empleados import *
from nomina import *

while True:
    def menu():
            print("""
            ==========================================
            ========= Gestion de nomina ACME =========
            ==========================================
            =                                        =
            =   1. Registro de empleado              =  
            =   2. Registro de inasistencias         =
            =   3. Registro bonos extra legales      =  
            =   4. Nomina                            =
            =   0. Salir                             =  
            =                                        =  
            ==========================================
                """)
        
    menu()

    try:

        eleccion = int(input("Escoja un opcion: \n"))

    except ValueError:
        print("Ingrese solo valores numericos")
        continue

    if eleccion == 0:
        print("Gracias por utilizar el sistema de gestion de nomina - Acme")
        print("Saliendo del programa...")
        sleep(1)
        break

    elif eleccion == 1:        
        registro_Empleados()

    elif eleccion == 2:
        registro_Inasistencias()

    elif eleccion == 3:
        registro_Bonos()

    elif eleccion == 4:
        calculo_Nomina()
