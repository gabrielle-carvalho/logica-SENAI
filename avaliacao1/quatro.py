#leia 20 números inteiros e armazene-os num vetor. Armazene os númerospares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
lista = []
lista_par = []
lista_impar = []
for i in range(5):
    num=int(input("Digite um número: "))
    lista=num
    if num%2==0:
        lista_par = num
    else:
        lista_impar = num
        
print("Lista: ",lista)
print("Números ímpares: " , lista_impar)
print("Números pares: ",lista_par)
