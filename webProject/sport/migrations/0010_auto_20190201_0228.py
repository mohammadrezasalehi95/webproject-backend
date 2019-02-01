# Generated by Django 2.1.5 on 2019-02-01 02:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0009_auto_20190201_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='cup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/sport/competition'),
        ),
        migrations.AddField(
            model_name='league',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/sport/competition'),
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 2, 1, 2, 27, 59, 674500, tzinfo=utc), null=True),
        ),
    ]