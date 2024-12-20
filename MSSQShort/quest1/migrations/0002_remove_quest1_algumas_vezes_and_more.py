# Generated by Django 5.1.3 on 2024-11-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest1',
            name='algumas_vezes',
        ),
        migrations.RemoveField(
            model_name='quest1',
            name='frequentemente',
        ),
        migrations.RemoveField(
            model_name='quest1',
            name='nao_aplicavel',
        ),
        migrations.RemoveField(
            model_name='quest1',
            name='nunca',
        ),
        migrations.RemoveField(
            model_name='quest1',
            name='raramente',
        ),
        migrations.AddField(
            model_name='quest1',
            name='autocarros',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='autocarros10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='aviões',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='aviões10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='baloiços',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='baloiços10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='carros',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='carros10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='carroseis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='carroseis10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='comboios',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='comboios10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='embarcacao_pequena',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='embarcacao_pequena10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='montanha_russa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='montanha_russa10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='navios',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quest1',
            name='navios10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quest1',
            name='sexo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
