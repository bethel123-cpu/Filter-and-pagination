# Generated by Django 3.2.4 on 2021-06-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50),
        ),
    ]
