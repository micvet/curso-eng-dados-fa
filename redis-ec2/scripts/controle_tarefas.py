import redis

# Adicionar uma tarefa
def adicionar_tarefa(conn, descricao):

    id_tarefa = conn.incr('contador_tarefas')

    chave_tarefa = f'tarefa:{id_tarefa}'

    conn.set(chave_tarefa, descricao)
    return id_tarefa

# Visualizar as tarefas na lista
def visualizar_tarefas(conn):
    contador_tarefas = int(conn.get('contador_tarefas') or 0)
    for id_tarefa in range(1, contador_tarefas + 1):
        chave_tarefa = f'tarefa:{id_tarefa}'
        descricao_tarefa = conn.get(chave_tarefa)
        if descricao_tarefa:
            print(f'Tarefa {id_tarefa}: {descricao_tarefa.decode()}')

# Remover uma tarefa da lista
def remover_tarefa(conn, id_tarefa):
    chave_tarefa = f'tarefa:{id_tarefa}'
    if conn.exists(chave_tarefa):
        conn.delete(chave_tarefa)
        print(f'Tarefa {id_tarefa} removida com sucesso!')
    else:
        print(f'Tarefa {id_tarefa} não encontrada na lista.')

if __name__ == "__main__":
    # Conectar ao redis
    conn = redis.Redis()

    while True:
        print("\n1. Adicionar Tarefa\n2. Visualizar Tarefas\n3. Remover Tarefa\n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            id_tarefa = adicionar_tarefa(conn, descricao)
            print(f'Tarefa {id_tarefa} adicionada com sucesso!')

        elif opcao == '2':
            print("\nLista de Tarefas:")
            visualizar_tarefas(conn)

        elif opcao == '3':
            id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
            remover_tarefa(conn, id_tarefa)

        elif opcao == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
