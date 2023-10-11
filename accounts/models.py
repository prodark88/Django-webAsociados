from django.db import models

# Create your models here.
class Profesion(models.Model):
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return self.profesion

class Account(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    profesiones = models.ManyToManyField(Profesion)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Enterprise(models.Model):
    name_enterprise = models.CharField(max_length=100)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    history = models.TextField(blank=True)
    values = models.TextField(blank=True)
    achievements = models.TextField(blank=True)

    def __str__(self):
        return self.name_enterprise
 