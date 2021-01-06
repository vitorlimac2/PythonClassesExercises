numero = int(input("Digite um número:"))

numeros_lidos = 0

soma = 0

while numero != 0:
    soma = soma + numero
    numeros_lidos = numeros_lidos + 1
    numero = int(input("Digite um número:"))

print(soma)

media_aritmetica = soma/numeros_lidos
print(media_aritmetica)