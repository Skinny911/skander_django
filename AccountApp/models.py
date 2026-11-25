from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, RegexValidator

class User(AbstractUser):
    pass


regex_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="Champ doit contenir 8 chiffres."
)

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 

class Doctor(User):
    license_number = models.CharField(max_length=8, unique=True, validators=[regex_validator])
    phone = models.CharField(max_length=8, validators=[regex_validator])
    specialties = models.ManyToManyField(Specialty, related_name='doctors')
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'



class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[regex_validator])
    phone = models.CharField(max_length=8 , validators=[regex_validator])
    birth_date = models.DateField()
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
