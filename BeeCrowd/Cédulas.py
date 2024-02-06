from math import trunc
# cedulas:
# 100
# 50
# 20
# 10
# 5
# 2
# 1
valor=int(input())
def quantidade_de_cedulas(cedula,valor):
    qtdCedulas=trunc(valor/cedula)
    return qtdCedulas
def valorRe(cedula,valor):
    valor=valor%cedula
    return valor
print(valor)
if valor>=100:
    cedula=100
    print(f"{quantidade_de_cedulas(cedula,valor)} nota(s) de R$ {cedula},00")
    valor=valorRe(cedula,valor)
else :
    print(f"0 nota(s) de R$ 100,00")
if valor>=50:
    cedula=50
    print(f"{quantidade_de_cedulas(cedula,valor)} nota(s) de R$ {cedula},00")
    valor=valorRe(cedula,valor)
else:
    print(f"0 nota(s) de R$ 50,00")
if valor>=20:
    cedula=20
    print(f"{quantidade_de_cedulas(cedula,valor)} nota(s) de R$ {cedula},00")
    valor=valorRe(cedula,valor)
else:
    print(f"0 nota(s) de R$ 20,00")
if valor>=10:
    cedula=10
    print(f"{quantidade_de_cedulas(cedula,valor)} nota(s) de R$ {cedula},00")
    valor=valorRe(cedula,valor)
else:
    print(f"0 nota(s) de R$ 10,00")
if valor>=5:
    cedula=5
    print(f"{quantidade_de_cedulas(cedula,valor)} nota(s) de R$ {cedula},00")
    valor=valorRe(cedula,valor)
else:
    print(f"0 nota(s) de R$ 5,00")
if valor>=2:
    cedula=2
    print(f"{quantidade_de_cedulas(cedula,valor)} nota(s) de R$ {cedula},00")
    valor=valorRe(cedula,valor)
else:
    print(f"0 nota(s) de R$ 2,00")
if valor>=1:
    cedula=1
    print(f"{quantidade_de_cedulas(cedula,valor)} nota(s) de R$ {cedula},00")
    valor=valorRe(cedula,valor)
else:
    print(f"0 nota(s) de R$ 1,00")

