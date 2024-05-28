from django.db import models

# Create your models here.
class PatientModel(models.Model):
    Name        =   models.CharField(max_length=50)
    Email       =   models.EmailField(unique=True)
    Gender      =   models.CharField(max_length=50)
    PhoneNumber =   models.CharField(max_length=12)
    Address     =   models.TextField()
    BirthDate   =   models.DateField()
    bloodGroup  =   models.CharField(max_length=5)

    def __str__(self):
        return self.Name