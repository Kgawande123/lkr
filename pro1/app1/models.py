from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER = [('female','Female'),('male','Male')]
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=23)
    city = models.CharField(max_length=34)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=23,choices=GENDER)
    profile_pic = models.ImageField(upload_to="profile/")