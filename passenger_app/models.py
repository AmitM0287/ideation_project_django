from django.db import models

# passenger_movement model
class passenger_movement(models.Model):
    Date = models.DateTimeField()
    ArrivalsActualCounts = models.IntegerField()
    DeparturesActualCounts = models.IntegerField()
