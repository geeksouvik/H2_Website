# Generated by Django 3.0.8 on 2021-01-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0036_auto_20210121_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='council',
            name='headingstyle',
        ),
        migrations.AddField(
            model_name='council_category',
            name='headingstyle',
            field=models.CharField(default='adminstyle', max_length=150),
        ),
    ]
