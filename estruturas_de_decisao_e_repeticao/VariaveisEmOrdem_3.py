#### ler variavel A

a = int(input("Digite variavel A:"))

### ler variavel B

b = int(input("Digite variavel B:"))

#### variavel que recebe valor temporario
auxiliar = 0

if a > b:
    auxiliar = a
    a = b
    b = auxiliar

### imprime A e B
print("Variavel A %d" % a)
print("Variavel B %d" % b)