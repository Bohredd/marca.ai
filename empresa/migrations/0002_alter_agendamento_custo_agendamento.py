# Generated by Django 5.0 on 2023-12-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='custo_agendamento',
            field=models.FloatField(blank=True, default=0.0, verbose_name='Custo do Agendamento'),
        ),
    ]
