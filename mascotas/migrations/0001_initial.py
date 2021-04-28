# Generated by Django 3.1.7 on 2021-04-27 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('abreviatura', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='razas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('abreviatura', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('id_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.tipos')),
            ],
        ),
        migrations.CreateModel(
            name='mascotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('tiene_vacunas', models.BooleanField(null=True)),
                ('estado', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('id_raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.razas')),
                ('id_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.tipos')),
            ],
        ),
    ]