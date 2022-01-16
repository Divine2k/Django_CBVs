from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk':self.pk})



class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveBigIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=CASCADE)

    def __str__(self):
        return self.name

