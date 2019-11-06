from django import forms
from todo.models import ToDo

class CreateTodoForm(forms.ModelForm):
	class Meta:
		model = ToDo
		fields = [
			'title_text',
			'notes',
			'do_by_date',
			'parent',
			'category',
			'tag_list'
		]

