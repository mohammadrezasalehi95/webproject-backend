# Generated by Django 2.1.5 on 2019-01-27 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_auto_20190127_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_report',
            name='id',
        ),
        migrations.AlterField(
            model_name='game_report',
            name='game',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sport.Game'),
        ),
    ]
