# Generated by Django 2.2.5 on 2019-10-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20191008_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='todos', to='todo.Tag'),
        ),
    ]