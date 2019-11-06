from django import forms
from todo.models import ToDo

class CreateTodoForm(forms.ModelForm):
	class Meta:
		model = ToDo
		widgets = {
			'tag_list': forms.CheckboxSelectMultiple()
		}

		fields = [
			'title_text',
			'notes',
			'do_by_date',
			'parent',
			'category',
			'tag_list'
		]

