#Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
#negativo (considere o valor zero como positivo).
valor = float(input("Digite um valor real:"))
if valor >= 0:
    print("Seu valor é positivo!")
else:
    print("Seu valor é negativo!")