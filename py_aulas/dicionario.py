import pprint

filme_inception = {
    "Inception": {
    "year_release": 2010,
    "imdb_rating": 8.8,
    "genere": ["Sci-fi","Action","Thriller"]
    },
}
filmes_dic = {
    "Inception": {
    "year_release": 2010,
    "imdb_rating": 8.8,
    "genere": ["Sci-fi","Action","Thriller"]
    },
    "Interestellar": {
    "year_release": 2014,
    "imdb_rating": 8.6,
    "genere": ["Sci-fi","Drama"  ]
    },
    "The dark knight": {
    "year_release": 2008,
    "imdb_rating": 9.0,
    "genere": ["Sci-fi","Action","Crime"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmes_dic)    

print("---------------------------")
print(filmes_dic["Interestellar"]["genere"])

print(filme_inception)

print(len(filme_inception))

print(type(filme_inception))

# 1 Recuperar um elemento do dicionario

print(filme_inception["Inception"]["genere"])
print(filme_inception.get("imdb_rating"))

# 1 Buscar apenas a chave do dicionario

print(filme_inception.keys())

# Buscar apenas os valores do dicionario

print(filme_inception.values())

# Buscar itens do dicionario com chave e valor

print(filme_inception.items())

# Adicionar itens no dicionario

filme_inception["Inception"]["director"] = "Christopher Nolan"
print(filme_inception)

# Atualizar itens no direcionario

#   filme_inception({"imdb_rating": 8.7})
