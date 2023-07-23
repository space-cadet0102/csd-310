import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", password="P@ssw@rd123", database="movies", port="3307")


cursor=db.cursor()
cursor.execute("SELECT * FROM studio")
studio = cursor.fetchall()
for studio in studio:
	print("studio_id: {}\n studio_name:{}\n".format(studio[0], studio[1]))

cursor=db.cursor()
cursor.execute("SELECT * FROM genre")
genre = cursor.fetchall()
for genre in genre:
	print("genre_id: {}\n genre_name:{}\n".format(genre[0], genre[1]))

cursor=db.cursor()
cursor.execute("SELECT * FROM film WHERE film_runtime < 120")
film = cursor.fetchall()
for film in film:
	print("film_name: {}\n film_runtime:{}\n".format(film[1], film[3]))

cursor=db.cursor()
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
film = cursor.fetchall()
for film in film:
	print("film_name: {}\n film_director:{}\n".format(film[0], film[1]))