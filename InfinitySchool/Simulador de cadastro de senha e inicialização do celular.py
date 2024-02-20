print("Digite a senha cadastrada no celular")
senha="123456"
senha_digitada=0
acerto=False
for i in range(3,0,-1):
    senha_digitada=input("Digite a senha: ")
    if senha_digitada==senha:
        print("Senha correta")
        acerto=True
        break
    else:
        print("Senha incorreta")
        print("Digite a senha novamente")
        print(f"Você tem mais {i-1} tentativas")
if acerto==False:
    print("celular bloqueado")
    print("Compre outro celular")
else:
    print("Celular desbloqueado")

    

        
