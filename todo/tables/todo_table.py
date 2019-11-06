import django_tables2 as tables

from todo.models import ToDo

class ToDoTable(tables.Table):
	class Meta:
		model = ToDo
		fields = [
			'title_text',
			'do_by_date',
			'parent',
			'category',
			'tag_list'
		]

	title_text = tables.Column(
        verbose_name="Title",
        linkify=True
    )
	do_by_date = tables.Column(
		verbose_name="Do-by date"
	)
	parent = tables.Column(
        verbose_name='Parent Task'
    )
	category = tables.Column(
        initial_sort_descending=True,
    )
	tag_list = tables.Column(
        verbose_name="Tags",
    )