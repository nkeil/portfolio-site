from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
