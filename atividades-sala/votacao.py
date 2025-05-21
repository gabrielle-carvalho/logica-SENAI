c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
branco = 0

eleitores = int(input("Número de eleitores: "))
for n in range(eleitores):
    voto = int(input("Vote em 1, 2, 3 ou 4(Os brancos serão 0 e os nulos qualquer valor que não seja o dos candidatos): "))
    if (voto == 1):
        c1 = c1 + 1
    elif (voto == 2):
        c2 = c2 + 1
    elif (voto == 3):
        c3 = c3 + 1
    elif(voto == 0):
        branco = branco + 1
    else:
        nulo = nulo + 1

print("O candidato 1 recebeu:", c1, "votos.")
print("O candidato 2:", c2, "votos.")
print("O candidato 3:", c3, "votos.")
print("Nulos: ", nulo)
print("Brancos: " , branco)

print("Porcentagem de votos brancos = ", 100*(branco/eleitores) , "%")
print("Porcentagem de votos nulos = ", 100*(nulo/eleitores) , "%")
