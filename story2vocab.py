import os
from openai import OpenAI
import json

client = OpenAI()

# Directorio donde están los archivos de texto
dir_path = './Cuentos/todos/'

# JSON del Prompt
vocab_structure = {
        "palabras_complejas": ["ingenuo", "astuto", "desinteresado"],
        "sinonimos": {
            "ingenuo": ["crédulo", "inocente", "novato"],
            "astuto": ["sagaz", "perspicaz", "mañoso"],
            "desinteresado": ["altruista", "generoso", "desprendido"]
        }
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
                {"role": "system", "content": "Dado un cuento extraes 3 palabras dificiles y las colocas en un JSON con la siguiente estructura donde ademas te indico ejemplos de lo que puede ir en cada campo:" + json.dumps(vocab_structure) + " Ademas el JSON generado debe estar todo en una sola linea, no pongas saltos de linea. Asegurate que las palabras extraidas para el JSON deben estar en el cuento dado. Ademas estas palabras y sus sinonimos van a servir para mejorar la comprension lectora del que lea este cuento cosa que estas 3 palabras le serviran para entender mejor el cuento por ello las palabras deben ser las mas complejas del cuento dado. Esto es para niños de 10 años."},
                {"role": "user", "content": "Indica 3 palabras complejas sacadas del cuento anteriormente escrito, ademas 3 sinonimos por cada palabra en el formato JSON indicado:" + texto},
            ]
        )

        print(f'Archivo {i+1}: {respuesta.choices[0].message.content}')

        # Guardar la salida en un archivo JSON
        output_filename = os.path.splitext(filename)[0] + '.vocab.json'
        with open(os.path.join('./Vocabularios/', output_filename), 'w', encoding='utf-8') as file:
            json_data = json.dumps(respuesta.choices[0].message.content, ensure_ascii=False)
            file.write(json_data)