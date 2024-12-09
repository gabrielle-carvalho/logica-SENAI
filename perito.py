while True:
    telef = int(input("Se o suspeito telefonou para a vítima digite 1, caso contrário digite 0: "))
    if telef != 0 or telef != 1:
        break
while True:    
    local = int(input("Se o suspeito esteve no local onde a vítima estava digite 1, caso contrário digite 0: "))
    if local != 0 or local != 1:
        break
while True:
    mora = int(input("Se o suspeito mora perto da vítima digite 1, caso contrário digite 0: "))
    if mora != 0 or mora != 1:
        break
while True:
    dividas = int(input("Se o suspeito tinha dívidas com a vítima digite 1, caso contrário digite 0: "))
    if dividas != 0 or dividas != 1:
        break
while True:
    trabalhou = int(input("Se o suspeito trabalhou com a vítima digite 1, caso contrário digite 0: "))
    if trabalhou != 0 or trabalhou != 1:
        break
classificacao =  telef + local + mora + dividas + trabalhou
    
if classificacao  == 2:
    print("Suspeita")
if classificacao == 3 or classificacao == 4:
    print("Cúmplice")
if classificacao == 5:
    print("Assassino")
elif classificacao < 2:
    print("Inocente")
