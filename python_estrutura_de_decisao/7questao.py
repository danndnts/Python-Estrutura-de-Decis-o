#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
#calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
#testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
#senão escrever a mensagem 'Saldo Negativo'.

nmr = int(input('Digite o número da conta do cliente: '))
sal = float(input('Digite o saldo atual da conta: '))
deb = float(input('Digite o valor do débito: '))
cred = float(input('Digite o valor do crédito: '))
if sal - deb + cred >= 0:
    print('Saldo Positivo')
else:
    print('Saldo Negativo')


