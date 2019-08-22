from django.db import models
from college.models import College

# Create your models here.
class Applicant(models.Model):
    college = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    college_fk = models.ForeignKey(College, on_delete=models.CASCADE)