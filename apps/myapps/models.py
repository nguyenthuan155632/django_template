from django.db import models

# Create your models here.

class Myapps(models.Model):
    field1 = models.CharField(max_length=20)
    field2 = models.DateTimeField('field 2')