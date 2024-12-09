# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais 
# baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a
# cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de
# dados deve ser dado quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
# programa também deve ser informado os códigos e valores do cliente mais alto, do mais baixo,
# do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
codigoMaisPesado = 0
codigoMaisLeve = 0
codigoMaisAlto = 0
codigoMaisBaixo = 0

pesoMaior = 0
pesoMenor = 0
alturaMaisAlto = 0
alturaMaisBaixo = 0
somaPesos = 0
somaAlturas = 0
qtdClientes = 0

while True:
    codigo = input("Digite o codigo do cliente: ")
    if codigo == 0:
        break

    qtdClientes += 1
    altura = int(input("Digite a altura do cliente (em centímetros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))

    somaPesos += peso
    somaAlturas += altura

    if altura > alturaMaisAlto:
        alturaMaisAlto = altura
        codigoMaisAlto = codigo

    if altura < alturaMaisBaixo:
        alturaMaisBaixo = altura
        codigoMaisBaixo = codigo

    if peso > pesoMaior:
        pesoMaior = peso
        codigoMaisPesado = codigo

    if peso < pesoMenor:
        pesoMenor = peso
        codigoMaisLeve = codigo

mediaAlturas = somaAlturas / qtdClientes
mediaPesos = somaPesos / qtdClientes

print("O cliente mais alto é o que tem o código {codigoMaisAlto}" ," e ele possui {alturaMaisAlto}cm de altura\n" , "O cliente mais baixo é o que tem o código {codigoMaisBaixo}" , " e ele possui {alturaMaisBaixo}cm de altura\n" , "O cliente mais pesado é o que tem o código {codigoMaisPesado}" , " e ele pesa {pesoMaior:.2f}kg\n" , "O cliente mais leve é o que tem o código {codigoMaisLeve}" , " e ele pesa {pesoMenor:.2f}kg\n" , "A média de altura dos clientes é de {mediaAlturas:.2f}cm\n" , "A média de peso dos clientes é de {mediaPesos:.2f}kg")
