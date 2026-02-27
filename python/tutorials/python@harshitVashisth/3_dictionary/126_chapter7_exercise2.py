usr = {}

name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_movies = input("Enter your fav_movies separated by comma: ").split(",")
fav_songs = input("Enter your fav_songs separated by comma: ").split(",")

usr["name"] = name
usr["age"] = age
usr["fav_movies"] = fav_movies
usr["fav_songs"] = fav_songs

for key, value in usr.items():
    print(f"{key}: {value}")