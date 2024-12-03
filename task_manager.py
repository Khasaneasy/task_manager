import uuid
import json

from datetime import datetime


TASK_FILE = 'tasks.json'


def load_tasks():
    """Загрузка всех задач."""
    try:
        with open(TASK_FILE, 'r') as F:
            return json.load(F)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Сохранение задач."""
    with open(TASK_FILE, 'w') as F:
        return json.dump(tasks, F, indent=4)


def add_tasks(title, description, category, due_date, priority):
    """Добавление задач."""
    if not title or not description or not category or not due_date or not priority:
        print('Ошибка: Все поля должны быть заполнены!')
        return
    try:
        due_date = datetime.strptime(due_date, "%d.%m.%Y")
    except ValueError:
        print('Ошибка: Не верный формат даты!')
        return
    tasks = load_tasks()

    new_task = {
        'id': uuid.uuid4().hex,
        'title': title,
        'description': description,
        'category': category,
        'due_date': due_date.strftime("%d.%m.%Y"),
        'priority': priority,
        'status': 'Не выполнена'
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f'Задача {title} успешно добавлена!')


def view_tasks():
    """Просмотр всех задач."""
    tasks = load_tasks()
    for task in tasks:
        print(
            f"ID: {task['id']}, Название: {task['title']}, Статус: {task['status']}")


def view_tasks_category(category):
    """Просмотр задач по категориям."""
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task['category'] == category]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Название: {task['title']}, Статус: {task['status']}")
    else:
        print(f"Задачи в категории '{category}' не найдены!")


def edit_tasks(task_id, new_data):
    """Поиск по ID и обновление задач."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task.update(new_data)
            save_tasks(tasks)
            print(f'Задача с ID {task_id} обновлена!')
    print(f'Задача с ID {task_id} не найдена!')


def delete_tasks_by_id(task_id):
    """Удаление задач по ID."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Задача с ID {task_id} удалена!")
            return
    print(f"Задача с ID {task_id} не найдена.")


def delete_tasks_category(category):
    """Удаление задач по категориям."""
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task['category'] != category]
    if len(filtered_tasks) < len(tasks):
        save_tasks(filtered_tasks)
        print(f"Все задачи в категории '{category}' удалены!")
    else:
        print(f"Задачи в категории '{category}' не найдены.")


def search_tasks(keyword=None, status=None):
    """Поиск задач по ключевым словам и статусу."""
    tasks = load_tasks()

    filtered_tasks = tasks
    if keyword:
        filtered_tasks = [
            task for task in filtered_tasks 
            if keyword.lower() in task['title'].lower() or keyword.lower() in task['description'].lower()
        ]
    if status:
        filtered_tasks = [
            task for task in filtered_tasks 
            if task['status'] == status
        ]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Название: {task['title']}, Статус: {task['status']}")
    else:
        print("Задачи по заданным критериям не найдены.")


if __name__ == "__main__":
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
            view_tasks()
        elif choice == "2":
            category = input("Введите категорию: ")
            view_tasks_category(category)
        elif choice == "3":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            due_date = input("Введите срок выполнения (день-месяц-год): ")
            priority = input("Введите приоритет задачи (Низкий/Средний/Высокий): ")
            add_tasks(title, description, category, due_date, priority)
        elif choice == "4":
            task_id = input("Введите ID задачи для редактирования: ")
            new_data = {}
            new_data['title'] = input("Новое название задачи (оставьте пустым, чтобы не менять): ")
            new_data['description'] = input("Новое описание задачи (оставьте пустым, чтобы не менять): ")
            new_data['category'] = input("Новая категория задачи (оставьте пустым, чтобы не менять): ")
            new_data['due_date'] = input("Новый срок выполнения (оставьте пустым, чтобы не менять): ")
            new_data['priority'] = input("Новый приоритет задачи (оставьте пустым, чтобы не менять): ")
            new_data = {key: value for key, value in new_data.items() if value}
            edit_tasks(task_id, new_data)
        elif choice == "5":
            task_id = input("Введите ID задачи для удаления: ")
            delete_tasks_by_id(task_id)
        elif choice == "6":
            category = input("Введите категорию задач для удаления: ")
            delete_tasks_category(category)
        elif choice == "7":
            keyword = input("Введите ключевое слово для поиска (можно оставить пустым): ")
            status = input("Введите статус задачи для поиска (оставьте пустым, чтобы не фильтровать): ")
            search_tasks(keyword, status)
        elif choice == "8":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
