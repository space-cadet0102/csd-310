import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", password="P@ssw@rd123", database="movies", port="3307")

def show_films(cursor, title):
    cursor.execute("select film_name as 'Name', film_director as 'Director', genre_name as 'Genre', studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()
    print("\n -- {} --".format("title"))
    for film in films:
        print("Film Name: {} \nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))