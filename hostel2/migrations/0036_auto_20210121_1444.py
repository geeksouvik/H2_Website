# Generated by Django 3.0.8 on 2021-01-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0035_council_bordercolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='council',
            name='bordercolor',
        ),
        migrations.RemoveField(
            model_name='council',
            name='headingcolor',
        ),
        migrations.AddField(
            model_name='council',
            name='headingstyle',
            field=models.CharField(default='adminstyle', max_length=150),
        ),
    ]
