from django.db import models

class ServicoAgendavel(models.Model):

    nome_servico = models.CharField(max_length=200, verbose_name="Servico Ofertado")
    empresa_possuinte = models.ForeignKey('components.Empresa', verbose_name='Empresa',
                                          on_delete=models.CASCADE)
    custo = models.FloatField(verbose_name='Preço do Serviço')
    preco_por_hora = models.BooleanField(verbose_name="Preço por Hora?")

    def __str__(self):
        resultado = f'{self.nome_servico} - {self.empresa_possuinte.nome_empresa}'

        return resultado

class Agendamento(models.Model):

    servico_agendado = models.ManyToManyField('empresa.ServicoAgendavel', verbose_name='Servico Agendado')
    custo_agendamento = models.FloatField(verbose_name='Custo do Agendamento', blank=True, default=0.0)
    informacoes_padroes = models.ForeignKey('components.DadosAgendamento', on_delete=models.CASCADE, verbose_name='Dados do Agendamento')

    def __str__(self):
        nomes_servicos = [servico.nome_servico for servico in self.servico_agendado.all()]
        nomes_servicos = ', '.join(nomes_servicos)
        resultado_final = f'{nomes_servicos} - Custo: {self.custo_agendamento} e duração {self.informacoes_padroes.duracao} minutos'

        return resultado_final

    def save(self, *args, **kwargs):
        super(Agendamento, self).save(*args, **kwargs)