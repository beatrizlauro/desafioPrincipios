# model.py
# Princípios aplicados:
# - Encapsulamento: Atributos privados com getters e setters (usando propriedades).
# - Abstração: A classe Task representa uma tarefa de forma abstrata, escondendo detalhes de implementação.
# - Alta coesão: A classe Task é responsável apenas por gerenciar os dados e o comportamento de uma única tarefa.

class Task:
    def __init__(self, title: str, description: str):
        self._title = title
        self._description = description
        self._status = "pendente"  # Status inicial é pendente

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value.strip():
            raise ValueError("O título não pode ser vazio")
        self._title = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def status(self) -> str:
        return self._status

    def mark_as_completed(self):
        self._status = "concluída"

    def __str__(self) -> str:
        return f"Título: {self._title}, Descrição: {self._description}, Status: {self._status}"