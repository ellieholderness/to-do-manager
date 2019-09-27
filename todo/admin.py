from django.contrib import admin
from .models import ToDo, Tag, Category

admin.site.register(ToDo)
admin.site.register(Tag)
admin.site.register(Category)