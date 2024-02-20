email="bixodoido@goutlook.com"
senha="bixodoido123"
emailUser=input("Digite seu email: ")
senhaUser=input("Digite sua senha: ")
while emailUser!=email or senhaUser!=senha:
    print("Email ou senha incorretos")
    emailUser=input("Digite seu email: ")
    senhaUser=input("Digite sua senha: ")
print("Login Validado")