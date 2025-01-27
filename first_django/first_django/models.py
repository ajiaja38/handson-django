from django.db import models

class Cat(models.Model):
  name = models.CharField(max_length=200)
  color = models.CharField(max_length=50)
  type = models.CharField(max_length=200)