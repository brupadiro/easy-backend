# Generated by Django 2.2 on 2020-02-20 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gimnasios', '0004_auto_20200220_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('gimnasio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnasios.Gimnasios')),
            ],
        ),
    ]
