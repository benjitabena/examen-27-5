import requests
import json
import os

api_url = 'https://jsonplaceholder.typicode.com/posts/'

download_dir = 'Descargas'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Función para obtener las publicaciones desde la API
def get_posts():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_next_file_number(directory):
    existing_files = os.listdir(directory)
    if not existing_files:
        return 1
    else:
        numbers = [int(f.split('.')[0]) for f in existing_files if f.endswith('.json')]
        return max(numbers) + 1 if numbers else 1

# Obtener las publicaciones
posts = get_posts()

for post in posts:
    post_data = {
        'id': post['id'],
        'title': post['title'],
        'body': post['body']
    }

    post_json = json.dumps(post_data, indent=4)

    file_number = get_next_file_number(download_dir)
    file_name = f"{file_number}.json"
    file_path = os.path.join(download_dir, file_name)

    # Guardar el JSON en un archivo
    with open(file_path, 'w') as json_file:
        json_file.write(post_json)

    print(f"Guardado: {file_name}")
