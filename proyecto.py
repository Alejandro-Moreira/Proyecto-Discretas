# Importa product para generar combinaciones binarias
from itertools import product

# Genera la tabla de verdad para n variables
# Devuelve una lista de tuplas con todas las combinaciones posibles de 0 y 1

def generar_tabla_verdad(n):
    return list(product([0, 1], repeat=n))

# Construye la expresión en forma SOP (Suma de Productos)
# tabla: lista de combinaciones binarias
# salidas: lista de salidas para cada combinación
# variables: lista de nombres de variables

def construir_SOP(tabla, salidas, variables):
    terminos = []
    for fila, salida in zip(tabla, salidas):
        if salida == 1:
            termino = []
            for var, val in zip(variables, fila):
                termino.append(var if val == 1 else f"{var}'")
            terminos.append(''.join(termino))
    return ' + '.join(terminos)

# Construye la expresión en forma POS (Producto de Sumas)
# tabla: lista de combinaciones binarias
# salidas: lista de salidas para cada combinación
# variables: lista de nombres de variables

def construir_POS(tabla, salidas, variables):
    terminos = []
    for fila, salida in zip(tabla, salidas):
        if salida == 0:
            termino = []
            for var, val in zip(variables, fila):
                termino.append(f"{var}'" if val == 1 else var)
            terminos.append('(' + ' + '.join(termino) + ')')
    return ' '.join(terminos)

# Solicita al usuario la salida para cada fila de la tabla de verdad
# Devuelve una lista de salidas (0 o 1) para cada combinación

def entrada_por_fila(tabla):
    salidas = []
    for fila in tabla:
        while True:
            entrada = input(f"{fila} -> ").strip()
            if entrada in ('0', '1'):
                salidas.append(int(entrada))
                break
            else:
                print("Entrada inválida. Solo se permite 0 o 1.")
    return salidas

# Función principal que controla el flujo del programa
# Permite al usuario ingresar una tabla de verdad, generar SOP/POS, y salir

def main():
    print("=== Generador de Expresiones Lógicas (SOP / POS) ===\n")
    while True:
        # Menú principal
        print("\nMenú principal:")
        print("1. Ingresar nueva tabla de verdad")
        print("2. Salir")
        opcion_menu = input(">>> ").strip()
        if opcion_menu == '2':
            print("¡Fin del programa!")
            break
        elif opcion_menu != '1':
            print("Opción inválida. Escriba 1 o 2.")
            continue

        # Solicita el número de variables y valida el rango
        while True:
            try:
                n = int(input("Ingrese el número de variables (2 a 5): "))
                if n < 2 or n > 5:
                    raise ValueError
                break
            except ValueError:
                print("Solo se permiten números enteros entre 2 y 5.")

        # Genera nombres de variables (A, B, C, ...)
        variables = [chr(65+i) for i in range(n)]  # ['A', 'B', 'C', ...]
        tabla = generar_tabla_verdad(n)
        total_filas = len(tabla)

        print("\nVariables:", variables)
        # Solicita la salida para cada fila de la tabla
        salidas = entrada_por_fila(tabla)

        # Submenú para elegir SOP, POS o volver al menú principal
        while True:
            print("\nSeleccione el tipo de expresión a generar:")
            print("1. SOP (Suma de productos)")
            print("2. POS (Producto de sumas)")
            print("3. Volver al menú principal")
            opcion = input(">>> ").strip()
            if opcion == '1':
                expresion = construir_SOP(tabla, salidas, variables)
                print("\nExpresión SOP:", expresion)
            elif opcion == '2':
                expresion = construir_POS(tabla, salidas, variables)
                print("\nExpresión POS:", expresion)
            elif opcion == '3':
                break
            else:
                print("Opción inválida. Escriba 1, 2 o 3.")
                continue

            # Muestra la tabla de verdad con encabezados
            print("\nTabla de Verdad:")
            print(' | '.join(variables) + ' | S')
            print('-' * (4 * len(variables) + 4))
            for fila, salida in zip(tabla, salidas):
                print(' | '.join(str(val) for val in fila) + f' | {salida}')

# Ejecuta el programa principal si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()