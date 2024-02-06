velx=60
vely=90
dist0=0
velrel=vely-velx
#tempo=dist/velrel
dist=int(input())
t=dist/velrel
t=t*60
print(f"{t:.0f} minutos")
