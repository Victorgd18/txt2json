import os
import json

# Get a list of all files in the directory
path = '../Cuentos/clasicos'
files = os.listdir(path)

# Open the output file
with open('./output.jsonl', 'w', encoding='utf-8') as output_file:
    for file in files:
        # Only process .txt files
        if file.endswith('.txt'):
            # Read the story file
            with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
                cuento = f.read()

            # Replace line breaks with '\n'
            cuento = cuento.replace('\n', '\\n')
            # Obtain the name of the story from the file name. Example: 'blanca-nieves.txt' -> 'blanca nieves'
            title = file.replace('.txt', '').replace('-',' ')
            # Create the JSON format
            prompt  = f'Genera un cuento llamado {title}.'

            roleSystem = '{"role": "system", "content": "Eres un generador de cuentos para niños."}' 
            roleUser = '{"role": "user", "content": "'+prompt+'"}'
            roleAssistant = '{"role": "assistant", "content": "'+cuento+'"}'
            formato ='{"messages": ['+roleSystem+', '+roleUser+', '+roleAssistant+']}'

            # Convert the string to a Python dictionary
            formato_dict = json.loads(formato)
            # Convert to JSON format
            json_data = json.dumps(formato_dict, ensure_ascii=False)

            # Write the JSON data to the output file, followed by a newline
            output_file.write(json_data + '\n')

print('Conversion completed!')