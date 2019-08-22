from django.db import models

# Create your models here.
class College(models.Model):
    college_name = models.CharField(max_length=40)
