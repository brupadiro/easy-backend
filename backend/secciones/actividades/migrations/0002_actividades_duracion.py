# Generated by Django 2.2 on 2020-02-20 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='duracion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
