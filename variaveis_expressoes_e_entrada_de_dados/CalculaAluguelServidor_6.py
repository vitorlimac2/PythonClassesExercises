### ler quantidade de dias de utilizacao

dias = float(input("Digite a quantidade de dias de utilização: "))
terabytes = float(input("Digite a quantidade de terabytes armazenado: "))

megabytes = terabytes * 1024 ** 2

valor = 40 * dias + 0.05 * megabytes

print("Valor a ser pago: R$ %.00f" % valor)

## valor a ser pago por 2 anos utilizando o servidor e ocupou 5 terabytes
## Valor a ser pago: R$ 291344

