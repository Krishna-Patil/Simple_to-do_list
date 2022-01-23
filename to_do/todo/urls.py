from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDoView.as_view(), name='todo'),
    path('<int:pk>/done/', DoneView.as_view(), name='done'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
]
