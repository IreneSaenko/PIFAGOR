from django.db import models


class Pifs(models.Model):
    number=models.IntegerField()
    one= models.TextField()
    two=models.TextField()
    three=models.TextField()
    four=models.TextField()
    five=models.TextField()
    six=models.TextField()
    seven=models.TextField()
    eight=models.TextField()
    nine=models.TextField()

    def __num__(self):
        return self.number

class Numbers (models.Model):

    name = models.CharField(max_length=2)
    description = models.TextField()



