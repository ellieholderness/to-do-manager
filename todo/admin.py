from django.contrib import admin
from .models import ToDo, Tag

admin.site.register(ToDo)
admin.site.register(Tag)