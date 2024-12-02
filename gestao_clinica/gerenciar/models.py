from django.db import models
from django.contrib.auth.models import User

class Especialidade(models.Model):
    especializacao = models.CharField(max_length=100)

    def __str__(self):
        return self.especializacao

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    convenio_saude = models.CharField(max_length=50)
    codigo_convenio = models.CharField(max_length=30, unique=True)
    plano_saude = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome

class Convenio(models.Model):
    nome_convenio = models.CharField(max_length=100)
    tipo_convenio = models.CharField(max_length=50)
    numero_convenio = models.CharField(max_length=30)
    validade = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_convenio

class Agendamento(models.Model):
    data_horario = models.DateTimeField()
    tipo_consulta = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Agendamento: {self.tipo_consulta} - {self.paciente.nome}"



