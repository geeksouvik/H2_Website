# Generated by Django 3.0.8 on 2021-01-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210114_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(default='Update your department', max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(default='Update your year', max_length=1000),
        ),
    ]
