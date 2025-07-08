def numeros_primos(n):
    primos=[]
    for num in range(2, n + 1):
        eh_primo=True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return primos

numero_digitado=int(input("Digite um número para ser o limite de análise dos números primos: "))
numero_ser_primo=numeros_primos(numero_digitado)
print(f"Números primos até {numero_digitado}: {numero_ser_primo}")