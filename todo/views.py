from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from todo.forms.todo_create_form import CreateTodoForm


def index(request):
    return HttpResponse("Hello, viewer. One day this page will be functional.")


class Create(CreateView):
	template_name = "todo_create.html"
	form_class = CreateTodoForm
	success_url = reverse_lazy('todo_index')