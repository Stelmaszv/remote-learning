from django.db import models
class Classroom(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
