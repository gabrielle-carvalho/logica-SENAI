salario = float (input("Digite o seu salário: "))
print(salario)

if salario < 280:
    print("Aumento de 20%")
    aumento1 = 20*salario/100
    print(aumento1, "aumento em reais")
    salarioNovo = aumento1+salario
    print(salarioNovo , "é o novo salário")

elif salario >= 280 and salario <=700:
    print("Aumento de 15%")
    aumento2 = 15*salario/100
    print(aumento2, "aumento em reais")
    salarioNovo2 = aumento2+salario
    print(salarioNovo2 , "é o novo salário")

elif salario >= 701 and salario <=1500:
    print("Aumento de 10%")
    aumento3 = 10*salario/100
    print(aumento3, "aumento em reais")
    salarioNovo3 = aumento3+salario
    print(salarioNovo3 , "é o novo salário")

elif salario >= 1501:
    print("Aumento de 5%")
    aumento4 = 5*salario/100
    print(aumento4, "aumento em reais")
    salarioNovo4 = aumento4+salario
    print(salarioNovo4 , "é o novo salário")
