from django.db import models
from django.urls import reverse
# Create your models here.


class ToDo(models.Model):
    todo_task = models.CharField(max_length=70)

    def __str__(self):
        return self.todo_task

    def get_absolute_url(self):
        return reverse('todo')
