from django.db import models

# passenger_movement model
class passenger_movement(models.Model):
    Date = models.CharField(max_length=20)
    ArrivalsActualCounts = models.IntegerField()
    DeparturesActualCounts = models.IntegerField()
