from django.db import models

class Aufgabe(models.Model):
    titel = models.CharField(max_length=200)
    beschreibung = models.TextField()

    def __str__(self):
        return self.titel

