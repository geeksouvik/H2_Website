# Generated by Django 3.0.5 on 2020-12-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0003_council_council_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='council',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
