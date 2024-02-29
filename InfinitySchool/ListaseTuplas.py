numeros=[];par=[];impar=[]
for i in range(0,10,1):
    numeros.append(int(input("Digite um número: ")))
print(numeros)
for i in numeros:
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)
par=tuple(par)
impar=tuple(impar)
print(par)
print(impar)
print("A quantidade de números pares é: ",len(par))
print("A quantidade de números ímpares é: ",len(impar))
print("A soma dos números pares é: ",sum(par))
print("A soma dos números ímpares é: ",sum(impar))


    