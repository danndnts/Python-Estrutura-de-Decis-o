#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
val1 = float(input("Digite o primeiro valor:"))
val2 = float(input("Digite o segundo valor:"))
if val1 > val2:
    print("{}<{}" .format(val2, val1))
else:
    print("{}<{}" .format(val1, val2))