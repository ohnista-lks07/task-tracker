from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To do'),
        ('progres', 'In progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='todo')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


