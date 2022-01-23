from re import template
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy

from .models import *


# Create your views here.
class ToDoView(ListView):
    model = ToDo
    template_name = 'todo.html'


class DoneView(DeleteView):
    model = ToDo
    template_name = 'done.html'
    success_url = reverse_lazy('todo')


class TaskCreateView(CreateView):
    model = ToDo
    template_name = 'create_task.html'
    fields = ['todo_task']
