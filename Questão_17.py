import random

def simular_dado(n):
    resultados = []
    for _ in range(n):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

n = int(input("Quantas vezes deseja rolar o dado de 6 lados? "))

resultados = simular_dado(n)

print(f"Resultados das {n} rolagens:")
print(resultados)