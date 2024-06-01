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
    
    
class Docto(models.Model):
    Doct_Name           =   models.CharField(max_length=50)
    Doct_Email          =   models.EmailField()
    Doct_Gender         =   models.CharField(max_length=10)
    Doct_PhoneNumber    =   models.CharField(max_length=12)
    Doct_Address        =   models.TextField()
    Doct_DOB            =   models.DateField()
    Doct_BloodGroup     =   models.CharField(max_length=10)
    Specialization      =   models.CharField(max_length=50)
    def __str__(self):
        return self.Doct_Name