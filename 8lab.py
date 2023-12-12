#Task 1
import requests

# 1.1 GET Request
post_id = 1  #отправляет запрос к серверу JSONPlaceholder для получения данных о задачеаписи

url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
response = requests.get(url)

if response.status_code >= 400:
    if 400 <= response.status_code < 500:
        print(f"Client Error: {response.status_code}")
    elif 500 <= response.status_code < 600:
        print(f"Server Error: {response.status_code}")
else:
    print("Response Content (JSON):")
    print(response.json())

# 1.2 Create ToDo Class
class ToDo: #определяется клаcc, который представляет собой представление задачи со свойствами
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# 1.3 Create a new object of class ToDo
json_data = response.json() #создает объект классана основе полученных данных из первого GET-запроса
new_todo = ToDo(json_data['userId'], json_data['id'], json_data['title'], json_data['completed'])

# 1.4 POST Request
new_todo_payload = { #создает новую задачу (ToDo) на сервере JSONPlaceholder, используя данные из только что созданного объекта ToDo
    "userId": new_todo.userId,
    "title": new_todo.title,
    "completed": new_todo.completed
}

post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo_payload)

if post_response.status_code >= 400:
    if 400 <= post_response.status_code < 500:
        print(f"Client Error: {post_response.status_code}")
    elif 500 <= post_response.status_code < 600:
        print(f"Server Error: {post_response.status_code}")
else:
    print("POST Response Content (JSON):")
    print(post_response.json())

# 1.5 Edit some data
# изменяет некоторые данные в объекте new_todo
new_todo.title = "New Title"

# 1.6 PUT Request
updated_todo_payload = { #происходит обновление выбранной задачи на сервере JSONPlaceholder. Используются измененные данные из объекта new_todo
    "userId": new_todo.userId,
    "id": new_todo.id,
    "title": new_todo.title,
    "completed": new_todo.completed
}

chosen_id = 1  

put_response = requests.put(f'https://jsonplaceholder.typicode.com/todos/{chosen_id}', json=updated_todo_payload)

if put_response.status_code >= 400:
    if 400 <= put_response.status_code < 500:
        print(f"Client Error: {put_response.status_code}")
    elif 500 <= put_response.status_code < 600:
        print(f"Server Error: {put_response.status_code}")
else:
    print("PUT Response Content (JSON):")
    print(put_response.json())



#Task 2: Character Exploration
import requests
import random
import json

# 2.1 Random Character Request
character_id = random.randint(1, 826)
character_url = f"https://rickandmortyapi.com/api/character/{character_id}"
response = requests.get(character_url)
character_data = response.json()

# 2.2 Response Output
print("JSON Response:")
print(json.dumps(character_data, indent=2))  # Print JSON response

print("\nKeys in the JSON structure:")
print(character_data.keys())  # Display keys in the JSON structure

# 2.3 Save to File
file_name = f"info_character_{character_id}.json"
with open(file_name, 'w') as file:
    json.dump(character_data, file, indent=2)  # Save JSON response to a file

# 2.4 Episode List
episode_urls = character_data['episode']
episode_ids = [int(url.split('/')[-1]) for url in episode_urls]

with open(f"all_episodes_with_character_{character_id}.txt", 'a') as episode_file:
    for url in episode_urls:
        episode_file.write(url + '\n')  # Append episode URLs to a file

# 2.5 Episode Response Structure
episode_example_url = "https://rickandmortyapi.com/api/episode/1"
episode_example_response = requests.get(episode_example_url).json()
print("\nEpisode Response Structure:")
print(json.dumps(episode_example_response, indent=2))

# 2.6 Episode Class Creation (to be done in a separate file)

# 2.7 Episode Data Retrieval
# Fetch data for each episode ID and create Episode objects

# 2.8 Class Methods (to be added to the Episode class)

# 2.9 Character Response Structure
character_example_url = "https://rickandmortyapi.com/api/character/1"
character_example_response = requests.get(character_example_url).json()
print("\nCharacter Response Structure:")
print(json.dumps(character_example_response, indent=2))

# 2.10 Character Class Creation (to be done in a separate file)

# 2.11 Character Object Creation (to be done after defining the Character class)

# 2.12 Character Class Methods (to be added to the Character class)

# 2.13 Result
# Show results, including printed responses, file creations, objects created, and methods utilized
