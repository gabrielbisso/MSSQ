# Generated by Django 5.1.3 on 2024-11-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quest1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField()),
                ('sexo', models.FloatField(blank=True, null=True)),
                ('nao_aplicavel', models.FloatField(blank=True, null=True)),
                ('nunca', models.FloatField(blank=True, null=True)),
                ('raramente', models.FloatField(blank=True, null=True)),
                ('algumas_vezes', models.FloatField(blank=True, null=True)),
                ('frequentemente', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
