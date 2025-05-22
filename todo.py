import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Tarefa adicionada.")

def mark_done(tasks, idx):
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Listar tarefas\n2. Adicionar tarefa\n3. Marcar como concluída\n4. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            list_tasks(tasks)
        elif op == "2":
            title = input("Título da tarefa: ")
            add_task(tasks, title)
            tasks = load_tasks()
        elif op == "3":
            list_tasks(tasks)
            idx = int(input("Número da tarefa para marcar como concluída: ")) - 1
            mark_done(tasks, idx)
            tasks = load_tasks()
        elif op == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()