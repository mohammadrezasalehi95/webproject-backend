# Generated by Django 2.1.5 on 2019-01-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_auto_20190126_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='assets/sport/teams'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='assets/sport/players'),
        ),
    ]
