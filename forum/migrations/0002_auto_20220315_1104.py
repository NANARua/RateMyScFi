# Generated by Django 2.1.5 on 2022-03-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=''),
        ),
    ]