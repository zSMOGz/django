from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12,
                                  decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=8,
                               decimal_places=2)
    size = models.DecimalField(max_digits=8,
                               decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(Buyer,
                                   related_name='buyers')

    def __str__(self):
        return self.title