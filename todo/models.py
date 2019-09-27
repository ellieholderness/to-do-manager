from django.db import models

# Create your models here.
class ToDo(models.Model):
    title_text = models.CharField(
        max_length=150,
    )

    notes = models.CharField(
        max_length=500,
        null=True,
    )

    do_by_date = models.DateField(
        'Do-by date',
        null=True,
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        related_query_name='child',
        null=True,
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='todos',
        related_query_name='todo',
        null=True,
    )

class Tag(models.Model):
    todo = models.ForeignKey(
        ToDo,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=20,
    )

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(
        max_length=20,
    )