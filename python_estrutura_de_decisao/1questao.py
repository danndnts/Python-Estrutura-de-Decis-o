#Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
#menor que 10. O programa deve escrever a mensagem correspondente (maior ou
#menor) e informar o valor digitado pelo usuário.
num1 = float(input("Digite o primeiro valor:"))
num2 = float(input("Digite o segundo valor:"))
if num1 > num2:
    print ("O valor {} é maior" .format(num1))
else:
    print ("O valor {} é maior" .format(num2))