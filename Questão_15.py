def analisa_lista(lista):
    maior=max(lista)
    menor=min(lista)
    media=sum(lista)/len(lista)
    return maior,menor,media

def ler_lista():
    entrada=input("Digite os números da lista separados por vírgula: ")
    lista=[float(num.strip()) for num in entrada.split(",")]
    return lista

numeros=ler_lista()
maior,menor,media=analisa_lista(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média: {media:.2f}")