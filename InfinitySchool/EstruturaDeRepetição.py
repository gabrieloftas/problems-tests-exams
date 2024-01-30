numeros=[9999]
i=1
idx=1
soma=0
while numeros[i-1]!=0:
    numerosaux=int(input("Digite um número: "))
    numeros.append(numerosaux)
    i+=1
quantidade=len(numeros)-2
print(f"Você digitou {quantidade} números")
while idx<=quantidade:
    soma+=numeros[idx]
    idx+=1 
print(f"A soma dos números é {soma}")
media=soma/quantidade
print(f"A média aritmética dos números é {media}")
def mostrarnumeros():
    idx=1
    while idx<=quantidade:
        print(numeros[idx])
        idx+=1

print("Deseja ver os números digitados?")
print("1 - Sim")
print("0 - Não")
opcao=int(input("Digite a opção desejada: "))
if opcao==1:
    mostrarnumeros()
elif opcao==0:
    print("Programa finalizado")
else:
    print("Pare de tentar quebrar o programa, por favor")

 
