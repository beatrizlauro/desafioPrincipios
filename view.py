from controller import TaskController

class TaskView:
    def __init__(self):
        self.controller = TaskController()

    def show_menu(self):
        """Exibe o menu principal e gerencia a interação com o usuário."""
        while True:
            print("\nSistema de Controle de Tarefas\n")
            print("1. Cadastrar tarefa")
            print("2. Listar tarefas")
            print("3. Marcar tarefa como concluída")
            print("4. Excluir tarefa")
            print("5. Sair")
            choice = input("\nEscolha uma opção: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("\nSaindo...")
                break
            else:
                print("\nOpção inválida!")

    def add_task(self):
        """Solicita dados para cadastrar uma nova tarefa."""
        title = input("\nTítulo da tarefa: ")
        description = input("Descrição da tarefa: ")
        try:
            self.controller.add_task(title, description)
            print("\nTarefa cadastrada com sucesso!")
        except ValueError as e:
            print(f"\nErro: {e}")

    def list_tasks(self):
        """Exibe todas as tarefas cadastradas."""
        tasks = self.controller.list_tasks()
        if not tasks:
            print("\nNenhuma tarefa cadastrada.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}: {task}")

    def complete_task(self):
        """Marca uma tarefa como concluída."""
        try:
            index = int(input("\nDigite o índice da tarefa a marcar como concluída: "))
            if self.controller.complete_task(index - 1):
                print("\nTarefa marcada como concluída!")
            else:
                print("\nÍndice inválido!")
        except ValueError:
            print("\nEntrada inválida! Digite um número.")

    def delete_task(self):
        """Exclui uma tarefa."""
        self.list_tasks()
        try:
            index = int(input("\nDigite o índice da tarefa a excluir: "))
            if self.controller.delete_task(index - 1):
                print("\nTarefa excluída com sucesso!")
            else:
                print("\nÍndice inválido!")
        except ValueError:
            print("\nEntrada inválida! Digite um número.")

def main():
    view = TaskView()
    view.show_menu()

if __name__ == "__main__":
    main()