# Generated by Django 5.0 on 2023-12-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_agendamento_informacoes_padroes'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicoagendavel',
            name='preco_por_hora',
            field=models.BooleanField(default=False, verbose_name='Preço por Hora?'),
            preserve_default=False,
        ),
    ]