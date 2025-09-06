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
        return

    # Encabezados de la tabla
    headers = ["Departamento", "Municipio", "Cultivo", "Topografias", "Mediana pH", "Mediana P", "Mediana K"]

    # Imprimir encabezados con formato
    print("-" * 100)
    print(f"{headers[0]:<15} {headers[1]:<15} {headers[2]:<15} {headers[3]:<20} {headers[4]:<12} {headers[5]:<12} {headers[6]:<12}")
    print("-" * 100)

    # Imprimir filas
    for fila in resultados:
        med_ph = f"{fila['Mediana_pH']:.2f}" if fila['Mediana_pH'] is not None else "N/A"
        med_p  = f"{fila['Mediana_P']:.2f}"  if fila['Mediana_P'] is not None else "N/A"
        med_k  = f"{fila['Mediana_K']:.2f}"  if fila['Mediana_K'] is not None else "N/A"
        topografias = ", ".join(fila['Topografias']) if fila['Topografias'] else "N/A"

        print(f"{fila['Departamento']:<15} {fila['Municipio']:<15} {fila['Cultivo']:<15} {topografias:<20} {med_ph:<12} {med_p:<12} {med_k:<12}")

    print("-" * 100)
