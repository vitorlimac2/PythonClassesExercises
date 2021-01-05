

cigarros_por_dia = int(input("Digite quantos cigarros por dia: "))
anos_de_fumante = int(input("Digite há quantos anos é fumante: "))

## calcula quantos minutos serão perdidos por dia para cada cigarro
estimativa_em_minutos = 10 * cigarros_por_dia * anos_de_fumante * 365

## converte a estimativa de minutos para dias
estimativa_em_dias = estimativa_em_minutos / 1440

print("Estimativa em dias perdidos de vida do fumante: %f" % estimativa_em_dias)