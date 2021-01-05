salario = float(input("Digite o salário: "))
percentual_aumento = float(input("Digite a porcentagem de aumento do salário: "))

valor_aumento = salario * percentual_aumento/100

salario = salario + valor_aumento

print("Aumento do salário: %.2f" % valor_aumento)
print("Salário atualizado: %.2f" % salario)
