tamanho=int(input('digite o tamanho da lista: '))
lista = list()

for i in range(tamanho):
	lista.append(int(input('Digite o valor da posição {} da lista: '.format(i+1))))

for i in range(int(tamanho/2)):
    aux=lista[i]
    lista [i] = lista[tamanho-(i+1)]
    lista[tamanho-(i+1)]=aux

print(lista)
