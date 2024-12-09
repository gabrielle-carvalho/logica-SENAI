ano = date.today().year
codigo = int (input("Digite o seu código: "))
anoIngresso = int(input("Digite o ano de ingresso na empresa: "))
anoNascimento = int(input("Digite o seu ano de nascimento: "))

tempoTrabalho = (ano - anoIngresso)
idade = (ano - anoNascimento)

if idade >= 65 or tempoTrabalho >= 30 or tempoTrabalho >= 25 and idade >=60:
    print("Idade: ", idade, "\nTempo de trabalho: " , tempoTrabalho , "\nRequerer aposentadoria.")
else:
    print("Não requerer aposentadoria.")
