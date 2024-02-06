nome=input()
salario=float(input())
vendas=float(input())
bonus=vendas*0.15
salariofinal=salario+bonus
print("TOTAL = R$ {:.2f}".format(salariofinal))