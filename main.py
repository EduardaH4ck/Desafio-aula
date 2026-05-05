funcionarios = []
id_contador = 1

def cadastrar():
    global id_contador
    nome = input("Nome: ")
    setor = input("Setor: ")
    
    funcionario = {
        "id": id_contador,
        "nome": nome,
        "setor": setor
    }
    
    funcionarios.append(funcionario)
    id_contador += 1
    print("Funcionário cadastrado!\n")

def consultar_todos():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return
    
    for f in funcionarios:
        print(f)
    print()

def consultar_por_id():
    id_busca = int(input("Digite o ID: "))
    for f in funcionarios:
        if f["id"] == id_busca:
            print(f, "\n")
            return
    print("Funcionário não encontrado.\n")

def consultar_por_setor():
    setor_busca = input("Digite o setor: ")
    encontrados = [f for f in funcionarios if f["setor"] == setor_busca]
    
    if encontrados:
        for f in encontrados:
            print(f)
    else:
        print("Nenhum encontrado.")
    print()

def remover():
    id_busca = int(input("Digite o ID para remover: "))
    for f in funcionarios:
        if f["id"] == id_busca:
            funcionarios.remove(f)
            print("Removido!\n")
            return
    print("Funcionário não encontrado.\n")

while True:
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Todos")
    print("3 - Consultar por ID")
    print("4 - Consultar por Setor")
    print("5 - Remover Funcionário")
    print("6 - Encerrar Programa")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        consultar_todos()
    elif opcao == "3":
        consultar_por_id()
    elif opcao == "4":
        consultar_por_setor()
    elif opcao == "5":
        remover()
    elif opcao == "6":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!\n")
