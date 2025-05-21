tamanho=int(input('digite o tamanho da lista:'))
lista = list()

for i in range(tamanho):
	lista.append(int(input('digite o valor da posição{} da lista'.format(i+1))))
print(lista)
maior= lista[0]
menor=lista[0]

for i in range(tamanho):
	if(lista[i]>maior):
		maior= lista[i]
	elif(lista[i]<menor):
		menor=lista[i]
print("O maior número da lista é: " , maior)
print("O menor número da lista ´: " , menor)
