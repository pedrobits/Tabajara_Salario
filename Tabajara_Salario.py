
Salario = float(input("Qual o seu salario? R$"))

if Salario <= 280.00:
    aumento = Salario+Salario*20/100
    print(
        "Seu salario de R${} terá o reajuste de 20%, ficando assim R${}".format(Salario,aumento)
        )
elif Salario <= 700.00:
    aumento1 = Salario+Salario*15/100
    print(
        "Seu Salario de R${} terá o reajuste de 15%, ficando assim R${}".format(Salario,aumento1)
    )
elif Salario <= 1500:
    aumento2 = Salario+Salario*10/100
    print("Seu salario de R${} terá o reajuste de 10%, ficando assim R${}".format(Salario,aumento2))
elif Salario > 1500:
    aumento3 = Salario+Salario*5/100
    print("Seu salario de R${} terá o reajuste de 5%, ficando assim R${}".format(Salario,aumento3))

