# Generated by Django 2.1.5 on 2019-01-27 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_auto_20190127_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamgame',
            name='game',
        ),
        migrations.RemoveField(
            model_name='teamgame',
            name='team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='games',
        ),
        migrations.DeleteModel(
            name='TeamGame',
        ),
    ]
