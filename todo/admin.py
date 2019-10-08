from django.contrib import admin
from .models import ToDo, Tag, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
	list_display = (
		'title_text',
		'notes',
		'do_by_date',
		'parent',
		'category',
	)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'todo')