from django.db import models

class DadosAgendamento(models.Model):

    inicio = models.TimeField(verbose_name="Horário de Início")
    termino = models.TimeField(verbose_name="Horário de Término")
    data = models.DateField(verbose_name="Data do Agendamento")
    duracao = models.PositiveSmallIntegerField(verbose_name="Duração do Agendamento", blank=True, null=True, default=0)

    def __str__(self):
        return f'Inicio: {self.inicio} Termino: {self.termino} Data: {self.data} Duracao: {self.duracao} minutos'
    
    def save(self, *args, **kwargs):

        if self.inicio > self.termino:
            raise ValueError("O horário de término deve ser maior que o horário de início.")
        
        duracao = (self.termino.hour - self.inicio.hour) * 60 + (self.termino.minute - self.inicio.minute)
        self.duracao = duracao

        super(DadosAgendamento, self).save(*args, **kwargs)

class Estado(models.Model):

    nome = models.CharField(max_length=100, verbose_name="Nome do Estado")
    sigla = models.CharField(max_length=5, verbose_name="Sigla da UF")

    def __str__(self):
        return f'Estado: {self.nome} com UF: {self.sigla}'
    

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    estado = models.ForeignKey('components.Estado', on_delete=models.CASCADE, verbose_name='Estado da Cidade')

    def __str__(self):
        return f'Cidade: {self.nome} do estado: {self.estado.nome}'
    

class Endereco(models.Model):

    cidade = models.ForeignKey('components.Cidade', on_delete=models.CASCADE, verbose_name='Cidade do Endereço')
    logradouro = models.CharField(max_length=200, verbose_name="Endereço")
    bairro = models.CharField(max_length=100, verbose_name="Nome do Bairro")
    numero = models.CharField(max_length=20, verbose_name="Número do Local")
    complemento = models.CharField(max_length=100, verbose_name="Complemento", null=True, blank=True)

    def __str__(self):
        return f'Cidade {self.cidade.nome} endereço {self.logradouro},{self.bairro},{self.numero}'

class Empresa(models.Model):

    TIPOS_NEGOCIO_CHOICES = [
        (' ', 'Escolha o tipo do negócio'),
        ('ESPORTES', 'Esportes'),
        ('SAÚDE', 'Saúde'),
        ('OUTRO', 'Outro')
    ]

    nome_empresa = models.CharField(max_length=250, verbose_name="Nome da Empresa")
    slug_empresa = models.SlugField(verbose_name="Slug da Empresa")
    endereco = models.ForeignKey('components.Endereco', verbose_name='Endereço da Empresa', on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, verbose_name='Telefone da Empresa')
    tipo_negocio = models.CharField(
        max_length=8,
        choices=TIPOS_NEGOCIO_CHOICES,
        default=' ',
        verbose_name='Tipo do Negócio'
    )

    def __str__(self):
        return f'Empresa {self.nome_empresa} com tipo de negócio {self.tipo_negocio}'
    
    class Meta:
        db_table = 'empresas_empresa'