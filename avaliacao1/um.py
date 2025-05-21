nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
media = (nota1 + nota2)/2 
print("Média: ", media)

if media >= 9:
    print("Conceito A, aluno aprovado.")
elif media >= 7.5 and media <=8.9:
    print("Conceito B, aluno aprovado.")
elif media >= 6 and media <=7.4:
    print("Conceito C, aluno aprovado.")
elif media >= 4 and media <=5.9:
    print("Conceito D, aluno reprovado.")
elif media <= 3.9:
    print("Conceito E, aluno reprovado.")
