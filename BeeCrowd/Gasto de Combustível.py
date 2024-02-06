tempo=int(input())
velocidade=int(input())
distancia=tempo*velocidade
gasto=12#km/l
gastocal=1/gasto
resultado=distancia*gastocal#l
print(f"{resultado:.3f}")