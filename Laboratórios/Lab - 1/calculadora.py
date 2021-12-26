# Calculadora em Python
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    return x / y

def multiplicacao(x, y):
    return x * y

print("*************** Python Calculator ***************")
print("Selecione o número da operação desejada: ")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
opcao = int(input("Escolha sua opção (1/2/3/4): "))
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
if(opcao==1):
    print("%d + %d = %d" %(x, y, soma(x, y)))
elif(opcao==2):
    print("%d - %d = %d" %(x, y, subtracao(x, y)))
elif(opcao==3):
    print("%d * %d = %d" %(x, y, multiplicacao(x, y)))
elif(opcao==4):
    print("%d / %d = %.1f" %(x, y, divisao(x, y)))
else:
    print("Opção inválida")
