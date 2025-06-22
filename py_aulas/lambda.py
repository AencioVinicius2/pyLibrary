power = lambda num: num ** 2

is_even = lambda x: x % 2 == 0

div_num = lambda x, y: x / y

reverse_string = lambda s: s[::-1]

movies_list = ["Titanic","The GodFather","Inception","Jurassic Park"]

ratings = {
    "Titanic":[8.5, 9.0, 7.5],
    "The GodFather":[9.5, 9.8, 8.0],
    "Inception":[8.0, 7.0, 8.5],
    "Jurassic Park":[8.8, 9.2, 8.5]
}

print(movies_list)
print(ratings)

print('-------------------------------------------------------------------------')

average_ratings = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name]) 

print(ratings["Inception"])
print(len(ratings["Inception"]))
print()

print(f"A media de avaliação do fime Inception: {average_ratings("Inception")}")


print('-------------------------------------------------------------------------')


check_movie = lambda movie_name: movie_name in movies_list

print(f"Inception está na lista? {check_movie("Inception")}")

print('-------------------------------------------------------------------------')

recommend_movie = lambda movie_name: f"Recomendo assistir o filme {movie_name} com média de {average_ratings(movie_name):.2f}"

print(f"{recommend_movie("Inception")}")