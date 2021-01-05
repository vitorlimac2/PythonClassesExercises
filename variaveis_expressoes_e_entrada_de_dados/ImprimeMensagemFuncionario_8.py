
nome_completo = input("Digite o nome completo: ")
email = input("Digite o email: ")

matricula = email.split("@")[0]

mensagem = "Funcionário: %s; Matrícula: %s; E-mail: %s" % (nome_completo, matricula,email)

print(mensagem)