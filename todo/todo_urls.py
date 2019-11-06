from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoOverview.as_view(), name='todo_overview'),
    path('create', views.ToDoCreate.as_view(), name='todo_create'),
    path('<int:pk>', views.ToDoDetail.as_view(), name='todo_detail'),
]