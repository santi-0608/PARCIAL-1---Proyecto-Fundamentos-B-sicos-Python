"""
Módulo de interfaz de usuario (UI).
Contiene funciones para interactuar por consola.
"""

def obtener_entrada_usuario():
    departamento = input("Ingrese el Departamento: ")
    municipio = input("Ingrese el Municipio: ")
    cultivo = input("Ingrese el Cultivo: ")
    n_registros = int(input("Ingrese el número de registros a consultar: "))
    return departamento, municipio, cultivo, n_registros

def mostrar_tabla(resultados):
    print("\n=== Resultados de la consulta ===")
    if not resultados:
        print("No se encontraron registros.")
    else:
        for fila in resultados:
            print(fila)
