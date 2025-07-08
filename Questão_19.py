import random

def jogo_adivinhacao(numero_secreto):
    while True:
        n_usuario = int(input("Digite seu palpite: "))

        if n_usuario < numero_secreto:
            print("O número é maior que isso.")
        elif n_usuario > numero_secreto:
            print("O número é menor que isso.")
        else:
            print(f'Parabéns! Você acertou, o número secreto é o {n_usuario}.')
numero_sorteado=random.randint(0,100)        
tentativa=jogo_adivinhacao(numero_sorteado)
print(tentativa)
