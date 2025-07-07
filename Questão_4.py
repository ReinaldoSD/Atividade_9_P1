def media(num1,num2,num3):
    media=(num1+num2+num3)/3
    return media

num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
num3=float(input("Digite o terceiro número: "))
resultado=media(num1,num2,num3)

print(f"A média é {resultado}")