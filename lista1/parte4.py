maior= lista[0]
menor=lista[0]
media=0

for i in range(tamanho):
	if(lista[i]>maior):
		maior= lista[i]
	elif(lista[i]<menor):
	    menor=lista[i]
media += lista[i]
media /= tamanho
print("A média da lista é {}".format(media))
print("O maior número da lista é: " , maior)
print("O menor número da lista é: " , menor)
