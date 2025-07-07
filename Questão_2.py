def saudacao(nome):
    print(f"Olá, {nome}!")
def pegar_nome():
    nome=input("Digite um nome: ")
    return nome

pessoa=pegar_nome()
saudacao(pessoa)