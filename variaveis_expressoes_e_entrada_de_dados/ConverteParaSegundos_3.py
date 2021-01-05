# A questao nao especifica como os valores devem ser informados
# Entao foram lidos um a um

horas = float(input("Digite as horas: "))
minutos = float(input("Digite os minutos: "))
segundos = float(input("Digite os segundos: "))

## os parenteses foram utilizados apenas para organizar os valores
## a ordem de prioridade eh a multiplicacao primeiro de qualquer forma
segundos_totais = (horas * 60 * 60) + (minutos * 60) + segundos

print("Total de segundos = %d" % segundos_totais)