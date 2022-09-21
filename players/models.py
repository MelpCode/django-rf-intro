from django.db import models

# Create your models here.
class Player(models.Model):
  fullname = models.CharField(max_length=200)
  age = models.PositiveIntegerField()
  height=models.FloatField()
  subtitute=models.BooleanField()
  country=models.CharField(max_length=200)
  price = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)