qtd =  10
leves = 0
assintomaticos = 0
graves = 0
for i in range(qtd):
    entrada = int(input("Digite a condição do {} paciente\nPara sintomas leves 1: \nAssintomáticos 2: \n3 para sintomas graves: ".format(i+1))) 
    if (entrada == 1):
        leves+=1
    elif (entrada == 2):
        assintomaticos +=1
    elif (entrada == 3):
        graves+=1
    else:
        print("Valor inválido")

sintomasleves = leves/qtd*100
sintomasassintomaticos = assintomaticos/qtd*100
sintomasgraves = graves/qtd*100

print("Os pacientes com sistemas leves equivalem a {}% do total\nOs pacientes assintomáicos equivalem a {}% do total\nOs pacientes com sistemas graves equivalem a {}% do total".format(sintomasleves, sintomasassintomaticos, sintomasgraves))  
