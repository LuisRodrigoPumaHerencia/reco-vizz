# Generated by Django 4.1.2 on 2022-10-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_persona_delete_choices_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='contrasena',
            field=models.CharField(max_length=50, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.CharField(max_length=50, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.DateTimeField(verbose_name='FechaNacimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='primerApellido',
            field=models.CharField(max_length=50, verbose_name='PrimerApellido'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='primerNombre',
            field=models.CharField(max_length=50, verbose_name='PrimerNombre'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundoApellido',
            field=models.CharField(max_length=50, verbose_name='SegundoNombre'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundoNombre',
            field=models.CharField(max_length=50, verbose_name='SegundoNombre'),
        ),
    ]