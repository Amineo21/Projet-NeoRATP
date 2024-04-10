from django.db import models

# Create your models here.
class Train (models.Model) :
    trainId = models.AutoField(primary_key = True)
    number = models.PositiveIntegerField()
    # pour avoir que des valeurs positives
    destination = models.CharField(max_length = 20)
    date = models.TimeField()
    # pour avoir une valeur corespondant à l'heure
    