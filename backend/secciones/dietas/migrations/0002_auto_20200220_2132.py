# Generated by Django 2.2 on 2020-02-20 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gimnasios', '0004_auto_20200220_2007'),
        ('dietas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rutinas',
            new_name='Dietas',
        ),
        migrations.RenameField(
            model_name='dietas',
            old_name='nombre_rutina',
            new_name='nombre_dieta',
        ),
        migrations.RemoveField(
            model_name='dia',
            name='rutina',
        ),
        migrations.AddField(
            model_name='dia',
            name='dieta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dietas.Dietas'),
            preserve_default=False,
        ),
    ]
