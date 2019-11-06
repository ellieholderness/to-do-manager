from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django_tables2 import SingleTableView

from todo.forms.todo_create_form import CreateTodoForm
from todo.models import ToDo
from todo.tables.todo_table import ToDoTable


class ToDoOverview(SingleTableView):
    model = ToDo
    template_name = "todo_overview.html"
    table_class = ToDoTable

    def get_queryset(self):
        return ToDo.objects.all().order_by('do_by_date')

class ToDoCreate(CreateView):
	template_name = "todo_create.html"
	form_class = CreateTodoForm
	success_url = reverse_lazy('todo_index')

class ToDoDetail(DetailView):
	model = ToDo
	template_name = "todo_detail.html"