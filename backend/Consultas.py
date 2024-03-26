import sqlite3

# Función para ver los registros de la base de datos
def ver_registro_por_id(id_a_buscar):
   
    conexion = sqlite3.connect('backend/database_Carreras.db') # Conectar a la base de datos
    cursor = conexion.cursor() # Crear un cursor para ejecutar consultas SQL

    # Obtener los registros de la tabla 'carreras' excluyendo el ID
    cursor.execute("SELECT Carreras, Descripcion FROM carreras WHERE id=?", (id_a_buscar,))
    registros = cursor.fetchall()
   
    if registros: # este lo puedes borrar no es necesario para el final del proyecto
    
    # Mostrar los registros
     for registro in registros:
        print()  # Espacio entre registros
        print("Carrera:", registro[0])
        print()  # Espacio entre registros
        print("Descripción:", registro[1])
        print()  # Espacio entre registros
    else: 
        print("Has llegado al límite de registros de las carreras.") 
    conexion.close() # Cerrar la conexión

# ID de ejemplo para buscar en la base de datos
id_carrera = 113  # Cambia esto con el ID que desees buscar

# Llamar a la función para ver el registro por el ID especificado
ver_registro_por_id(id_carrera)