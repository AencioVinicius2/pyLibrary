# list
filmes_list = ["Titanic","The GodFather","Inception","Jurassic Park"]

print(filmes_list)

for filme in filmes_list:
    if filme == "Inception":
        break
    print(filme)


for filme in filmes_list:
    if filme == "Inception":
        continue
    print(filme)

print("------------------------------------------------------------------")

# Avaliação do filme
movie_name = input("Digite o nome do filme:\n")
movie_rating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
average = 0

for i in range(movie_rating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

if movie_rating > 0:
    average = total / movie_rating

print(f"Media de avaliação do filme {movie_name} é: {average:.2f}")

