# Generated by Django 4.1.2 on 2022-10-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_persona_fechanacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.DateField(verbose_name='Fecha Nacimiento'),
        ),
    ]
