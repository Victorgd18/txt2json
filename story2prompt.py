import os
from openai import OpenAI
import json

client = OpenAI()

# Directorio donde están los archivos de texto
dir_path = './Cuentos/nuevos/'

# JSON del Prompt
story_structure = {
    "genero": "terror, comedia, ciencia ficcion, etc",
    "escenario": "",
    "personajes": [
        {
            "nombre": "",
            "tipo": "niño, animal, fantasma, etc.",
            "rasgos": ["", ""],
            "rol": "principal o secundario",
            "caracterstica_especial": ["", ""]
        },
        {
            "nombre": "",
            "tipo": "",
            "rasgos": ["", ""],
            "rol": ""
        }
    ]
}

# Iterar sobre todos los archivos en el directorio
for i, filename in enumerate(os.listdir(dir_path)):
    if filename.endswith('.txt'):
        # Leer el archivo de texto
        with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as file:
            texto = file.read()

        # Realizar la solicitud a la API de OpenAI
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "Dado un cuento extraes sus caracteristicas y las colocas en un JSON para un futuro prompt con la siguiente estructura donde ademas te indico ejemplos de lo que puede ir en cada campo:" + json.dumps(story_structure) + " Ademas el JSON generado debe estar todo en una sola linea, no pongas saltos de linea."},
                {"role": "user", "content": "Genera el prompt de las caracteristicas del siguiente cuento en el formato JSON indicado:" + texto},
            ]
        )

        print(f'Archivo {i+1}: {respuesta.choices[0].message.content}')

        # Guardar la salida en un archivo JSON
        output_filename = os.path.splitext(filename)[0] + '.prompt.json'
        with open(os.path.join('./Prompts/', output_filename), 'w', encoding='utf-8') as file:
            json_data = json.dumps(respuesta.choices[0].message.content, ensure_ascii=False)
            file.write(json_data)