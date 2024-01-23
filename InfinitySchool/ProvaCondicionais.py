# [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado e o valor da multa, 
# cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade=int(input("Digite a velocidade do carro:"))
if velocidade>80:
    print(f"Você foi multado em R${(velocidade-80)*20}")
else:
    print("Você não foi multado")

