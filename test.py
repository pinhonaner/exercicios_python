import requests

def search_books(title):
    url = f'https://openlibrary.org/search.json?q={title}'
    response = requests.get(url)
    data = response.json()
    return data['docs']

books = search_books('1984')
for book in books:
    print(f"{book['title']} by {', '.join(book['author_name'])}")
