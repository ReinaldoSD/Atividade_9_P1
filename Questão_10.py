def maior_numero(a,b,c):
    maior_numero=max(a,b,c)
    return maior_numero

num1=float(input("Digite um número: "))
num2=float(input("Digite outro número: "))
num3=float(input("Digite mais um número: "))

resultado=maior_numero(num1,num2,num3)
print(f'O maior número entre os digitados é: {resultado}')