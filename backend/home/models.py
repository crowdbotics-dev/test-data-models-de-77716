from django.conf import settings
from django.db import models
class House(models.Model):
    'Generated Model'
    bedroom = models.BigIntegerField()
