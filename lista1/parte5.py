tamanho=int(input('Digite o tamanho da lista: '))
lista = list()

for i in range(tamanho):
	lista.append(int(input('Digite o valor da posição {} da lista: '.format(i+1))))


busca = int(input('digite o numero que deseja: '))

if busca in lista:
    for i in range(int(tamanho)):
        if(lista[i]==busca):
            print('valor encontrado na posição{}' .format(i))
            encontrou = True
if (not encontrou):
    print('o numero nao esta na lista' )

print(lista)
