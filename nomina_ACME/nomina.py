def calculo_Nomina():

    salario_Minimo = 1000000
    id_Empleado = int(input("Ingrese el numero de indentificacion del empleado: "))

    for empleado in Empleados:
        salario = empleado["salario"]
        descuento_Salud = salario * 0.04
        descuento_Pension = salario * 0.04
        auxilio_Transporte = 0

    if salario < salario_Minimo * 2:
        auxilio_Transporte = salario * 0.10

    inasistencias = [falta for falta in inasistencias if falta ["id"] == empleado ["id"]]
    descuento_Inasistencias = (salario_Minimo / 30) * len(inasistencias)

    bonos_Empleado = [bono for bono in bonos if bono ["id"] == empleado ["id"]]
    total_Bonos = sum(bono["valor_bono"] for bono in bonos_Empleado)

    total_Nomina = salario - descuento_Salud - descuento_Pension - descuento_Inasistencias + auxilio_Transporte + total_Bonos

    info_Nomina = {
        "Numero de indentificacion" : empleado[id],
        "Nombre" : empleado[nombre],
        "Cargo" : empleado[cargo],
        "Salario" : salario,
        "Descuento por concepto salud" : descuento_Salud,
        "Descuento por concepto pension" : descuento_Pension,
        "Auxilio de transporte" : auxilio_Transporte,
        "Descuento por inasistencias" : descuento_Inasistencias,
        "Bonos extra" : total_Bonos,
        "Pago total de nomina" : total_Nomina
    }

