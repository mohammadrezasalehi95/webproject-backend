# Generated by Django 2.1.5 on 2019-01-31 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0005_auto_20190131_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
