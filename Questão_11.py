def fatorial(n):
    resultado=1
    for i in range(1,n+1):
        resultado*=i
    return resultado

numero=int(input("Digite um número inteiro para calcular o fatorial: "))

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")