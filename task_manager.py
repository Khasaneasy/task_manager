import uuid
import json

from datetime import datetime
from typing import List


TASK_FILE = 'tasks.json'


class Task:
    def __init__(
            self,
            title: str,
            description: str,
            category: str,
            due_date: str,
            priority: str,
            id: str = None,
            status: str = 'Не выполнена'
            ):
        self.id = id if id else uuid.uuid4().hex
        self.title = title
        self.description = description
        self.category = category
        self.due_date = datetime.strptime(due_date, "%d.%m.%Y")
        try:
            datetime.strptime(due_date, "%d.%m.%Y")
            self.due_date = due_date
        except ValueError:
            raise ValueError(
                "Неверный формат даты. Ожидаемый формат: ДД.ММ.ГГГГ"
            )
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Название: {self.title}, Статус: {self.status}"

    def update(self,
               title: str = None,
               description: str = None,
               category: str = None,
               due_date: str = None,
               priority: str = None
               ):
        """Метод для обновления атрибутов задачи."""
        if title:
            self.title = title
        if description:
            self.description = description
        if category:
            self.category = category
        if due_date:
            self.due_date = datetime.strptime(due_date, "%d.%m.%Y")
        if priority:
            self.priority = priority


class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        """Загрузка всех задач."""
        try:
            with open(TASK_FILE, 'r') as file:
                data = json.load(file)
                return [Task(**task_data) for task_data in data]
        except FileNotFoundError:
            return []

    def save_tasks(self) -> None:
        """Сохранение задач."""
        with open(TASK_FILE, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def add_tasks(
            self,
            title: str,
            description: str,
            category: str,
            due_date: str,
            priority: str
    ) -> None:
        """Добавление задачи."""
        task = Task(title, description, category, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Задача '{task.title}' успешно добавлена!")

    def view_tasks(self) -> None:
        """Просмотр всех задач."""
        for task in self.tasks:
            print(task)

    def view_tasks_by_category(self, category: str) -> None:
        """Просмотр задач по категории."""
        filtered_tasks = [
            task for task in self.tasks if task.category == category
        ]
        if filtered_tasks:
            for task in filtered_tasks:
                print(f"ID: {task.id}, Название: {task.title}, "
                      f"Статус: {task.status}")
        else:
            print(f"Задачи в категории '{category}' не найдены!")

    def edit_tasks(self, task_id: str, new_data: dict) -> None:
        """Редактирование задачи по ID."""
        for task in self.tasks:
            if task.id == task_id:
                task.update(**new_data)
                self.save_tasks()
                print(f"Задача с ID {task_id} обновлена!")
                return
        print(f"Задача с ID {task_id} не найдена!")

    def delete_tasks_by_id(self, task_id: str) -> None:
        """Удаление задачи по ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        print(f"Задача с ID {task_id} удалена!")

    def delete_tasks_by_category(self, category: str) -> None:
        """Удаление задач по категории."""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.category != category]

        if len(self.tasks) < initial_count:
            self.save_tasks()
            print(f"Все задачи в категории '{category}' удалены!")
        else:
            print(f"Задачи в категории '{category}' не найдены.")

    def search_tasks(self, keyword: str = None, status: str = None) -> None:
        """Поиск задач по ключевым словам и статусу."""
        filtered_tasks = self.tasks
        if keyword:
            filtered_tasks = [
                task for task in filtered_tasks if keyword.lower()
                in task.title.lower()
                or keyword.lower() in task.description.lower()
            ]
        if status:
            filtered_tasks = [
                task for task in filtered_tasks if task.status == status
            ]

        if filtered_tasks:
            for task in filtered_tasks:
                print(task)
        else:
            print("Задачи по заданным критериям не найдены.")


if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nМеню:")
        print("1. Просмотр всех задач")
        print("2. Просмотр задач по категории")
        print("3. Добавление задачи")
        print("4. Редактирование задачи")
        print("5. Удаление задачи по ID")
        print("6. Удаление задач по категории")
        print("7. Поиск задач")
        print("8. Выход")

        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            task_manager.view_tasks()
        elif choice == "2":
            category = input("Введите категорию: ")
            task_manager.view_tasks_by_category(category)
        elif choice == "3":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            due_date = input("Введите срок выполнения (день-месяц-год): ")
            priority = input(
                "Введите приоритет задачи (Низкий/Средний/Высокий): "
            )
            task_manager.add_tasks(
                title,
                description,
                category,
                due_date,
                priority
            )
        elif choice == "4":
            task_id = input("Введите ID задачи для редактирования: ")
            new_data = {}
            new_data['title'] = input(
                "Новое название задачи (оставьте пустым, чтобы не менять): "
                )
            new_data['description'] = input(
                "Новое описание задачи (оставьте пустым, чтобы не менять): "
                )
            new_data['category'] = input(
                "Новая категория задачи (оставьте пустым, чтобы не менять): "
                )
            new_data['due_date'] = input(
                "Новый срок выполнения (оставьте пустым, чтобы не менять): "
                )
            new_data['priority'] = input(
                "Новый приоритет задачи (оставьте пустым, чтобы не менять): "
                )
            new_data = {key: value for key, value in new_data.items() if value}
            task_manager.edit_tasks(task_id, new_data)
        elif choice == "5":
            task_id = input("Введите ID задачи для удаления: ")
            task_manager.delete_tasks_by_id(task_id)
        elif choice == "6":
            category = input("Введите категорию задач для удаления: ")
            task_manager.delete_tasks_by_category(category)
        elif choice == "7":
            keyword = input(
                "Введите ключевое слово для поиска (можно оставить пустым): "
                )
            status = input(
                "Введите статус задачи для поиска"
                "(оставьте пустым, чтобы не фильтровать): "
                )
            task_manager.search_tasks(keyword, status)
        elif choice == "8":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
