# Generated by Django 5.0 on 2023-12-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosagendamento',
            name='duracao',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Duração do Agendamento'),
        ),
    ]
