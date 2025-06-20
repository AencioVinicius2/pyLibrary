"""
*args - Utilizamos ele quando não temos certeza de quantos arguments queremos ter numa função
- Os argumentos são passados como tuplas
**k
    for key, value in data.items():
        print("f")args - Além dos valores podemos passa também as repectivas chaves para cada argumento.
- Os argumentos são passados como um dicionário
"""
# 1 - Soma de números
def sum(num*)
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")
    
sum(7)

# 2 - Apresentação de curso

def apresentation(**data)
    for key, value in data.items():
        print(f"{key} - {value}")
        
print("Lista de cursos: ")
apresentation(name="Python",category="Backend",level="Iniciante")
apresentation(name="Visão computacional com python",category="IA",level="Avançado")
apresentation(name="Dashboards com Dash",category="Data Science",level="Intermediário")