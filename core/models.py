from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    
class PatientProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    def __str__(self):
        return self.user.username
    
class DoctorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    specialization=models.CharField(max_length=10)
    def __str__(self):
        return self.user.username
    
class VitalSigns(models.Model):
    patient=models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    heart_rate=models.IntegerField()
    temperature=models.FloatField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.heart_rate} - {self.temperature} at {self.timestamp}  "
    
    
    
    
    
