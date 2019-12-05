from django.db import models

class Pokemon(models.Model):
    serial = models.IntegerField(null = True)
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, null = True)
    total = models.IntegerField(null = True)
    hp = models.IntegerField(null = True)
    attack = models.IntegerField(null = True)
    defense = models.IntegerField(null = True)
    sp_atk = models.IntegerField(null = True)
    sp_def = models.IntegerField(null = True)
    speed = models.IntegerField(null = True)
    generation = models.IntegerField(null = True)
    legend = models.BooleanField(null = True)

    def __str__(self):
        return self.name
