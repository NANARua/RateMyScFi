# Generated by Django 2.1.5 on 2022-03-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='posters'),
        ),
    ]
