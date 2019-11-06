from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='todo_index'),
    path('create', views.Create.as_view(), name='todo_create'),
]