def intercalar_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        print("Erro: As listas devem ter o mesmo tamanho para serem intercaladas.")
        return None
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

    return lista_intercalada

entrada1 = input("Digite os elementos da primeira lista, separados por vírgula: ")
entrada2 = input("Digite os elementos da segunda lista, separados por vírgula: ")

lista1 = [item.strip() for item in entrada1.split(",")]
lista2 = [item.strip() for item in entrada2.split(",")]

resultado = intercalar_listas(lista1, lista2)

if resultado is not None:
    print("Lista intercalada:", resultado)