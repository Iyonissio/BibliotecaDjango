from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200, null=True)
    celular = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

