from django.db import models

class Hive(models.Model):
    name = models.CharField(max_length=250, unique=True, default="Kein Name vorhanden")
    location = models.CharField(max_length=250)
    started = models.DateField

    def __str__(self):
        return self.name

class Measurement(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    day = models.IntegerField(default=-1)
    month = models.IntegerField(default=-1)
    year = models.IntegerField(default=-1)
    timestamp = models.DateTimeField
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    pressure = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.day) + "." + str(self.month) + "." + str(self.year)