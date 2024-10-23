from time import sleep
import json
import os

def registro_Empleados():

    if os.path.exists('Empleados.json'):
        try:
            with open('Empleados.json', 'r') as file:
                empleado = json.load(file)
        except json.JSONDecodeError:
            empleado = {}
    else:
        empleado = {}

    
    id_Empleado = int(input("Ingrese el numero de indentificacion del empleado: "))        
    nombre = input("Ingrese el nombre del empleado: "), 
    cargo = input("Ingrese el cargo del empleado: "),
    salario = input("Ingrese el salario del empleado: ")

    empleado[id_Empleado] = {
        'Nombre' : nombre,
        'Cargo' : cargo,
        'Salario' : salario,
        'Inasistencias' : [],
        'Bonos' : []
        }

    with open('Empleados.json', 'w') as file:
        json.dump(empleado, file, indent=4)    

    print("Creando empleado")
    print("Espere un momento ...")
    sleep(1)
    print("Empleado creado con exito")

def registro_Inasistencias():

    id_Empleado = int(input("Ingrese el numero de indentificacion del empleado: "))
    fecha_Inasistencia = input("Ingrese la fecha en la que se presento la inasistencia (YYYY-MM-DD): ")
    
    with open('Empleados.json', 'r') as file:
            json.dump(empleado, file, indent=4)

    with open('Empleados.json', 'w') as file:
        json.dump(empleado, file, indent=4)

    for id_Empleado in Empleados :
        inasistencia["inasistencias"].append({
        "fecha_Inasistencia": fecha_Inasistencia })
        print("Registrando inasistencia")
        print("Espere un momento ...")
        sleep(1)
        print("Inasistencia registrada con exito")
    else:
        print("Empleado no registrado")
    

def registro_Bonos():
    id_Empleado = int(input("Ingrese el numero de indentificacion del empleado: "))
    fecha_Bono = input("Ingrese la fecha del bono a otorgar: ")
    valor_Bono = int(input("Ingrese el valor del bono otrogado al empleado: "))
    concepto_Bono = input("Ingrese el concepto del bono: ")
    for id_Empleado in Empleados :
        inasistencia["inasistencias"].append({
        "id_Empleado": id_Empleado,
        "fecha_Bono": fecha_Bono,
        "valor_Bono": valor_Bono,
        "concepto_Bono": concepto_Bono})
        print("Inasistencia registrada con exito")
    else:
        print("Empleado no registrado")
    print(f"Bono del empleado {nombre} registrado")