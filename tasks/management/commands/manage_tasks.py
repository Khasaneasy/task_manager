import json

from datetime import datetime
from django.core.management.base import BaseCommand

from tasks.models import Task


class Command(BaseCommand):
    help = 'Управление задачами'

    def add_task(self, title, description, category, due_date, priority):
        pass

    def view_task(self, category=None):
        pass

    def edit_task(self, task_id, title=None, description=None, category=None, due_date=None, priority=None):
        pass

    def delete_task(self, task_id):
        pass

    def search_task(self, keyword=None, category=None, status=None):
        pass

    def handle(self, *args, **kwargs):
        pass


#Шаблон, надо дополнить все мтоды 