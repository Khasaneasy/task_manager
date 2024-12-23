# Описание проекта
Task Manager — консольное приложение на Python для управления задачами. Приложение позволяет создавать, редактировать, удалять и просматривать задачи с различными атрибутами, такими как приоритет, категория и срок выполнения. Все данные хранятся в JSON-файле.

## Основные возможности
1. Просмотр всех задач — выводит список всех задач.
2. Просмотр задач по категории — фильтрация задач по заданной категории.
3. Добавление задачи — создание новой задачи с уникальным идентификатором.
4. Редактирование задачи — изменение свойств задачи по её ID.
5. Удаление задачи по ID — удаляет задачу по указанному идентификатору.
6. Удаление задач по категории — удаляет все задачи в выбранной категории.
7. Поиск задач — поиск по ключевым словам и статусу.
8. Выход — завершение работы программы.


### Установка и запуск
```bash
git clone <https://github.com/Khasaneasy/task_manager>
```
```bash
cd task_manager
```
```bash
python task_manager.py
```

#### Формат данных
```json
{
  "id": "уникальный идентификатор",
  "title": "Название задачи",
  "description": "Описание задачи",
  "category": "Категория",
  "due_date": "ДД.ММ.ГГГГ",
  "priority": "Низкий/Средний/Высокий",
  "status": "Не выполнена/Выполнена"
}
```

# Автор
https://github.com/Khasaneasy