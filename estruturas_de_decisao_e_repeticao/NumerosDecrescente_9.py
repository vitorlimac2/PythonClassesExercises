num = int(input("Digite um número:"))

## criei uma variavel auxiliar apenas para não alterar o valor original da variável num.
aux = num
while aux > 0:
    print(aux)
    aux = aux - 1

## testando o for para imprimir uma sequência de números

## recupero o valor original de num
aux = num

## apesar que a estrutura for não tenha sido introduzida na aula
## de estrutura de repetição, ela também pode ser usada

for i in range(aux, 0, -1):
    print(i)