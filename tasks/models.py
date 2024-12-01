from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('Copmleted', 'Выполнена'),
        ('Incompleted', 'Не выполнена')
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Низкий')
        ('Medium', 'Средний')
        ('High', 'Высокий')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    priority = models.CharField(
        max_length=10,
        choices=[('Low', 'Низкий'), ('Medium', 'Средний'), ('High', 'Высокий')]
    )
    due_date = models.DateField()
    status = models.CharField(
        max_length=15,
        choices=[('Incomplete', 'Не выполнена'), ('Complete', 'Выполнена')]
    )
