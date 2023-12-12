from django.contrib import admin
from empresa.models import Agendamento, ServicoAgendavel
from components.models import Cidade, DadosAgendamento, Endereco, Empresa, Estado

admin.site.register(Agendamento)
admin.site.register(ServicoAgendavel)
admin.site.register(Cidade)
admin.site.register(DadosAgendamento)
admin.site.register(Endereco)
admin.site.register(Empresa)
admin.site.register(Estado)