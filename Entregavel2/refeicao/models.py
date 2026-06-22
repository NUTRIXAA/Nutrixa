from django.db import models

class Refeicao(models.Model):
    nome = models.CharField(max_length=100)
    calorias = models.IntegerField()
    vegetariana = models.BooleanField(default=False)
    data_planejada = models.DateField()
    descricao = models.TextField()

    favorita = models.BooleanField(default=False)

    def __str__(self):
        return self.nome