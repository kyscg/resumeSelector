from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_applicant = models.BooleanField('Is applicant', default=False)
    is_recruiter = models.BooleanField('Is recruiter', default=False)
    pdf_resume = models.FileField(upload_to='resumes/pdfs', blank=True, null=True)

    GENDER_CHOICES = (
        ('N', ''),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="N")

class Document(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='documents')

    def __str__(self) -> str:
        return self.title

