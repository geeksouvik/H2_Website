# Generated by Django 3.0.8 on 2021-01-21 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0034_council_headingcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='council',
            name='bordercolor',
            field=models.CharField(default='gold', max_length=150),
        ),
    ]
