def soma_lista(lista):
    return sum(lista)

def ler_lista():
    entrada = input("Digite os números da lista que será analisada separados por vírgula: ")
    lista = [float(num.strip()) for num in entrada.split(",")]
    return lista

numeros = ler_lista()

resultado = soma_lista(numeros)
print(f"A soma dos números da lista é: {resultado}")