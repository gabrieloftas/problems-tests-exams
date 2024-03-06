alunos = dict()
i=0

print("1 para visualizar todos os estudantes")
print("2 para adicionar um estudante")
print("3 para remover um estudante")
print("4 para total de estudantes")

while True:
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        if alunos:
            for chave, valor in alunos.items():
                print(f"{chave}: Nome: {valor['nome']}, Matrícula: {valor['matrícula']}")
        else:
            print("Não há alunos cadastrados.")
    elif opcao == 2:
        nome = input("Digite o nome do estudante: ")
        matricula = input("Digite a matrícula do estudante: ")  
        alunos[matricula] = {"nome": nome, "matrícula": matricula}
        i += 1
        print("Estudante adicionado com sucesso.")
    elif opcao == 3:
        matricula = input("Digite a matrícula do estudante para remover: ")
        if matricula in alunos:
            del alunos[matricula]
            print("Estudante removido com sucesso.")
            i -= 1
        else:
            print("Estudante não encontrado.")
    elif opcao == 4:
        print(f"Total de estudantes: {i}")
    else:
        print("Opção inválida")
        break
