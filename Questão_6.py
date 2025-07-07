def contador(inicial, final):
    if inicial <= final:
        return list(range(inicial, final + 1))
    else:
        return list(range(inicial, final - 1, -1))


inicio=int(input("Digite o número inicial: "))
fim=int(input("Digite o número final: "))

resultado=contador(inicio,fim)
print(resultado)