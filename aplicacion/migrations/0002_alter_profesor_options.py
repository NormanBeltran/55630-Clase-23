# Generated by Django 4.2 on 2023-08-15 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['nombre'], 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
    ]
