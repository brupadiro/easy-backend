# Generated by Django 2.2 on 2020-02-09 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_infocliente_gym_socio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='vendedor',
        ),
    ]
