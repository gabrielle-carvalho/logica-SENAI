indice = float(input ("Qual foi o índice de poluição na sua cidade hoje? "))
if(indice>=0.05 and indice<= 0.25):
    print("Indice de polução aceitável")
else:
    if (indice>0.25 and índice<=0.3):
            print("As empresa do 1° grupo devem suspender as atividades.")
    if(indice <= 0.4 and indice >0.3):
            print("As indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades.")
    if (indice <= 0.5 and indice >0.4):
            print("Todos os grupos devem ser notificados a paralisarem suas atividades.")
