# Generated by Django 3.0.5 on 2021-01-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0038_auto_20210121_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='council',
            name='picture',
            field=models.ImageField(default='avatar7.png', upload_to='images/'),
        ),
    ]