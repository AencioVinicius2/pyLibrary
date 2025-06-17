"""
Split, join, enumerate em Python
* Split - Dividir uma string #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista # iteráveis
"""

string = 'Python é uma ótima linguagem para dados Python'
lista_1 = string.split(' ')
voltas = 0

palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})')

string2 = 'O Brasil é penta'
lista = string2.split(' ')
string3 = ' - '.join(lista)

print(string2)
print(' t ')
print(lista)
print(string3)

print('-------------------------------------------------------------')

string4 = 'O flamengo ganhou'
lista3 = string4.split(' ')

print(string4)
print(lista3)
for indice, valor in enumerate(lista3):
    print(indice, valor)

print('-------------------------------------------------------------')

aPessoas = [
    [0,'JOAO'],
    [1,'MARIA'],
    [2,'LUIZ']
]

for indice, nome in aPessoas:
    print(indice,nome)

print('-------------------------------------------------------------')

aPessoas2 = ['Luiz', 'Pedro', 'Clara']

n1, n2, n3 = aPessoas2

print(n2)
