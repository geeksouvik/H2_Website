# Generated by Django 3.0.5 on 2021-01-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel2', '0041_council_category_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(default='avatar7.png', upload_to='testimonial/')),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]