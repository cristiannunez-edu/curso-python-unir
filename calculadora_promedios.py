"""
Calculadora de Promedios Escolares.

Este programa permite al usuario ingresar nombres de materias y sus 
calificaciones, calcula el promedio general, determina el estado 
(aprobado/reprobado) de cada materia e identifica los extremos 
(mejor y peor calificación).

Desarrollado por Cristian Silverio Nuñez Mata
"""

def ingresar_calificaciones():
    """
    Solicita al usuario el nombre de materias y sus calificaciones.

    Utiliza un bucle while para permitir la entrada de múltiples registros 
    hasta que el usuario decida terminar. Valida que la calificación esté 
    dentro del rango permitido (0-10).

    Returns:
        tuple: (materias, calificaciones) donde 'materias' es una lista de 
                strings y 'calificaciones' una lista de floats.
    """
    numero = 1
    salir = ''

    materias = []
    calificaciones = []

    while salir.lower() != "x":
        materia = input(f"Ingrese el nombre de la materia #{numero}: ")

        while len(materia.strip()) < 1:
            materia = input("El nombre de la materia no puede estar vacío. Intente de nuevo ")

        calificacion = input("Ingrese la calificacion (0-10): ")

        # Validar calificacion:
        calificacion_es_válida = validar_calificacion(calificacion)

        while not calificacion_es_válida:
            calificacion = input("Ingrese una calificacion (0-10): ")
            calificacion_es_válida = validar_calificacion(calificacion)

        materias.append(materia)
        calificaciones.append(float(calificacion))

        print(f"Materia \'{materia}\' con calificacion \'{calificacion}\' agregada correctamente.")

        numero += 1

        salir = input("Para continuar presione cualquier tecla; para salir presione la tecla [x]")

    print("Entrada de datos finalizada.")
    return materias, calificaciones

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Args:
        calificaciones (list): Lista de números.

    Returns:
        float: El promedio de los valores ingresados.
    """
    return round(sum(calificaciones) / len(calificaciones), 1)

def determinar_estado(calificaciones, umbral = 5.0):
    """
    Clasifica las materias según su calificación respecto al umbral de 5.0.

    Args:
        calificaciones (list): Lista con las calificaciones de las materias.

    Returns:
        tuple: (aprobadas, reprobadas) conteniendo los índices de las 
                posiciones en la lista original.
    """
    indices_aprobadas = []
    indices_reprobadas = []

    for index, cal in enumerate(calificaciones):
        if cal >= umbral:
            indices_aprobadas.append(index)
        else:
            indices_reprobadas.append(index)

    return indices_aprobadas, indices_reprobadas

def encontrar_extremos(calificaciones):
    """
    Identifica los índices de las calificaciones más alta y más baja.

    Args:
        calificaciones (list): Lista de calificaciones.

    Returns:
        tuple: (indice_calificacion_mayor, indice_calificacion_menor) 
                correspondientes a la mejor y peor nota.
    """
    calificacion_mayor = max(calificaciones)
    calificacion_menor = min(calificaciones)

    indice_calificacion_mayor = calificaciones.index(calificacion_mayor)
    indice_calificacion_menor = calificaciones.index(calificacion_menor)

    return indice_calificacion_mayor, indice_calificacion_menor


def validar_calificacion(calificacion):
    """
    Verifica si el valor ingresado es un número válido entre 0 y 10.

    Args:
        calificación (str): El valor capturado mediante input.

    Returns:
        bool: True si es válida, False en caso contrario.
    """
    # Verificar si la calificacion está vacía:
    if len(calificacion.strip()) < 1:
        print("La calificacion no puede estar vacía.")
        return False

    try:
        # Intentar convertir a float para aceptar decimales
        valor = float(calificacion)

        # Verificar el rango permitido
        if not 0 <= valor <= 10:
            print("Calificación fuera del rango permitido (0-10).")
            return False

    except ValueError:
        # Si la conversión falla, significa que no es un número válido
        print("La calificación debe ser un número válido.")
        return False

    return True

def mostrar_resultados(materias, calificaciones):
    """Muestra un resumen final con los datos digitados y procesados

    Args:
        materias (list): lista con los nombres de las materias
        calificaciones (list): lista con las calificaciones
    """

    # Todas las materias con sus calificaciones
    print("\n[Materia]".ljust(30, ' '), '[Calificacion]')
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

    # La materia con mejor calificacion y su valor
    indice_alto, indice_bajo = encontrar_extremos(calificaciones)
    print("\nMATERIA CON MEJOR CALIFICACIoN")
    print(materias[indice_alto].title().ljust(30, '.'), calificaciones[indice_alto])

    # La materia con peor calificacion y su valor
    print("\nMATERIA CON PEOR CALIFICACIoN")
    print(materias[indice_bajo].title().ljust(30, '.'), calificaciones[indice_bajo])
    print("\n¡Muchas gracias por usar la Calculadora de Promedio Escolares!")

def main():
    """Función principal que invoca a la función ingresar_calificaciones y 
    """
    print("Bienvenido/a a la Calculadora de Promedios Escolares.")
    print("Empezaremos por digitar tus materias con su respectiva calificacion.")

    materias, calificaciones = ingresar_calificaciones()

    if not materias or not calificaciones:
        print("No hay materias o calificaciones para procesar. Que pase feliz resto del día.")
        return

    mostrar_resultados(materias, calificaciones)

if __name__ == "__main__":
    main()
