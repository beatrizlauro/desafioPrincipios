# controller.py
# Princípios aplicados:
# - Separação de interesses: Este módulo gerencia a lógica de negócio, sem se preocupar com a interface ou armazenamento.
# - Baixo acoplamento: Depende apenas da classe Task, sem conhecimento da interface de usuário.
# - Alta coesão: Todas as funções estão relacionadas ao gerenciamento de tarefas.
# - Modularidade: A lógica de negócio está isolada neste módulo.

from model import Task

class TaskController:
    def __init__(self):
        self.tasks = []  # Lista para armazenar as tarefas

    def add_task(self, title: str, description: str) -> Task:
        """Cadastra uma nova tarefa."""
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def list_tasks(self) -> list:
        """Retorna a lista de todas as tarefas."""
        return self.tasks

    def complete_task(self, index: int) -> bool:
        """Marca uma tarefa como concluída pelo índice."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            return True
        return False

    def delete_task(self, index: int) -> bool:
        """Exclui uma tarefa pelo índice."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False