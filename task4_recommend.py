import json

input = str(input('Введите полное название фильма: '))
with open('movies.json', 'r') as f:
    movies = json.loads(f.read())

budget = 0
for m in movies:
    if input.lower() == m['title']:
        budget = int(m['budget'])

for m in movies:
    if int(m['budget']) == budget:
        print(m['id'], m['title'], m['budget'])
