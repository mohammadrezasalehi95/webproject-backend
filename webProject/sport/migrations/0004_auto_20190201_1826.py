# Generated by Django 2.1.5 on 2019-02-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0003_auto_20190201_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
