# Generated by Django 3.0.4 on 2020-03-10 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='nombre',
            field=models.CharField(db_column='res_nom', max_length=40, verbose_name='Razon Social'),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(db_column='suc_id', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='suc_nom', max_length=50, verbose_name='Direccion')),
                ('latitud', models.DecimalField(db_column='suc_lat', decimal_places=8, max_digits=10)),
                ('longitud', models.DecimalField(db_column='suc_long', decimal_places=8, max_digits=10)),
                ('telefono', models.CharField(db_column='suc_fono', max_length=10)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sucursales', to='administracion.Restaurante')),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
                'db_table': 't_sucursal',
            },
        ),
    ]
