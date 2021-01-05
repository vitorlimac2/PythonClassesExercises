identificador = int(input("Digite o numero de identificação: "))

## ler as 3 notas

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

## ler a media dos exercicios

mp = float(input("Digite a média de pontuação das habilidades práticas: "))

## calcular a media de aproveitamento

media_ap = (nota1 + nota2 * 2 + nota3 * 3 + mp)/7

## verificar qual o conceito

if media_ap >= 90:
    conceito = "A"
    status = "aprovado"
elif media_ap >= 75:
    conceito = "B"
    status = "classificado"
elif media_ap >= 60:
    conceito = "C"
    status = "classificado"
elif media_ap >= 40:
    conceito = "D"
    status = "reprovado"
else:
    conceito = "E"
    status = "reprovado"

print("Identificação = %d\nMédia de aproveitamento = %f\nConceito = %s\nResultado = %s"
      % (identificador, media_ap, conceito, status))