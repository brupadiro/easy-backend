# Generated by Django 2.2 on 2020-02-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gimnasios', '0003_planes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planes',
            name='duracion',
        ),
        migrations.AddField(
            model_name='planes',
            name='duracion_dias',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
