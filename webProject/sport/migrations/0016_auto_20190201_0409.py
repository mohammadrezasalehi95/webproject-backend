# Generated by Django 2.1.5 on 2019-02-01 04:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0015_auto_20190201_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 2, 1, 4, 9, 11, 691792, tzinfo=utc), null=True),
        ),
    ]
