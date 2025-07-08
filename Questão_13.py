def palindromo(palavra):
    palavra=palavra.lower()
    return palavra==palavra[::-1]

palavra=input("Digite uma palavra para verificar se ela é palindromo: ")
palavras_palindromo=palindromo(palavra)

if palavras_palindromo:
    print(True)
else:
    print(False)
