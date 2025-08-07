#1.Task: JSON Parsing
#write a Python script that reads the students.jon JSON file and prints details of each student.

import json
with open ('students.json') as f:
    data = json.load(f)
for each in data['students']:
    print(f"{each['name']} is {each['age']} years old and lives in {each['address']['city']}")

#2.
import requests
API_KEY= '6c22988c302d4f26916917f083a10820'
CITY = 'Tashkent'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']
    
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc}")
else:
    print("Error fetching weather data:", response.status_code)
    print("Response:", response.json())

#3
import json
import os

FILE_NAME = 'books.json'

# Load books from file or create new
def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_books(books):
    with open(FILE_NAME, 'w') as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author: ")
    book_id = max([b["id"] for b in books], default=0) + 1
    books.append({"id": book_id, "title": title, "author": author})
    save_books(books)
    print("Book added!")

# Update an existing book
def update_book():
    books = load_books()
    book_id = int(input("Enter book ID to update: "))
    for book in books:
        if book["id"] == book_id:
            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            save_books(books)
            print("Book updated!")
            return
    print("Book not found.")

# Delete a book
def delete_book():
    books = load_books()
    book_id = int(input("Enter book ID to delete: "))
    books = [book for book in books if book["id"] != book_id]
    save_books(books)
    print("Book deleted!")

# Menu
def menu():
    while True:
        print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

menu()
#4.
import requests
import random

API_KEY = 'your_omdb_api_key_here'

# Example genre list with movie titles
genre_movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "comedy": ["Superbad", "The Hangover", "Step Brothers"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "sci-fi": ["Inception", "Interstellar", "Blade Runner 2049"]
}

def recommend_movie():
    genre = input("Enter a movie genre (action, comedy, drama, sci-fi): ").lower()
    if genre not in genre_movies:
        print("Sorry, we don't have that genre.")
        return
    
    movie_title = random.choice(genre_movies[genre])
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_title}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            print(f"\n🎬 {data['Title']} ({data['Year']})")
            print(f"⭐ IMDb Rating: {data['imdbRating']}")
            print(f"📖 Plot: {data['Plot']}")
        else:
            print("Movie not found in OMDb.")
    else:
        print("Error fetching movie data.")

recommend_movie()

