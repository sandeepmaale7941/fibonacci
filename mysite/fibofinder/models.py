from django.db import models

# Create your models here.
class Fibonacci(models.Model):
    number = models.PositiveIntegerField()
    fibo_number = models.PositiveIntegerField()

