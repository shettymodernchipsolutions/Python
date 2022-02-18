from django.db import models

class Marks(models.Model):
    Name = models.CharField(max_length=50)
    Roll_no = models.IntegerField()
    English = models.IntegerField()
    Tamil = models.IntegerField()
    Science = models.IntegerField()
    Maths = models.IntegerField()
    Social = models.IntegerField()
    Hindi = models.IntegerField()
    Average = models.IntegerField()
    Status = models.CharField(max_length=10)
    def __str__(self):
        return self.Name





