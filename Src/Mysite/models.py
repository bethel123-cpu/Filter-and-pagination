from django.db import models

# Create your models here.
MALE = 'male'
FEMALE = 'female'

GENDER_CHOICES = [
    (MALE, MALE),
    (FEMALE, FEMALE),
]


class patients(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    age = models.IntegerField(default=5)
