def dobro(a):
    dobro=a*2
    return dobro

def numero():
    numero=float(input("Digite um número: "))
    return numero

numero_digitado=numero()
dobro_do_n=dobro(numero_digitado)

print(f'O Dobro do número é: {dobro_do_n}')