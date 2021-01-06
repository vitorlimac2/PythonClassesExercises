
valor = float(input("Digite altura:"))
valores_lidos = 1

maiorValor = valor
menorValor = valor


## usando while

while valores_lidos <= 14:
    valor = float(input("Digite valor:"))
    if valor > maiorValor:
        maiorValor = valor
    if valor < menorValor:
        menorValor = valor
    valores_lidos = valores_lidos + 1

print("Menor %d: " % menorValor)
print("Maior %d: " % maiorValor)

## usando estrutura de repetição for e função range
## range(4) = [0,1, 2, 3]

for i in range(14): ## 14 porque eu já li o primeiro número
    valor = float(input("Digite valor:"))
    if valor > maiorValor:
        maiorValor = valor
    if valor < menorValor:
        menorValor = valor