from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    type2= models.CharField(max_length=50)
    total=models.IntegerField()
    hp=models.IntegerField()
    attack=models.IntegerField()
    defense=models.IntegerField()
    sp_atk=models.IntegerField()
    sp_def=models.IntegerField()
    speed=models.IntegerField()
    generation=models.IntegerField()
    legend=models.BooleanField()

    def __str__(self):
        return self.name
