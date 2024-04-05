#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
#forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
maca = float(input("Digite a quantidade de maçãs:"))
if maca < 12:
    print(maca * 1.3)
else:
    print(maca * 1)