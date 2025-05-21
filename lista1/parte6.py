tamanho=int(input('Digite o tamanho da lista: '))
lista = list()

for i in range(tamanho):
	lista.append(int(input('Digite o valor da posição {} da lista:  '.format(i+1))))
#busca = int(input('Digite o numero que deseja: '))

listaPares = list()

for i in range(tamanho):
    if (lista[i]%2 == 0):
        listaPares.append(lista[i])
print("A lista de números pares é {}".format(listaPares))
 #matriz = [['5','6','7'],['8','9','3'],['2','4','1']]
#print(matriz)
tamanho=int(input('Digite o tamanho da lista: '))
lista = list()

for i in range(tamanho):
	lista.append(int(input('Digite o valor da posição {} da lista:  '.format(i+1))))
#busca = int(input('Digite o numero que deseja: '))

listaPares = list()

for i in range(tamanho):
    if (lista[i]%2 == 0):
        listaPares.append(lista[i])
print("A lista de números pares é {}".format(listaPares))
