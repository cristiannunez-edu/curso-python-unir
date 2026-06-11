MATERIAS = []
CALIFICACIONES = []
CALIFICACIÓN_MÍNIMA = 0
CALIFICACIÓN_MÁXIMA = 10

def ingresar_calificaciones():
    numero = 1
    salir = ''

    while salir.lower() != "x":
        materia = input(f"Ingrese el nombre de la materia #{numero}: ")

        while len(materia.strip()) < 1:
            materia = input(f"El nombre de la materia no puede estar vacío. Ingrese el nombre de la materia #{numero}: ")

        calificación = input("Ingrese la calificación (0-10): ")

        # Validar calificación vacía:
        calificación_es_válida = validar_calificación(calificación)

        while not calificación_es_válida:
            calificación = input(f"Ingrese una calificación (0-10): ")
            calificación_es_válida = validar_calificación(calificación)

        MATERIAS.append(materia)
        CALIFICACIONES.append(float(calificación))
        
        print(f"Materia \'{materia}\' con calificación \'{calificación}\' agregada correctamente. ✓  \n")

        numero += 1

        salir = input("Si desea finalizar presione la tecla [x] y cualquier otra tecla para continuar. ")
        
    print("Entrada de datos finalizada.")
    return MATERIAS, CALIFICACIONES


def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)

def determinar_estado(calificaciones, umbral = 5.0):
    indices_aprobadas = []
    indices_reprobadas = []

    for index, cal in enumerate(calificaciones):
        if cal >= umbral:
            indices_aprobadas.append(index)
        else:
            indices_reprobadas.append(index)

    return indices_aprobadas, indices_reprobadas

def encontrar_extremos(calificaciones):
    # return min(calificaciones), max(calificaciones)
    indice_mas_alto = 0
    indice_mas_bajo = 0
    calificacion_mas_baja = 0
    calificacion_mas_alta = 0

    for index, cal in enumerate(calificaciones):
        if index == 0:
            calificacion_mas_alta = cal
            calificacion_mas_baja = cal
            indice_mas_alto = index
            indice_mas_bajo = index
        else:
            if cal > calificacion_mas_alta:
                calificacion_mas_alta = cal
                indice_mas_alto = index
            
            if cal < calificacion_mas_baja:
                calificacion_mas_baja = cal
                indice_mas_bajo = index

    return indice_mas_alto, indice_mas_bajo

def validar_calificación(calificación):
    # Verificar si la calificación está vacía:
    if len(calificación.strip()) < 1:
        print("La calificación no puede estar vacía.")
        return False

    # Verificar si la calificación no es numérica:
    if not calificación.isnumeric():
        print("La calificación debe ser un número.")
        return False

    # Verificar si la calificación está fuera del rango permitido
    if CALIFICACIÓN_MÍNIMA < float(calificación) > CALIFICACIÓN_MÁXIMA:
        print("Calificación fuera del rango permitido.")
        return False

    return True

def mostrar_resultados():
    print("[Materia]".ljust(30, ' '), '[Calificación]')
    for i, materia in enumerate(MATERIAS):
        print(materia.title().ljust(30, '.'), CALIFICACIONES[i])

    print(f"\n\nPROMEDIO GENERAL: {calcular_promedio(CALIFICACIONES)}")
    
    aprobadas, reprobadas = determinar_estado(CALIFICACIONES)
    print(f"\n\nMATERIAS APROBADAS: {len(aprobadas)}\n")
    for i in aprobadas:
        print(MATERIAS[i].title().ljust(30, '.'), CALIFICACIONES[i])

    print(f"\n\nMATERIAS REPROBADAS: {len(reprobadas)}\n")
    for i in reprobadas:
        print(MATERIAS[i].title().ljust(30, '.'), CALIFICACIONES[i])

    indice_alto, indice_bajo = encontrar_extremos(CALIFICACIONES)
    print("\n\nMATERIA CON MEJOR CALIFICACIÓN")
    print(MATERIAS[indice_alto].title().ljust(30, '.'), CALIFICACIONES[indice_alto])

    print("\n\nMATERIA CON PEOR CALIFICACIÓN")
    print(MATERIAS[indice_bajo].title().ljust(30, '.'), CALIFICACIONES[indice_bajo])

def main():
    print("Bienvenido/a a la Calculadora de Promedios Escolares.\n\nEmpezaremos por digitar tus materias con su respectiva calificación. Puedes digitar las materias que quieras.\nCuando termines, presiona la tecla [ESC] para finalizar la entrada de datos.\n\n¡Así que empecemos! ")
    materias, calificaciones = ingresar_calificaciones()

    mostrar_resultados()

if __name__ == "__main__":
    main()