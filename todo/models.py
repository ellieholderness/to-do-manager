from django.db import models
from django.urls import reverse

# Create your models here.
class ToDo(models.Model):
    title_text = models.CharField(
        max_length=150,
    )

    notes = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )

    do_by_date = models.DateField(
        'Do-by date',
        null=True,
        blank=True,
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        related_query_name='child',
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='todos',
        null=True,
    )

    tag_list = models.ManyToManyField(
        'Tag',
        related_name='todos',
        blank=True,
        )

    def tags(self):
        return ", ".join([str(t) for t in self.tag_list.all()])

    def __str__(self):
        return self.title_text

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])

class Tag(models.Model):
    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(
        max_length=20,
        primary_key=True,
    )

    def __str__(self):
        return self.name