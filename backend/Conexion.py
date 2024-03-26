from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS desde flask_cors
import sqlite3

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes desde cualquier origen

# Ruta para recibir las respuestas del usuario y devolver las carreras recomendadas
@app.route('/recibir-respuestas', methods=['POST'])
def recibir_respuestas():
    # Obtener las respuestas del cuerpo de la solicitud
    respuestas = request.json

    # Realizar la lógica del sistema experto para determinar las carreras recomendadas
    carreras_recomendadas = logica_sistema_experto(respuestas)

    # Devolver las carreras recomendadas al frontend
    return jsonify(carreras_recomendadas)

# Función para la lógica del sistema experto
def logica_sistema_experto(respuestas):
    # Aquí puedes implementar la lógica del sistema experto para analizar las respuestas y determinar las carreras recomendadas
    
    # Conexión a la base de datos
    conexion = sqlite3.connect('backend/database_Carreras.db')
    cursor = conexion.cursor()

    # Inicializar un diccionario para almacenar las coincidencias de cada carrera
    coincidencias = {}

    # Iterar sobre cada carrera en la base de datos
    cursor.execute('SELECT Carreras, Descripcion FROM carreras')
    carreras = cursor.fetchall()
    for carrera, descripcion in carreras:
        # Inicializar el contador de coincidencias para esta carrera
        contador_coincidencias = 0
        
        # Comparar las respuestas del usuario con la descripción de esta carrera
        for pregunta, respuesta_usuario in respuestas.items():
            # Si la respuesta del usuario coincide con alguna parte de la descripción de la carrera,
            # aumentar el contador de coincidencias
            if respuesta_usuario.lower() in descripcion.lower():
                contador_coincidencias += 1
        
        # Almacenar el contador de coincidencias de esta carrera en el diccionario
        coincidencias[carrera] = {'descripcion': descripcion, 'coincidencias': contador_coincidencias}

    # Cerrar la conexión a la base de datos
    conexion.close()

    carreras_recomendadas = [{'nombre': carrera, 'descripcion': coincidencias[carrera]['descripcion']} 
        for carrera in sorted(
            coincidencias, key=lambda x: coincidencias[x]['coincidencias'], reverse=True)[:3]] # Devolver las tres carreras con más coincidencias

    # Devolver las carreras recomendadas
    return carreras_recomendadas

if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación Flask en modo de depuración


