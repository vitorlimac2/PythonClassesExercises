soma = 0
produto = 1


### loop infinito
while True:
    num = int(input("Digite número: "))

    ## observe a utilização do valor inteiro 0 (zero)
    ## como teste de condição que retorna um valor lógico.

    ## Python atribui valores booleanos para outros tipos.
    # Variáveis numéricas (inteiros e floats) com valor 0 (zero) são falsos
    # e não-nulos são positivos

    if not num:
        break

    if num % 2 == 0:
        soma = soma + num
    else:
        produto = produto * num

print(soma)
print(produto)