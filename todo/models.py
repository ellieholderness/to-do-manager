from django.db import models

# Create your models here.
class ToDo(models.Model):
    title_text = models.CharField(max_length=150)
    notes = models.CharField(max_length=500)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        related_query_name='child',
        null=True,
    )

class Tag(models.Model):
    todo = models.ForeignKey(
        ToDo,
        on_delete=models.CASCADE,
        )
    name = models.CharField(max_length=20)