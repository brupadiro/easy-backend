# Generated by Django 2.2 on 2020-02-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_usuarios_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='username',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
