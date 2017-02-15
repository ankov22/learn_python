import json

input = input('Введите название фильма: ')
with open('movies.json', 'r') as f:
    movies = json.loads(f.read())

for m in movies:
    if input in str(m['title']).lower():
        print(m['id'], m['title'])
