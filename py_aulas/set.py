filmes_set = {"Inception","The Shawshank Redemption","The Dark Origin"}

print(type(filmes_set))

print(len(filmes_set))

# - True e 1 são considerados o mesmo valor
example_set = {"Inception", True, 1, 8.7}
print(example_set)

print("--------------------------------------------")

filmes_set.update(example_set)
print(filmes_set)

filmes_set.remove(True)

filmes_set.remove(8.7)

print(filmes_set)

