# Generated by Django 2.2 on 2020-03-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietas', '0002_auto_20200220_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dia',
            name='repeticiones',
        ),
        migrations.AddField(
            model_name='dia',
            name='cantidad',
            field=models.CharField(default='', max_length=100),
        ),
    ]
