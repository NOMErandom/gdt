import json
from datetime import datetime

# Arquivo JSON para salvar as tarefas
TASKS_FILE = "tasks.json"

# Carregar tarefas do arquivo JSON
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"pending": [], "completed": []}

# Salvar tarefas no arquivo JSON
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Adicionar uma nova tarefa
def add_task(description, deadline, priority):
    tasks = load_tasks()
    task = {
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "added_on": datetime.now().isoformat()
    }
    tasks["pending"].append(task)
    save_tasks(tasks)
    print("Tarefa adicionada com sucesso!")

# Listar tarefas pendentes ou concluídas
def list_tasks(status="pending"):
    tasks = load_tasks()
    for idx, task in enumerate(tasks[status], 1):
        print(f"{idx}. {task['description']} | Prazo: {task['deadline']} | Prioridade: {task['priority']}")

# Marcar uma tarefa como concluída
def mark_task_as_completed(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks["pending"]):
        task = tasks["pending"].pop(task_index)
        tasks["completed"].append(task)
        save_tasks(tasks)
        print("Tarefa marcada como concluída!")
    else:
        print("Índice de tarefa inválido.")

# Remover uma tarefa
def remove_task(task_index, status="pending"):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks[status]):
        tasks[status].pop(task_index)
        save_tasks(tasks)
        print("Tarefa removida com sucesso!")
    else:
        print("Índice de tarefa inválido.")

# Filtrar tarefas por prioridade
def filter_tasks_by_priority(priority):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks["pending"] if task["priority"].lower() == priority.lower()]
    for idx, task in enumerate(filtered_tasks, 1):
        print(f"{idx}. {task['description']} | Prazo: {task['deadline']} | Prioridade: {task['priority']}")

# Interface de comando para o usuário
def main():
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas Pendentes")
        print("3. Listar Tarefas Concluídas")
        print("4. Marcar Tarefa como Concluída")
        print("5. Remover Tarefa")
        print("6. Filtrar Tarefas por Prioridade")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            description = input("Descrição da tarefa: ")
            deadline = input("Prazo (AAAA-MM-DD): ")
            priority = input("Prioridade (alta, média, baixa): ")
            add_task(description, deadline, priority)

        elif choice == "2":
            print("\nTarefas Pendentes:")
            list_tasks("pending")

        elif choice == "3":
            print("\nTarefas Concluídas:")
            list_tasks("completed")

        elif choice == "4":
            list_tasks("pending")
            task_index = int(input("Índice da tarefa a marcar como concluída: ")) - 1
            mark_task_as_completed(task_index)

        elif choice == "5":
            status = input("Remover de pendentes ou concluídas? (pending/completed): ")
            list_tasks(status)
            task_index = int(input("Índice da tarefa a remover: ")) - 1
            remove_task(task_index, status)

        elif choice == "6":
            priority = input("Filtrar por prioridade (alta, média, baixa): ")
            filter_tasks_by_priority(priority)

        elif choice == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
