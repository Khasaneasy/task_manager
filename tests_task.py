import pytest
from datetime import datetime

from tasks.task_manager import TaskManager


@pytest.fixture
def task_manager():
    """Фикстура для создания экземпляра TaskManager."""
    return TaskManager()


def test_add_tasks(task_manager):
    """Тест на добавление задачи в TaskManager."""
    title = "Задача 1"
    description = "Описание задачи 1"
    category = "Работа"
    due_date = "01.01.2025"
    priority = "Низкий"

    task_manager.add_tasks(title, description, category, due_date, priority)

    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == title
    assert task_manager.tasks[0].description == description
    assert task_manager.tasks[0].category == category
    assert task_manager.tasks[0].due_date == datetime.strptime(due_date, "%d.%m.%Y")
    assert task_manager.tasks[0].priority == priority
    assert task_manager.tasks[0].status == "Не выполнена"


def test_edit_tasks(task_manager):
    """Тест на изменение и обновление задачи в TaskManager."""
    task_manager.add_tasks(
        "Задача 1",
        "Описание задачи 1",
        "Работа",
        "01.01.2025",
        "Низкий"
    )
    task_id = task_manager.tasks[0].id

    new_data = {
        "title": "Измененная задача",
        "description": "Измененное описание",
        "category": "Личное",
        "due_date": "02.02.2025",
        "priority": "Средний"
    }
    task_manager.edit_tasks(task_id, new_data)

    updated_task = task_manager.tasks[0]
    assert updated_task.title == "Измененная задача"
    assert updated_task.description == "Измененное описание"
    assert updated_task.category == "Личное"
    assert updated_task.due_date == datetime.strptime("02.02.2025", "%d.%m.%Y")
    assert updated_task.priority == "Средний"
    assert updated_task.status == "Не выполнена"


def test_search_tasks(task_manager, capsys):
    """Тест на поиск по ключевым словам и статусу задачи в TaskManager."""
    task_manager.add_tasks(
        "Задача 1",
        "Описание задачи 1",
        "Работа",
        "01.01.2025",
        "Низкий"
    )
    task_manager.add_tasks(
        "Задача 2",
        "Описание задачи 2",
        "Личное",
        "01.02.2025",
        "Средний"
    )

    task_manager.search_tasks(keyword="Задача 1")
    captured = capsys.readouterr()
    assert "Задача 1" in captured.out
    assert "Задача 2" not in captured.out

    task_manager.search_tasks(status="Низкий")
    captured = capsys.readouterr()
    assert "Задача 1" in captured.out
    assert "Задача 2" not in captured.out


def test_delete_tasks_by_id(task_manager):
    """Тест на удаление задачи по ID в TaskManager."""
    task_manager.add_tasks(
        "Задача 1",
        "Описание задачи 1",
        "Работа",
        "01.01.2025",
        "Низкий"
    )
    task_id = task_manager.tasks[0].id

    task_manager.delete_tasks_by_id(task_id)

    assert len(task_manager.tasks) == 0


def test_view_tasks_by_category(task_manager, capsys):
    """Тест на удаление задачи по категориям в TaskManager."""
    task_manager.add_tasks(
        "Задача 1",
        "Описание задачи 1",
        "Работа",
        "01.01.2025",
        "Низкий"
        )
    task_manager.add_tasks(
        "Задача 2",
        "Описание задачи 2",
        "Личное",
        "01.02.2025",
        "Средний"
    )

    task_manager.view_tasks_by_category("Работа")

    captured = capsys.readouterr()

    assert "Задача 1" in captured.out
    assert "Задача 2" not in captured.out


def test_add_tasks_invalid_due_date(task_manager):
    """Тест на добавление задачи с некорректной датой выполнения."""
    title = "Задача с неправильной датой"
    description = "Описание задачи с неправильной датой"
    category = "Работа"
    due_date = "01.01.2025"
    priority = "Средний"

    with pytest.raises(ValueError):
        task_manager.add_task(title, description, category, due_date, priority)