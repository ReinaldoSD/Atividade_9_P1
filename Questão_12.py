def contar_vogais(palavra):
    palavra=palavra.lower()
    vogais=['a','e','i','o','u']
    contador=0

    for letra in palavra:
        if letra in vogais:
            contador+=1
    return contador

n_de_vogais=input("Digite a palavra para que sejam contadas as vogais: ")
numero_de_vogais=contar_vogais(n_de_vogais)
print(f'O número de vogais da palavra digitada é: {numero_de_vogais}')