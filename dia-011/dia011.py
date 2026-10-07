opcao = None
tarefas = []

while True:  
    print("===== GERENCIADOR DE TAREFAS =====")
    print("1 — Adicionar tarefa")
    print("2 — Listar tarefas")
    print("3 — Pesquisar tarefa")
    print("4 — Remover tarefa")
    print("5 — Ordenar tarefas")
    print("6 — Sair")
    opcao = input()
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao not in (1,2,3,4,5,6):
                print("Digite uma opção valida!")
                continue
        elif opcao == 6:
                break
        else:
            if opcao == 1:
                tarefa = input("Digite a nova tarefa que deseja adicionar")
                tarefas.append(tarefa)
            elif opcao == 2:
                print("===== TAREFAS =====")
                for i in tarefas:
                    print(f"{i+1}")
    else:
        print("Digite uma opção valida!")

    
print(opcao)        
print("Fim do programa")


