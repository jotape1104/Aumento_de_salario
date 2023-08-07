salario = float(input('Digite seu salário: R$'))
dezporc = salario * 10 / 100
quinporc = salario * 15 / 100
if salario > 1250.00:
    aum10 = salario + dezporc
    print('De acordo com seu sálario de R${:.2f} você teve um aumento de 10%, e agora recebe R${:.2f}'.format(salario, aum10))
else:
    aum15 = salario + quinporc
    print('De acordo com seu sálario de R${:.2f} você teve um aumento de 15%, e agora recebe R${:.2f}'.format(salario, aum15))
