qtd = int(input("Quantas notas você necessita? "))
total = 0
for i in range (qtd):
    total += float(input("Digite a nota {} do aluno: ".format(i+1)))
media = total/qtd
print("A média do aluno é: {}".format(media))
