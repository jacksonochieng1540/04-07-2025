from rest_framework import serializers
from.models import User,PatientProfile,DoctorProfile,VitalSigns

class VitalSignsSerializers(serializers.ModelSerializer):
    class Meta:
        model=VitalSigns
        field='__all__'
        
        
class PatientProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model=PatientProfile
        field='__all__'
        
class DoctorProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model=DoctorProfile
        field='__all__'
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        field=['id','username','is_patient','is_doctor']
