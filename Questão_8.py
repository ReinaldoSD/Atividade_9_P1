def repetir_mensagem(mensagem, numero):
    mensagens = []
    for _ in range(numero):
        mensagens.append(mensagem)
    return mensagens

mensagem_usuario = input("Digite a mensagem que deseja repetir: ")
numero_vezes = int(input("Digite a quantidade de vezes: "))

resultado = repetir_mensagem(mensagem_usuario, numero_vezes)

for msg in resultado:
    print(msg)
