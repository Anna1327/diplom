# Generated by Django 3.1.1 on 2020-09-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_auto_20200913_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Operator', 'Operator'), ('Supervisor', 'Supervisor')], default='Supervisor', max_length=20),
        ),
    ]
