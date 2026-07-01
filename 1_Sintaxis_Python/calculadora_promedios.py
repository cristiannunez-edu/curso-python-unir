def ingresar_calificaciones():
    numero = 1
    salir = ''

    materias = []
    calificaciones = []

    while salir.lower() != "x":
        materia = input(f"Ingrese el nombre de la materia #{numero}: ")

        while len(materia.strip()) < 1:
            materia = input(f"El nombre de la materia no puede estar vacío. Ingrese el nombre de la materia #{numero}: ")

        calificación = input("Ingrese la calificación (0-10): ")

        # Validar calificación:
        calificación_es_válida = validar_calificación(calificación)

        while not calificación_es_válida:
            calificación = input(f"Ingrese una calificación (0-10): ")
            calificación_es_válida = validar_calificación(calificación)

        materias.append(materia)
        calificaciones.append(float(calificación))
        
        print(f"Materia \'{materia}\' con calificación \'{calificación}\' agregada correctamente. ✓  \n")

        numero += 1

        salir = input("Si desea continuar presione cualquier tecla; para salir presione la tecla [x]")
        
    print("Entrada de datos finalizada.")
    return materias, calificaciones

# Crea una función calcular_promedio(calificaciones) 
# que reciba una lista de calificaciones 
# y devuelva el promedio de todas ellas.
def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 1)

# Desarrolla una función determinar_estado(calificaciones, umbral) 
# que reciba la lista de calificaciones y un valor umbral (por defecto 5.0), 
# y devuelva dos listas: 
# una con los índices de las materias aprobadas y otra con los índices de las reprobadas.
def determinar_estado(calificaciones, umbral = 5.0):
    indices_aprobadas = []
    indices_reprobadas = []

    for index, cal in enumerate(calificaciones):
        if cal >= umbral:
            indices_aprobadas.append(index)
        else:
            indices_reprobadas.append(index)

    return indices_aprobadas, indices_reprobadas

# Implementa una función encontrar_extremos(calificaciones) 
# que identifique el índice de la calificación más alta
# y el índice de la más baja en la lista de calificaciones.
def encontrar_extremos(calificaciones):
    calificación_mayor = max(calificaciones)
    calificación_menor = min(calificaciones)
    
    indice_calificación_mayor = calificaciones.index(calificación_mayor)
    indice_calificación_menor = calificaciones.index(calificación_menor)
    
    return indice_calificación_mayor, indice_calificación_menor


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
    if not (0 <= float(calificación) <= 10):
        print("Calificación fuera del rango permitido.")
        return False

    return True

def mostrar_resultados(materias, calificaciones):
    # Muestra un resumen final que incluya:
    
    # Todas las materias con sus calificaciones
    print("\n[Materia]".ljust(30, ' '), '[Calificación]')
    for i, materia in enumerate(materias):
        print(materia.ljust(30, '.'), calificaciones[i])

    # El promedio general
    print(f"\nPROMEDIO GENERAL: {calcular_promedio(calificaciones)}")
    
    # Las materias aprobadas y reprobadas
    aprobadas, reprobadas = determinar_estado(calificaciones)
    print(f"\nMATERIAS APROBADAS: {len(aprobadas)}\n")
    for i in aprobadas:
        print(materias[i].title().ljust(30, '.'), calificaciones[i])

    print(f"\nMATERIAS REPROBADAS: {len(reprobadas)}\n")
    for i in reprobadas:
        print(materias[i].title().ljust(30, '.'), calificaciones[i])

    # La materia con mejor calificación y su valor
    indice_alto, indice_bajo = encontrar_extremos(calificaciones)
    print("\nMATERIA CON MEJOR CALIFICACIÓN")
    print(materias[indice_alto].title().ljust(30, '.'), calificaciones[indice_alto])

    # La materia con peor calificación y su valor
    print("\nMATERIA CON PEOR CALIFICACIÓN")
    print(materias[indice_bajo].title().ljust(30, '.'), calificaciones[indice_bajo])
    
    print("\n¡Muchas gracias por usar la Calculadora de Promedio Escolares! Nos vemos en otra ocasión")


def main():

    print("Bienvenido/a a la Calculadora de Promedios Escolares.")
    print("Empezaremos por digitar tus materias con su respectiva calificación.")
    
    materias, calificaciones = ingresar_calificaciones()
    
    if not materias or not calificaciones:
        print("No hay materias o calificaciones para procesar. Terminado el programa. Que pase feliz resto del día.")
        return
    
    mostrar_resultados(materias, calificaciones)

if __name__ == "__main__":
    main()