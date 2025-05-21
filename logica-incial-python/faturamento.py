valorFixo = float(input("Qual é o valor? (Em toneladas?) "))
meses = int(input("Digite a quantidade de meses: "))
i = 0
faturamento = 0
while i < meses:
    toneladas = float(input("Quantas toneladas saíram? "))
    faturamento += toneladas
    i+= 1
faturamento *= valorFixo
print("O valor total faturado foi de: ", faturamento)
