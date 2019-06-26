from django.db import models

class Answers(models.Model):
    topic = models.CharField(max_length=30)
    text = models.TextField()
    name = models.CharField(max_length=30)
    email = models.TextField()
