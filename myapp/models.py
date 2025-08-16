from django.db import models
from libro.models import Libro 

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True, blank=True)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)