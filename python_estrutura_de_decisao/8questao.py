#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
#estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
#quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
#Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
#mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.
qnt1 = int(input("Digite a quantidade atual do produto:"))
qntmax = int(input("Digite a quantidade máxima do estoque:"))
qntmin = int(input("Digite a quantidade mínima do estoque:"))
if (qntmax + qntmin)/2 >= qnt1:
    print("Não efetuar compra")
else:
    print("Efetuar compra")