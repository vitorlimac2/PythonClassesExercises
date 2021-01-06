soma = 0

numero = 3

while numero <= 500:
    if numero % 2 != 0 and numero % 3 == 0:
        soma = soma + numero
    numero = numero + 1

print(soma)