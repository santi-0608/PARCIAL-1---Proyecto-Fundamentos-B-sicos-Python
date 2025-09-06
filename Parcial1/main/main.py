"""
Archivo principal del proyecto
"""

import ui
import api

def main():
    print("=== Consulta de Variables Edáficas en Cultivos ===")

    # Obtener entradas del usuario
    departamento, municipio, cultivo, n_registros = ui.obtener_entrada_usuario()

    # Procesar datos usando API
    resultados = api.consultar_datos(departamento, municipio, cultivo, n_registros)

    # Mostrar resultados
    ui.mostrar_tabla(resultados)

if __name__ == "__main__":
    main()
