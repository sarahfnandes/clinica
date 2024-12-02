from django.contrib import admin
from .models import Especialidade, Clinica, Medico, Paciente, Convenio, Agendamento
from django.apps import apps

admin.site.register(Especialidade)
admin.site.register(Clinica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Convenio)
admin.site.register(Agendamento)

