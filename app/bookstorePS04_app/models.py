from django.db import models

# Create your models here.
class Carte(models.Model):
    titlu = models.CharField(max_length = 256)
    autor = models.CharField(max_length = 64)
    an = models.IntegerField()
    tara = models.CharField(max_length = 64)
    subiect = models.CharField(max_length = 256)

    def __str__(self):
        return f"{self.id}: {self.titlu}, scrisă de {self.autor}."