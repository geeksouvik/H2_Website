# Generated by Django 3.1.4 on 2020-12-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0016_auto_20201223_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legends',
            name='year',
            field=models.IntegerField(),
        ),
    ]
