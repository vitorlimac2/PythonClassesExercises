num = int(input("Digite o número: "))

### testar se está entre dois números quaisquer
limiteInferior = int(input("Digite o limite inferior: "))
limiteSuperior = int(input("Digite o limite superior: "))

## verificar a ordem que foram digitados os números
if limiteInferior > limiteSuperior:
    aux = limiteInferior
    limiteInferior = limiteSuperior
    limiteSuperior = aux

if num > limiteInferior and num < limiteSuperior:
    print("Sim! Está %d entre %d e %d!" % (num,limiteInferior,limiteSuperior))