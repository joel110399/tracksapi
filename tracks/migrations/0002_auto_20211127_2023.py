# Generated by Django 3.2.9 on 2021-11-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='genre',
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ManyToManyField(to='tracks.Genre', verbose_name='Genre'),
        ),
    ]
