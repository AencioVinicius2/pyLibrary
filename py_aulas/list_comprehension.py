# 1 - Listando valores de 0 a 10 que seja menor que 4
lowers_than_4 = []

for i in range(10):
    if i <= 4:
        lowers_than_4.append(i)

print(lowers_than_4)

print("-------------------------------------------------------------------")
# 1 - Listando valores de 0 a 10 que seja menor que 4 com list comprehension
list_numbers = [i for i in range(10) if i < 4]
print(list_numbers)

# Lista de filmes
movies_list = ["Inception","The Shawshank Redemption","The Dark Origin"]

# 2 - Filmes que possuem a letra 'e' no título
movies_withE = [movie for movie in movies_list if 'e' in movie.lower()]
print(movies_withE)

# 3 - Filmes que eu assisti
moviesWatched = [movie for movie in movies_list if movie != "Jurassic Park"]
print(moviesWatched) 

# 4 - Encontrando filmes assistidos

while True:
    search_name = input("Digite o nome do filme para buscar na lista (ou sair para encerrar:\n")
    if search_name.lower() == 'sair':
        print("Programa encerrado")
        break
    
    found_movies = [movie for movie in movies_list if search_name.lower() in movie.lower()]
    print(f"O que retornou: { found_movies}")
    if found_movies:
        print(f"Filme(s) encontrado(s) com o nome: {search_name}:")
        for found_movie in found_movies:
            print(found_movie)
    else:   
        print(f"Nenhum filme foi encontrado com o nome {search_name}. Tente novamente!")