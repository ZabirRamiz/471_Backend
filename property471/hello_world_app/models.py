from django.db import models

# Create your models here.
class hello_world_model(models.Model):
    hello = models.CharField( max_length=50)
    world = models.IntegerField()