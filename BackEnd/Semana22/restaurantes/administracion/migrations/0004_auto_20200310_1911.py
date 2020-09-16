# Generated by Django 3.0.4 on 2020-03-11 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(choices=[('LUN', 'LUNES'), ('MAR', 'MARTES'), ('MIE', 'MIERCOLES'), ('JUE', 'JUEVES'), ('VIE', 'VIERNES'), ('SAB', 'SABADO'), ('DOM', 'DOMINGO'), ('ALL', 'TODXS')], db_column='hor_dia', default='TODOS', max_length=20),
        ),
    ]
