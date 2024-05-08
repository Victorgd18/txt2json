import os
import json

# Get a list of all files in the directory
path = './Cuentos/todos'
files = os.listdir(path)

# Open the output file
with open('./output.jsonl', 'w', encoding='utf-8') as output_file:
    for file in files:
        # Only process .txt files
        if file.endswith('.txt'):
            # Read the story file
            with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
                cuento = f.read()

            # Obtain the name of the story from the file name. Example: 'blanca-nieves.txt' -> 'blanca nieves'
            title = file.replace('.txt', '')
            titleStory = file.replace('.txt', '').replace('-', ' ').capitalize()
            
            # Read the prompt from the corresponding .prompt.json file
            with open(f'./Prompts/{title}.prompt.json', 'r', encoding='utf-8') as f:
                prompt = json.load(f)

            # Read the vocabulary from the corresponding .vocab.json file
            # with open(f'./Vocabularios/{title}.vocab.json', 'r', encoding='utf-8') as f:
            #     vocabulario = json.load(f)

            # Create the JSON format
            roleSystem = {"role": "system", "content": "Eres un generador de cuentos para niños en español que toma en cuenta un JSON con las características de un cuento y en base a ello genera un cuento creativo e interesante. Además primero pones el titulo del cuento luego inmediatamente el caracter '&', y luego el cuento. Ejemplo: Titulo&TodoElcuento…"}
            roleUser = {"role": "user", "content": prompt}
            roleAssistant = {"role": "assistant", "content": titleStory + '&' + cuento}
            formato = {"messages": [roleSystem, roleUser, roleAssistant]}
            
            # Convert to JSON format
            json_data = json.dumps(formato, ensure_ascii=False)
            
            # Write the JSON data to the output file, followed by a newline
            output_file.write(json_data + '\n')

print('Conversion completed!')