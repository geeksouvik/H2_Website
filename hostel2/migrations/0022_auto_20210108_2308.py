# Generated by Django 3.0.5 on 2021-01-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0021_alumnitestimony_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnitestimony',
            name='pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
