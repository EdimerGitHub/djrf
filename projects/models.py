from django.db import models

# Create your models here.
class Project(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    tecnhology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
