
from django.db import models
from empresa.models import Agendamento
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=Agendamento.servico_agendado.through)
def atualizar_custo_agendamento(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        servicos = instance.servico_agendado.all()
        custo_total = 0
        for servico in servicos:
            if servico.preco_por_hora:
                duracao = instance.informacoes_padroes.duracao
                print('Duracao :', duracao)
                custo_total += (duracao/60) * servico.custo
                print("Custo do Item durante toda duração: ", custo_total)
        print("Servicos selecionados: ", servicos)
        print("Custo total :", custo_total)
        instance.custo_agendamento = custo_total if servicos else 0.0
        instance.save()