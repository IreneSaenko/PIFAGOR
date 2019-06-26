from django.db import models

class Predict(models.Model):
    number = models.IntegerField()
    pred = models.TextField()
