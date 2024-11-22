import json

# Leer el archivo output.jsonl con codificación utf-8
with open('output.jsonl', 'r', encoding='utf-8') as file:
    data = []
    for line in file:
        data.append(json.loads(line.strip()))

# Convertir los datos a una representación de escape Unicode
unicode_escaped_data = [json.dumps(item, ensure_ascii=True) for item in data]

# Guardar los datos convertidos en un nuevo archivo .jsonl
with open('output_unicode_escaped.jsonl', 'w', encoding='utf-8') as file:
    for item in unicode_escaped_data:
        file.write(item + '\n')