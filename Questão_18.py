def senha_segura(senha):
  if len(senha) < 8:
    return False

  tem_maiuscula = False
  tem_minuscula = False
  tem_numero = False

  for caractere in senha:
    if caractere.isupper():
      tem_maiuscula = True
    elif caractere.islower():
      tem_minuscula = True
    elif caractere.isdigit():
      tem_numero = True

  return tem_maiuscula and tem_minuscula and tem_numero

senha_digitada = input("Digite a senha que deseja verificar: ")
resultado_verificacao = senha_segura(senha_digitada)
print(resultado_verificacao)