from django.db import models
from django.contrib.postgres.fields import JSONField

class Names(models.Model):
    name = JSONField()

