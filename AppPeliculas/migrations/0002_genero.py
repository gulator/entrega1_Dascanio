# Generated by Django 4.0.4 on 2022-05-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPeliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=40)),
            ],
        ),
    ]
