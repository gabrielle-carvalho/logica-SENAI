#2. Faça um programa que leia um número indeterminado de notas. Após esta entrada de
#dados, faça o seguinte:
#• Mostre a quantidade de notas que foram lidas.
#• Exiba todas as notas na ordem em que foram informadas.
#• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
#• Calcule e mostre a soma das notas.
#• Calcule e mostre a média das notas.
#• Calcule e mostre a quantidade de notas acima da média calculada.

tamanho=int(input('Digite o tamanho da lista: '))
lista = list()

for i in range(tamanho):
	lista.append(int(input('Digite o valor da posição {} da lista: '.format(i+1))))
print(lista)

for i in range(int(tamanho/2)):
    aux=lista[i]
    lista [i] = lista[tamanho-(i+1)]
    lista[tamanho-(i+1)]=aux

print(lista)
media=0
print("A soma dos valores é: ",sum(lista))

media = sum(lista)/len(lista)
print("A média das notas é: ",media)

acima = 0
for valor_media in lista:  
    if valor_media > media:  
        acima += 1
print(acima , "notas ficaram acima da méida")
