## ler o valor em nanograma

nanograma = float(input("Digite o valor em nanogramas: "))

## converte

micrograma = nanograma * 0.001

print("Valor em nanograma = %.4f" % nanograma)
print("Convertido para micrograma = %.4f" % micrograma)