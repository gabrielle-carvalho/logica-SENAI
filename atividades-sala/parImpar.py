lista = list()

for i in range(20):
	lista.append(int(input('Digite o valor da posição {} da lista:  '.format(i+1))))
    
listaPares = list()

for i in range(20):
    if (lista[i]%2 == 0):
        listaPares.append(lista[i])
print("A lista de números pares é {}".format(listaPares))

listaImpares = list()
for i in range(20):
    if (lista[i]%2 != 0):
        listaImpares.append(lista[i])
print("A lista de números ímpares é {}".format(listaImpares))
