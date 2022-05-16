from multiprocessing.spawn import import_main_path
from django import views
from django.urls import path
from .views import TaskDetail, TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskAnalytic

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-analytic/', TaskAnalytic.as_view(), name='task-analytic'),
]


